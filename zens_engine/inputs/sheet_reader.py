import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_gspread_client():
    """
    Authenticates using the service account credentials and returns a gspread client.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials/google_creds.json", scope)
    return gspread.authorize(creds)

def read_sheet(config: dict):
    """
    Reads data from a Google Sheet using gspread and returns:
    - a list of row dictionaries
    - a metadata dictionary

    Args:
        config (dict): contains 'sheet_url' and optionally 'worksheet_name'

    Returns:
        tuple: (records, meta)
    """
    sheet_url = config["sheet_url"]
    worksheet_name = config.get("worksheet_name", "Sheet1")

    client = get_gspread_client()
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.worksheet(worksheet_name)
    records = worksheet.get_all_records()

    meta = {
        "worksheet": worksheet,
        "sheet_title": sheet.title,
        "worksheet_title": worksheet.title
    }

    return records, meta