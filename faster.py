import pandas as pd
import requests
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

def extract_file_id(drive_url):
    """
    Extracts the Google Drive or Docs file ID from the URL.
    Handles formats:
      - https://drive.google.com/file/d/<ID>/
      - https://docs.google.com/document/d/<ID>/
      - https://...id=<ID>
    """
    m = re.search(r'/[a-zA-Z]+/d/([^/?&]+)', drive_url)
    if m:
        return m.group(1)
    m = re.search(r'[?&]id=([^&]+)', drive_url)
    if m:
        return m.group(1)
    return None

def check_link(name, url, session, timeout=10):
    if not isinstance(url, str) or not url.startswith("http"):
        return name, False, "No URL", url

    file_id = extract_file_id(url)
    if not file_id:
        return name, False, "Invalid URL", url

    # Determine appropriate method and URL
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
    body = resp.text.lower() if method == session.get else ""

    # Handle known permission issues
    if "accounts.google.com" in final or "servicelogin" in final:
        return name, False, "Login required", url
    if status == 403:
        return name, False, "Forbidden (403)", url
    if status == 404:
        return name, False, "Not Found (404)", url
    if method == session.get and any(kw in body for kw in ("you need permission", "access denied", "request access")):
        return name, False, "Permission denied", url
    if status in (200, 302, 303):
        return name, True, "Public", url

    return name, False, f"HTTP {status}", url

if __name__ == "__main__":
    # Configuration
    excel_path = "Students-Registration-For-Placement-Drives.xlsx"
    sheet_name = "CS"
    name_col = 1   # Column B (0-indexed)
    url_col = 12   # Column M (0-indexed)
    max_workers = 12

    # Load with pandas
    df = pd.read_excel(excel_path, sheet_name=sheet_name, header=None, skiprows=[0], engine="openpyxl")

    # Filter out rows with both name and url missing
    df_filtered = df[[name_col, url_col]].dropna(how="all")

    names = df_filtered[name_col].astype(str).str.strip().tolist()
    urls  = df_filtered[url_col].astype(str).str.strip().tolist()

    session = requests.Session()
    session.headers.update({"User-Agent": "DriveLinkChecker/1.0"})

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(check_link, n, u, session) for n, u in zip(names, urls)]
        for future in as_completed(futures):
            results.append(future.result())

    # Display results
    print(f"{'Name':<30} | {'OK':<2} | {'Status':<18} | URL")
    print("-" * 110)
    failures = []
    for name, ok, msg, url in results:
        mark = "✅" if ok else "❌"
        print(f"{name:<30} | {mark:<2} | {msg:<18} | {url}")
        if not ok:
            failures.append((name, msg))

    # Summary
    if failures:
        print("\nStudents with inaccessible links:")
        for name, reason in failures:
            print(f"  {name} → {reason}")
    else:
        print("\n✅ All links are publicly accessible!")
