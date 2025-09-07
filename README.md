# Welcome Message Automation

This project automates the process of sending welcome messages to customers using the TextBee API. It is built with Python and utilizes the `httpx` library for making API calls and `rich` for output formatting.

## Project Structure

```
welcome-message-automation/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── textbee_client.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── customer.py
│   └── utils/
│       ├── __init__.py
│       └── render.py
├── templates/
│   ├── welcome_message.txt
│   └── welcome_message_sanitized.txt
├── config/
│   └── sample_config.yaml
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd welcome-message-automation
   ```

2. **Create a virtual environment:**
   ```
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up the environment variables:**
   Create a `.env` file in the root directory and add your TextBee API credentials:
   ```
   TEXTBEE_API=your_api_key_here
   TEXTBEE_DEVICE_ID=your_device_id_here
   ```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

Follow the prompts to enter customer details, and the script will send a welcome message via the TextBee API.

## Templates and Configuration

### Template System

The project uses Jinja2 templates for flexible message customization. Templates are stored in the `templates/` directory:

- **`welcome_message.txt`**: Current company-specific template
- **`welcome_message_sanitized.txt`**: Generic template with placeholders for any company

### Template Variables

Available variables in templates:
- `{{ customer_name }}` - Customer's full name
- `{{ account_number }}` - Customer's account number
- `{{ ssid }}` - Wi-Fi network name
- `{{ password }}` - Wi-Fi password
- `{{ company_name }}` - Your company name
- `{{ support_phone }}` - Support phone number
- `{{ service_type }}` - Type of service (e.g., "Residential")
- `{{ technician_name }}` - Technician's name
- `{{ technician_title }}` - Technician's job title
- `{{ technician_email }}` - Technician's email

### Sample Configuration

See `config/sample_config.yaml` for examples of how to configure the system for different companies. This file shows sanitized configurations that can be adapted for any internet service provider.

## Dependencies

- `httpx`: For making HTTP requests to the TextBee API
- `rich`: For enhanced output formatting in the terminal
- `python-dotenv`: For loading environment variables
- `jinja2`: For template rendering

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.