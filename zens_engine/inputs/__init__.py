from .sheet_reader import read_sheet as read_sheet_gspread
from .sheets_api_reader import read_sheet as read_sheet_api

def read_sheet(config):
    source_type = config.get("source_type", "gspread").lower()

    if source_type == "api":
        return read_sheet_api(config)
    elif source_type == "gspread":
        return read_sheet_gspread(config)
    else:
        raise ValueError(f"Unsupported source_type: {source_type}")