import pandas as pd
import requests
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor, as_completed

def extract_file_id(drive_url):
    if "id=" in drive_url:
        return parse_qs(urlparse(drive_url).query).get("id", [None])[0]
    if "/file/d/" in drive_url:
        return drive_url.split("/file/d/")[1].split("/")[0]
    if "/document/d/" in drive_url:
        return drive_url.split("/document/d/")[1].split("/")[0]
    return None

def check_link(name, url, session, timeout=10):
    """
    Returns (name, ok, msg, url) for a single link check.
    Uses HEAD for Drive files, GET for Docs.
    """
    if not isinstance(url, str) or not url.startswith("http"):
        return name, False, "No URL", url

    file_id = extract_file_id(url)
    if not file_id:
        return name, False, "Invalid URL", url

    # choose method/endpoint
    if "docs.google.com/document" in url:
        method, check_url = session.get, url
    else:
        method, check_url = session.head, f"https://drive.google.com/uc?export=download&id={file_id}"

    try:
        resp = method(check_url, allow_redirects=True, timeout=timeout)
    except Exception:
        return name, False, "Request error", url

    final = resp.url
    status = resp.status_code

    # quick login/permission gates from headers and URL
    if "accounts.google.com" in final or "ServiceLogin" in final:
        return name, False, "Login required", url
    if status in (403, ):
        return name, False, "Forbidden (403)", url
    if status in (404, ):
        return name, False, "Not Found (404)", url
    # treat 200/302/303 as public
    if status in (200, 302, 303):
        return name, True, "Public", url

    return name, False, f"HTTP {status}", url

if __name__ == "__main__":
    excel_path  = "Students-Registration-For-Placement-Drives.xlsx"
    sheet_name  = "CS"
    name_idx    = 1
    url_idx     = 12
    max_workers = 10   # tune this to your bandwidth/CPU

    # load sheet
    df = pd.read_excel(
        excel_path, sheet_name=sheet_name,
        skiprows=[0], header=None, engine="openpyxl"
    )
    names = df[name_idx].astype(str).tolist()
    urls  = df[url_idx].astype(str).tolist()

    # prepare session
    session = requests.Session()
    session.headers.update({"User-Agent": "DriveLinkChecker/1.0"})

    # parallel check
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as exe:
        futures = [
            exe.submit(check_link, name, url, session)
            for name, url in zip(names, urls)
        ]
        for fut in as_completed(futures):
            results.append(fut.result())

    # print
    print(f"{'Name':<30s} | {'OK':<2s} | {'Status':<16s} | URL")
    print("-" * 100)
    inaccessible = []
    for name, ok, msg, url in results:
        mark = "✅" if ok else "❌"
        print(f"{name:<30s} | {mark:<2s} | {msg:<16s} | {url}")
        if not ok:
            inaccessible.append((name, msg))

    # summary
    if inaccessible:
        print("\nStudents with inaccessible links:")
        for name, reason in inaccessible:
            print(f"  {name} → {reason}")
    else:
        print("\nAll links are publicly accessible!")
