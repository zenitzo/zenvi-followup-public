import os
import yaml
import argparse
from dotenv import load_dotenv

from zens_engine.io_router.input_router import read_sheet
from zens_engine.io_router.output_router import send_output
from zens_engine.io_router.log_output import log_output
from zens_engine.outputs.email_logger import get_previously_emailed
from zens_engine.outputs.sheets_writer import update_sheet_status
from zens_engine.utils.template_loader import load_template
from zens_engine.utils.error_handler import handle_email_error
from zens_engine.utils.config_validator import validate_config

# Load environment variables
load_dotenv()
email_username = os.getenv("EMAIL_USERNAME")
email_password = os.getenv("EMAIL_PASSWORD")

# Parse CLI argument for config name
parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True, help="Name of the client config YAML (without .yaml)")
args = parser.parse_args()

# Build path to client config (from root: client_configs/followup/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
config_path = os.path.join(BASE_DIR, "client_configs", "followup", args.config)
if not config_path.endswith(".yaml"):
    config_path += ".yaml"

# Load config
with open(config_path, "r") as file:
    config = yaml.safe_load(file)

# ✅ Validate required config fields
try:
    validate_config(config)
except ValueError as e:
    print(str(e))
    exit(1)

# Read data
print("Reading sheet data...")
records, meta = read_sheet(config)

trigger_column = config["trigger_column"]
trigger_value = config["trigger_value"]
campaign = config["campaign"]
product_slug = "followup"
status_column = config["status_column"]

template_path = os.path.join(os.path.dirname(__file__), "../../templates/followup/email_template.html")

previously_sent = get_previously_emailed(product_slug, campaign)

print(f"\nProcessing leads where {trigger_column} == '{trigger_value}' for campaign '{campaign}':\n")
for i, row in enumerate(records, 1):
    if row.get(trigger_column) == trigger_value:
        name = row.get(config["name_field"])
        to_email = row.get(config["email_field"])

        # ✅ Skip if already marked as emailed
        current_status = row.get(status_column, "").strip().lower()
        if current_status == "emailed":
            print(f"⏭️ Skipping {to_email} (already marked as 'Emailed' in sheet)")
            continue

        # ✅ Skip if already logged as sent
        if to_email in previously_sent:
            print(f"⏭️ Skipping {to_email} (already logged for '{campaign}')")
            continue

        subject = config.get("subject_line", "").replace("{{name}}", name)
        message_body = config["email_template"].replace("{{name}}", name)

        html_message = load_template(template_path, {
            "name": name,
            "company": config.get("client_name", "Your Company"),
            "message_body": message_body,
            "cta_label": config.get("cta_label", ""),
            "cta_link": config.get("cta_link", ""),
            "logo_url": config.get("logo_url", "")
        })

        try:
            send_output(
                output_type="email",
                to_email=to_email,
                subject=subject,
                body=html_message,
                from_email=email_username,
                password=email_password
            )
            print(f"✅ Sent follow-up email to {to_email}")
            log_output("email", name, to_email, "Success", campaign, product_slug)
            update_sheet_status(config, to_email, "Emailed")
        except Exception as e:
            print(f"❌ Failed to send to {to_email}: {str(e)}")
            log_output("email", name, to_email, "Failed", campaign, product_slug, str(e))
            update_sheet_status(config, to_email, "Failed")