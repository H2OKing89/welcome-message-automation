import os
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt, Confirm
from models.customer import Customer
from api.textbee_client import TextBeeClient

load_dotenv()

def main():
    console = Console()
    console.print("🎉 ALLO Welcome Message Automation 🎉", style="bold green")
    console.print()

    # Gather customer details
    name = Prompt.ask("Please enter the customer's name")
    account_number = Prompt.ask("Please enter the customer's account number")
    ssid = Prompt.ask("Please enter the customer's SSID")
    password = Prompt.ask("Please enter the customer's password")
    
    # Get phone number with verification
    while True:
        phone_number = Prompt.ask("Please enter the phone number to send the message to")
        console.print(f"Phone number entered: [bold]{phone_number}[/bold]")
        
        if Confirm.ask("Is this phone number correct?"):
            break
        console.print("Please re-enter the phone number.")

    # Create a Customer instance
    customer = Customer(name=name, account_number=account_number, ssid=ssid, password=password, phone_number=phone_number)

    # Generate the welcome message
    welcome_message = customer.format_welcome_message()
    
    console.print("\n[bold]Message Preview:[/bold]")
    console.print(welcome_message)
    console.print()
    
    if not Confirm.ask("Send this message?"):
        console.print("Message sending cancelled.", style="yellow")
        return

    # Send the message via TextBee API
    api_key = os.getenv("TEXTBEE_API")
    if not api_key:
        console.print("❌ Error: TEXTBEE_API not found in environment variables", style="bold red")
        return
        
    device_id = os.getenv("TEXTBEE_DEVICE_ID")
    if not device_id:
        console.print("❌ Error: TEXTBEE_DEVICE_ID not found in environment variables", style="bold red")
        console.print("Please add your TextBee device ID to the .env file", style="yellow")
        return
    
    client = TextBeeClient(api_key, device_id)
    
    try:
        success, response = client.send_welcome_message(customer.phone_number, welcome_message)
        
        if success:
            console.print("✅ Message sent successfully!", style="bold green")
            data = response.get('data', {}) if isinstance(response, dict) else {}
            console.print(f"📱 SMS Batch ID: {data.get('smsBatchId', 'N/A')}")
            console.print(f"👥 Recipients: {data.get('recipientCount', 'N/A')}")
            console.print(f"📋 Status: {data.get('message', 'SMS queued for processing')}")
        else:
            console.print("❌ Failed to send message.", style="bold red")
            console.print(f"Error: {response}")
            
    except Exception as e:
        console.print(f"❌ Error sending message: {str(e)}", style="bold red")

if __name__ == "__main__":
    main()