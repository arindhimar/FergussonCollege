import pandas as pd
import requests
from urllib.parse import urlparse, parse_qs

def extract_file_id(drive_url):
    """
    Extracts the file or document ID from Google Drive or Docs share URLs.
    """
    if "id=" in drive_url:
        return parse_qs(urlparse(drive_url).query).get("id", [None])[0]
    if "/file/d/" in drive_url:
        return drive_url.split("/file/d/")[1].split("/")[0]
    if "/document/d/" in drive_url:
        return drive_url.split("/document/d/")[1].split("/")[0]
    return None

def is_drive_link_public(url, timeout=10):
    """
    Returns (bool, message) indicating if a Drive or Docs link is publicly accessible.
    """
    file_id = extract_file_id(url)
    if not file_id:
        return False, "Invalid URL"

    if "docs.google.com/document" in url:
        check_url = url
    else:
        check_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    try:
        resp = requests.get(check_url, allow_redirects=True, timeout=timeout)
    except Exception:
        return False, "Request error"

    final = resp.url
    body = resp.text.lower()
    status = resp.status_code

    if "accounts.google.com" in final or "serviceLogin" in final:
        return False, "Login required"
    if "you need permission" in body or "access denied" in body:
        return False, "Permission denied"
    if "sign in" in body and "google.com" in final:
        return False, "Sign-in required"

    if status in (200, 302, 303):
        return True, "Public"
    if status == 403:
        return False, "Forbidden (403)"
    if status == 404:
        return False, "Not Found (404)"
    return False, f"HTTP {status}"

if __name__ == "__main__":
    excel_path   = "Students-Registration-For-Placement-Drives.xlsx"
    sheet_name   = "CS"
    name_idx     = 1    
    url_col_idx  = 12   

    df = pd.read_excel(
        excel_path,
        sheet_name=sheet_name,
        skiprows=[0],
        header=None,
        engine="openpyxl"
    )

    names = df[name_idx].astype(str).tolist()
    urls  = df[url_col_idx].astype(str).tolist()

    inaccessible = []
    print(f"{'Name':<30s} | {'OK':<2s} | {'Status':<16s} | URL")
    print("-" * 100)
    for name, url in zip(names, urls):
        if not url.startswith("http"):
            ok, msg = False, "No URL"
        else:
            ok, msg = is_drive_link_public(url)
        mark = "✅" if ok else "❌"
        print(f"{name:<30s} | {mark:<2s} | {msg:<16s} | {url}")
        if not ok:
            inaccessible.append((name, url, msg))

    if inaccessible:
        print("\nStudents with inaccessible links:")
        for name, url, reason in inaccessible:
            print(f"  {name} → {reason}")
    else:
        print("\nAll students’ Drive/Docs links are publicly accessible!")
