import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class MessageRenderer:
    def __init__(self, template_dir="templates"):
        """Initialize the Jinja2 template renderer"""
        # Get the project root directory (go up two levels from src/utils/)
        project_root = Path(__file__).parent.parent.parent
        template_path = project_root / template_dir
        
        # Create Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(template_path)),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def render_welcome_message(self, customer_name, ssid, password, account_number):
        """Render the welcome message template with customer data"""
        template = self.env.get_template('welcome_message.txt')
        
        return template.render(
            customer_name=customer_name,
            ssid=ssid,
            password=password,
            account_number=account_number
        )
    
    def render_template(self, template_name, **kwargs):
        """Generic method to render any template with provided data"""
        template = self.env.get_template(template_name)
        return template.render(**kwargs)
    
    def list_templates(self):
        """List all available templates"""
        return self.env.list_templates()
