from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

def update_sheet_status(config, email, new_status):
    """
    Updates the row in the sheet that matches the given email with new_status
    in the column defined by config["status_column"].

    Requires:
    - config["sheet_url"]
    - config["worksheet_name"] (optional, default = "Sheet1")
    - config["creds_path"] (optional, default = credentials/google_creds.json)
    - config["email_field"]
    - config["status_column"]
    """
    sheet_url = config["sheet_url"]
    worksheet_name = config.get("worksheet_name", "Sheet1")
    creds_path = config.get("creds_path", "credentials/google_creds.json")
    email_field = config["email_field"]
    status_column = config["status_column"]

    sheet_id = sheet_url.split("/d/")[1].split("/")[0]

    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = service_account.Credentials.from_service_account_file(creds_path, scopes=scopes)
    service = build("sheets", "v4", credentials=creds)

    # Read current sheet values
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=worksheet_name
    ).execute()

    values = result.get("values", [])
    if not values:
        return False

    headers = values[0]
    email_index = headers.index(email_field)
    status_index = headers.index(status_column)

    for i, row in enumerate(values[1:], start=2):  # start=2 because row 1 = header
        if len(row) > email_index and row[email_index].strip().lower() == email.strip().lower():
            # Pad row to match column count if needed
            while len(row) <= status_index:
                row.append("")
            row[status_index] = new_status

            update_range = f"{worksheet_name}!A{i}:{chr(65 + len(headers) - 1)}{i}"
            service.spreadsheets().values().update(
                spreadsheetId=sheet_id,
                range=update_range,
                valueInputOption="RAW",
                body={"values": [row]}
            ).execute()
            return True

    return False