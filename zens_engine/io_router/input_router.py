from zens_engine.inputs import sheet_reader, sheets_api_reader

def read_sheet(config: dict):
    """
    Routes to the correct sheet reader based on config["source_type"].
    Supports 'gspread', 'api', or 'supabase'.
    """
    source_type = config.get("source_type", "gspread")

    if source_type == "gspread":
        return sheet_reader.read_sheet(config)
    elif source_type == "api":
        return sheets_api_reader.read_sheet(config)
    elif source_type == "supabase":
        return supabase_reader.read_sheet(config)
    else:
        raise ValueError(f"Unsupported source_type: {source_type}")