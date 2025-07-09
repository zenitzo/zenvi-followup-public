REQUIRED_KEYS_COMMON = [
    "client_name",
    "campaign",
    "source_type",
    "trigger_column",
    "trigger_value",
    "email_field",
    "status_column",
    "subject_line",
    "email_template"
]

REQUIRED_KEYS_BY_SOURCE = {
    "gspread": ["sheet_url", "name_field"],
    "supabase": ["supabase_url", "supabase_key", "table_name"]
}

def validate_config(config: dict):
    source_type = config.get("source_type", "gspread")
    required_keys = REQUIRED_KEYS_COMMON + REQUIRED_KEYS_BY_SOURCE.get(source_type, [])

    missing = [key for key in required_keys if key not in config]
    if missing:
        raise ValueError(f"❌ Missing required config keys: {', '.join(missing)}")