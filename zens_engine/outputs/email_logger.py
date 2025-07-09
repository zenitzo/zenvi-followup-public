import csv
import os
from datetime import datetime

def get_log_path(product_slug: str, campaign: str) -> str:
    """Generates a unique log path for a product + campaign."""
    log_dir = os.path.join("zens_engine", "logs", product_slug)
    os.makedirs(log_dir, exist_ok=True)
    return os.path.join(log_dir, f"{campaign}_emails.csv")


def log_sent_email(product_slug, name, email, campaign, status, error_msg=None):
    """
    Logs an email event to the appropriate product + campaign log file.
    """
    log_path = get_log_path(product_slug, campaign)
    file_exists = os.path.isfile(log_path)

    with open(log_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Email", "Campaign", "Timestamp", "Status", "Error"])
        writer.writerow([
            name,
            email,
            campaign,
            datetime.now().isoformat(),
            status,
            error_msg or ""
        ])


def get_previously_emailed(product_slug, campaign):
    """
    Returns a set of emails already sent for the given product + campaign.
    """
    log_path = get_log_path(product_slug, campaign)
    if not os.path.exists(log_path):
        return set()

    sent_emails = set()
    with open(log_path, mode="r", encoding="utf-8") as file:
        try:
            reader = csv.DictReader(file)
            for row in reader:
                if not row:
                    continue
                if row.get("Status") == "Success":
                    sent_emails.add(row.get("Email"))
        except Exception as e:
            print(f"⚠️ Error reading log file '{log_path}': {e}")
    return sent_emails