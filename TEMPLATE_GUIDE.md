# Template Usage Guide

## Overview

This guide shows how to use the sanitized template system for the Welcome Message Automation project.

## Available Templates

### 1. Company-Specific Template

- **File**: `templates/welcome_message.txt`
- **Use**: Current ALLO Fiber specific template
- **Variables**: Hard-coded company information

### 2. Sanitized Template

- **File**: `templates/welcome_message_sanitized.txt`
- **Use**: Generic template for any company
- **Variables**: All information is parameterized

## Template Variables

The sanitized template uses these variables:

### Customer Information

- `{{ customer_name }}` - Customer's full name
- `{{ account_number }}` - Customer's account number
- `{{ ssid }}` - Wi-Fi network name
- `{{ password }}` - Wi-Fi password

### Company Information

- `{{ company_name }}` - Your company name
- `{{ support_phone }}` - Support phone number
- `{{ service_type }}` - Type of service (e.g., "Residential")

### Technician Information

- `{{ technician_name }}` - Technician's name
- `{{ technician_title }}` - Technician's job title
- `{{ technician_email }}` - Technician's email

## Example Usage

```python
from utils.render import MessageRenderer

renderer = MessageRenderer()

# Company configuration
company_data = {
    'company_name': 'Your ISP Name',
    'support_phone': '1-800-123-4567',
    'service_type': 'Residential',
    'technician_name': 'John Doe',
    'technician_title': 'Installation Technician',
    'technician_email': 'john.doe@yourisp.com'
}

# Customer data
customer_data = {
    'customer_name': 'Jane Smith',
    'account_number': '987654321',
    'ssid': 'JaneHomeWiFi',
    'password': 'SecurePassword123'
}

# Combine data
template_data = {**customer_data, **company_data}

# Render message
message = renderer.render_template('welcome_message_sanitized.txt', **template_data)
```

## Configuration File

See `config/sample_config.yaml` for complete configuration examples for different companies.

## Benefits of Sanitized Templates

1. **Reusability**: Use the same template for different companies
2. **Security**: No hard-coded company information
3. **Flexibility**: Easy to customize for different scenarios
4. **Maintainability**: Single template file for all variations
