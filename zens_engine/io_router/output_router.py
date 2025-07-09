from zens_engine.outputs.email_sender import send_email

def send_output(output_type: str, **kwargs):
    """
    Routes the output based on type.
    Currently supports only 'email'.
    """
    if output_type == "email":
        return send_email(**kwargs)
    else:
        raise ValueError(f"Unsupported output type: {output_type}")