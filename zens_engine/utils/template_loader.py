import re

def load_template(template_path: str, variables: dict) -> str:
    """
    Loads an HTML email template and injects variables like {{name}}.
    Also supports optional {% if some_var %}...{% endif %} blocks.
    """

    with open(template_path, "r", encoding="utf-8") as file:
        html = file.read()

    # Handle optional {% if some_var %} blocks
    def handle_conditionals(template: str) -> str:
        pattern = r"{% if (.*?) %}(.*?){% endif %}"
        matches = re.findall(pattern, template, re.DOTALL)
        for var, block in matches:
            var = var.strip()
            if var in variables and variables[var]:
                template = template.replace(f"{{% if {var} %}}{block}{{% endif %}}", block)
            else:
                template = template.replace(f"{{% if {var} %}}{block}{{% endif %}}", "")
        return template

    html = handle_conditionals(html)

    # Replace {{variable}} tags
    for key, value in variables.items():
        html = html.replace(f"{{{{{key}}}}}", str(value))

    return html