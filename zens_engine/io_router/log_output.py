from zens_engine.outputs.email_logger import log_sent_email

def log_output(output_type, name, email, status, campaign, product_slug, error_msg=""):
    """
    Routes logging based on output type. Currently only supports email.
    """
    if output_type == "email":
        log_sent_email(product_slug, name, email, campaign, status, error_msg)
    else:
        print(f"[log_output] ⚠️ Unsupported output type: {output_type}")