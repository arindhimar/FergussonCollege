import pandas as pd
import requests
from urllib.parse import urlparse, parse_qs

def extract_file_id(drive_url):
    if "id=" in drive_url:
        return parse_qs(urlparse(drive_url).query).get("id", [None])[0]
    elif "/file/d/" in drive_url:
        return drive_url.split("/file/d/")[1].split("/")[0]
    return None

def is_drive_link_public(drive_url, timeout=10):
    file_id = extract_file_id(drive_url)
    if not file_id:
        return False, "Invalid URL"
    check_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    try:
        resp = requests.get(check_url, allow_redirects=True, timeout=timeout)
    except Exception as e:
        return False, f"Request error"
    final, body = resp.url, resp.text.lower()
    if "accounts.google.com" in final or "serviceLogin" in final:
        return False, "Login required"
    if "you need permission" in body or "access denied" in body:
        return False, "Permission denied"
    if resp.status_code in (200,302,303):
        return True, "Public"
    return False, f"HTTP {resp.status_code}"

def process_sheet_numeric(
    excel_path, sheet_name,
    link_idx=12, fallback_idx=13,
    start_id=246200
):
    # 1) Read sheet skipping only the top descriptive row, no header
    df = pd.read_excel(
        excel_path, sheet_name=sheet_name,
        skiprows=[0], header=None
    )

    # 2) Add roll number column 'A'
    df.insert(0, 'A', range(start_id, start_id + len(df)))

    inaccessible = []

    # 3) Iterate rows
    for _, row in df.iterrows():
        roll = row['A']
        url = row[link_idx]
        # fallback value if URL missing
        fallback = row[fallback_idx]
        if not isinstance(url, str) or not url.startswith("http"):
            ok, msg = False, "No URL"
        else:
            ok, msg = is_drive_link_public(url)

        if not ok:
            # print and collect
            print(f"Roll {roll} | {msg:16s} | {url}")
            inaccessible.append((roll, url, msg))

    return inaccessible

if __name__ == "__main__":
    bad = process_sheet_numeric(
        excel_path="Students-Registration-For-Placement-Drives.xlsx",
        sheet_name="CS",
        link_idx=12,
        fallback_idx=13,
        start_id=246201
    )

    print("\nSummary: roll numbers whose Drive link failed:\n")
    for roll, url, reason in bad:
        print(f"{roll} → {reason}")
