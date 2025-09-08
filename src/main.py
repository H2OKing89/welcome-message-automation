import os
import logging
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from rich.status import Status
from rich.logging import RichHandler
from models.customer import Customer
from api.textbee_client import TextBeeClient

load_dotenv()

# Configure Rich logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
log = logging.getLogger("welcome_message")

def display_customer_info(customer, console):
    """Display customer information in a Rich table"""
    table = Table(title="Customer Information", show_header=True, header_style="bold blue")
    table.add_column("Field", style="cyan", width=15)
    table.add_column("Value", style="green")
    
    table.add_row("Name", customer.name)
    table.add_row("Account Number", customer.account_number)
    table.add_row("SSID", customer.ssid)
    table.add_row("Password", customer.password)
    table.add_row("Phone Number", customer.phone_number)
    
    console.print(table)
    console.print()

def main():
    console = Console()
    
    # Enhanced header with panel
    console.print(Panel.fit("🎉 ALLO Welcome Message Automation 🎉", style="bold green", border_style="green"))
    console.print()
    
    log.info("Starting welcome message process")

    # Gather customer details with enhanced prompts
    console.print("[bold cyan]Customer Information[/bold cyan]")
    name = Prompt.ask("👤 Please enter the customer's name")
    account_number = Prompt.ask("🔢 Please enter the customer's account number")
    ssid = Prompt.ask("📶 Please enter the customer's SSID")
    password = Prompt.ask("🔐 Please enter the customer's password")
    
    # Get phone number with verification
    while True:
        phone_number = Prompt.ask("📱 Please enter the phone number to send the message to")
        console.print(f"Phone number entered: [bold]{phone_number}[/bold]")
        
        if Confirm.ask("Is this phone number correct?"):
            break
        console.print("Please re-enter the phone number.", style="yellow")

    # Create a Customer instance
    customer = Customer(name=name, account_number=account_number, ssid=ssid, password=password, phone_number=phone_number)

    # Display customer information in a table
    display_customer_info(customer, console)

    # Generate the welcome message with status
    with console.status("[bold green]Generating welcome message...", spinner="dots") as status:
        welcome_message = customer.format_welcome_message()
    
    # Display message preview in a panel
    console.print(Panel(welcome_message, title="Message Preview", border_style="green"))
    console.print()
    
    if not Confirm.ask("Send this message?"):
        console.print("Message sending cancelled.", style="yellow")
        log.info("Message sending cancelled by user")
        return

    # Send the message via TextBee API
    api_key = os.getenv("TEXTBEE_API")
    if not api_key:
        console.print("❌ Error: TEXTBEE_API not found in environment variables", style="bold red")
        log.error("API key not found in environment variables")
        return
        
    device_id = os.getenv("TEXTBEE_DEVICE_ID")
    if not device_id:
        console.print("❌ Error: TEXTBEE_DEVICE_ID not found in environment variables", style="bold red")
        console.print("Please add your TextBee device ID to the .env file", style="yellow")
        log.error("Device ID not found in environment variables")
        return
    
    # Enhanced API interaction with status and progress
    try:
        with Status("Connecting to TextBee API...", console=console) as status:
            client = TextBeeClient(api_key, device_id)
            log.info("Connected to TextBee API")
            
            status.update("Sending message...")
            
            with Progress() as progress:
                task = progress.add_task("[green]Sending message...", total=1)
                success, response = client.send_welcome_message(customer.phone_number, welcome_message)
                progress.update(task, advance=1)
        
        if success:
            console.print("✅ Message sent successfully!", style="bold green")
            log.info("Message sent successfully")
            
            # Handle response data more safely
            if isinstance(response, dict):
                data = response.get('data', {})
                if isinstance(data, dict):
                    console.print(f"📱 SMS Batch ID: {data.get('smsBatchId', 'N/A')}")
                    console.print(f"👥 Recipients: {data.get('recipientCount', 'N/A')}")
                    console.print(f"📋 Status: {data.get('message', 'SMS queued for processing')}")
                else:
                    console.print(f"📋 Response: {response}")
            else:
                console.print(f"📋 Response: {response}")
        else:
            console.print("❌ Failed to send message.", style="bold red")
            console.print(f"Error: {response}", style="red")
            log.error(f"Failed to send message: {response}")
            
    except Exception as e:
        console.print(f"❌ Error sending message: {str(e)}", style="bold red")
        log.error(f"Error sending message: {str(e)}")

if __name__ == "__main__":
    main()