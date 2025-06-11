import json
import argparse
import asyncio
import requests
from playwright.async_api import async_playwright


def load_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def send_telegram(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        resp = requests.post(url, data=payload, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")


def classify_type(title, price, thresholds):
    title_lower = title.lower()
    if price <= thresholds['mainline']:
        return 'mainline'
    if 'premium' in title_lower or price > thresholds['silver']:
        return 'premium'
    if price <= thresholds['silver']:
        return 'silver'
    return None


async def scrape_page(page, keyword, page_num, thresholds, tolerance, include_oos):
    url = f"https://www.amazon.in/s?k={keyword.replace(' ', '+')}&page={page_num}"
    await page.goto(url, timeout=60000)
    await page.wait_for_selector('div.s-result-item[data-asin]')

    items = []
    cards = await page.query_selector_all('div.s-result-item[data-asin]')
    for card in cards:
        try:
            title_el = await card.query_selector('h2 a span')
            title = await title_el.inner_text()
            link_el = await card.query_selector('h2 a')
            href = await link_el.get_attribute('href')
            url_full = 'https://www.amazon.in' + href.split('?')[0]

            price_whole = await card.query_selector('span.a-price-whole')
            if not price_whole:
                if include_oos:
                    price = None
                else:
                    continue  # skip out-of-stock items
            else:
                whole = await price_whole.inner_text()
                frac_el = await card.query_selector('span.a-price-fraction')
                frac = await frac_el.inner_text() if frac_el else '00'
                price = float(whole.replace(',', '') + '.' + frac)

            car_type = classify_type(title, price or 0, thresholds)
            if car_type and price is not None and price <= thresholds[car_type] + tolerance:
                items.append({'title': title, 'url': url_full, 'price': price, 'type': car_type})
        except Exception:
            continue
    return items


async def main(args):
    cfg = load_config(args.config)
    keyword = cfg.get('search_keyword', 'hot wheels')
    pages = cfg.get('pages_to_scan', 3)
    thresholds = cfg['price_thresholds']
    tolerance = cfg.get('price_tolerance', 0)
    include_oos = cfg.get('filters', {}).get('include_out_of_stock', False)
    notif = cfg['notification']

    alerts = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        )
        for i in range(1, pages + 1):
            results = await scrape_page(page, keyword, i, thresholds, tolerance, include_oos)
            alerts.extend(results)
            print(results)
        await browser.close()

    if not alerts:
        print("No items at or below M.R.P. found.")
        return

    for item in alerts:
        msg = f"✅ {item['title']} at ₹{int(item['price'])} ({item['type'].capitalize()})\n🔗 {item['url']}"
        if notif['method'] == 'telegram':
            tg = notif['telegram']
            send_telegram(tg['bot_token'], tg['chat_id'], msg)
        else:
            print(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hot Wheels MRP Notifier')
    parser.add_argument('--config', type=str, required=True, help='Path to config.json')
    args = parser.parse_args()
    asyncio.run(main(args))