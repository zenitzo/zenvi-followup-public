def handle_email_error(name, email, campaign, error, product_slug, logger, sheet_updater, config):
    """
    Centralized error handler for email failures.
    Logs the error, updates the sheet, and prints the message.

    Args:
        name (str): Recipient name
        email (str): Recipient email
        campaign (str): Campaign name
        error (Exception): The error that occurred
        product_slug (str): Product folder name for logging
        logger (func): Reference to log_sent_email()
        sheet_updater (func): Reference to update_sheet_status()
        config (dict): Loaded YAML config
    """
    error_message = str(error)
    print(f"❌ Failed to send to {email}: {error_message}")

    logger(product_slug, name, email, campaign, "Failed", error_message)
    sheet_updater(config, email, "Failed")