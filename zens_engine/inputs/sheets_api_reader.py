from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

def read_sheet(config):
    """
    Reads a Google Sheet using the official Sheets API.
    Returns a list of dicts (rows) and meta info.

    Expects in config:
    - sheet_url: full Google Sheet URL
    - worksheet_name: optional, default is 'Sheet1'
    - creds_path: path to service account JSON (default 'credentials/google_creds.json')
    """
    sheet_url = config["sheet_url"]
    worksheet_name = config.get("worksheet_name", "Sheet1")
    creds_path = config.get("creds_path", "credentials/google_creds.json")

    # Extract spreadsheet ID from URL
    sheet_id = sheet_url.split("/d/")[1].split("/")[0]

    # Authenticate
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = service_account.Credentials.from_service_account_file(creds_path, scopes=scopes)
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    range_name = f"{worksheet_name}"
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()

    values = result.get("values", [])
    if not values:
        return [], {"sheet_id": sheet_id, "worksheet": worksheet_name}

    # Convert to list of dicts
    headers = values[0]
    records = [dict(zip(headers, row)) for row in values[1:]]

    return records, {
        "sheet_id": sheet_id,
        "worksheet": worksheet_name,
        "row_count": len(records)
    }