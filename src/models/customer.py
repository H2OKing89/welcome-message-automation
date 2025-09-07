from utils.render import MessageRenderer

class Customer:
    def __init__(self, name, account_number, ssid, password, phone_number):
        self.name = name
        self.account_number = account_number
        self.ssid = ssid
        self.password = password
        self.phone_number = phone_number
        self.renderer = MessageRenderer()

    def format_welcome_message(self):
        """Generate welcome message using Jinja2 template"""
        return self.renderer.render_welcome_message(
            customer_name=self.name,
            ssid=self.ssid,
            password=self.password,
            account_number=self.account_number
        )