from data_fetcher import fetch_data

try:
    cs_file = fetch_data("downloadCS")
    cdrs_file = fetch_data("downloadCDRs")
    print(f"Files downloaded: {cs_file}, {cdrs_file}")
except Exception as e:
    print(f"Error: {e}")