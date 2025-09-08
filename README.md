<div align="center">

# 🎉 Welcome Message Automation

<img src="assets/images/logos/allo-dimensional.webp" alt="ALLO Fiber Logo" width="200" style="border-radius: 10px; margin: 20px 0;"/>

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Rich](https://img.shields.io/badge/Rich-Terminal-brightgreen.svg?style=for-the-badge&logo=python&logoColor=white)](https://rich.readthedocs.io/)
[![TextBee](https://img.shields.io/badge/TextBee-API-orange.svg?style=for-the-badge)](https://textbee.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

*A beautiful, feature-rich CLI application for automating customer welcome messages with stunning visual interface*

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🎨 Features](#-features) • [🛠️ Development](#️-development)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎨 **Beautiful Rich UI**

- Stunning panels and tables
- Progress indicators and status bars
- Color-coded output with emojis
- Professional terminal interface

### 🔒 **Security First**

- Masked sensitive credentials
- Secure environment variable handling
- Safe API key management
- Privacy-focused design

</td>
<td width="50%">

### 📱 **Smart Messaging**

- Jinja2 template system
- Customizable message templates
- Real-time message preview
- Multi-provider API support

### 🚀 **Developer Experience**

- Rich logging with timestamps
- Comprehensive error handling
- Clean, maintainable code
- Easy configuration management

</td>
</tr>
</table>

---

## 🏗️ Project Architecture

```html
<div style="font-family: 'Courier New', monospace; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white;">
📦 welcome-message-automation/
├── 🎯 <strong>src/</strong>                      # Core application code
│   ├── 🚀 main.py                    # Enhanced Rich UI application
│   ├── 🌐 api/
│   │   └── 📡 textbee_client.py      # TextBee API integration
│   ├── 👥 models/
│   │   └── 🏠 customer.py            # Customer data models
│   └── 🛠️ utils/
│       ├── ⚙️ config.py              # Configuration management
│       └── 🎨 render.py              # Jinja2 template rendering
├── 📄 templates/                     # Message templates
│   ├── 💌 welcome_message.txt        # Company-specific template
│   └── 🧾 welcome_message_sanitized.txt
├── 🖼️ assets/images/logos/           # Brand assets
├── 📋 requirements.txt               # Python dependencies
└── 🔐 .env                          # Environment variables
</div>
```

---

## 🚀 Quick Start

<details>
<summary><strong>📥 Installation Guide</strong></summary>

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/H2OKing89/welcome-message-automation.git
cd welcome-message-automation
```

### 2️⃣ Set Up Python Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment

Create `.env` file with your TextBee credentials:

```env
TEXTBEE_API=your_api_key_here
TEXTBEE_DEVICE_ID=your_device_id_here
```

</details>

---

## 🎮 Usage

<div align="center">

### Launch the Application

```bash
python src/main.py
```

<img src="https://via.placeholder.com/600x400/667eea/white?text=Rich+CLI+Interface+Preview" alt="CLI Preview" style="border-radius: 10px; margin: 20px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);"/>

*Beautiful Rich-powered interface with tables, panels, and real-time feedback*

</div>

### 🔄 Application Flow

<table>
<tr>
<td align="center" width="25%">
<strong>📝 Input</strong><br/>
<img src="https://via.placeholder.com/100x100/4CAF50/white?text=📝" style="border-radius: 50%;"/><br/>
Enter customer details with guided prompts
</td>
<td align="center" width="25%">
<strong>👀 Preview</strong><br/>
<img src="https://via.placeholder.com/100x100/2196F3/white?text=👀" style="border-radius: 50%;"/><br/>
Review formatted message in beautiful panel
</td>
<td align="center" width="25%">
<strong>🚀 Send</strong><br/>
<img src="https://via.placeholder.com/100x100/FF9800/white?text=🚀" style="border-radius: 50%;"/><br/>
Send via TextBee API with progress tracking
</td>
<td align="center" width="25%">
<strong>✅ Confirm</strong><br/>
<img src="https://via.placeholder.com/100x100/9C27B0/white?text=✅" style="border-radius: 50%;"/><br/>
Get detailed delivery confirmation
</td>
</tr>
</table>

---

## 🎨 Rich UI Components

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white;">
<h3>🎭 Visual Elements</h3>
<ul>
<li>🎨 <strong>Rich Panels</strong> - Bordered content areas</li>
<li>📊 <strong>Data Tables</strong> - Structured information display</li>
<li>⏳ <strong>Progress Bars</strong> - Real-time operation feedback</li>
<li>🌀 <strong>Status Spinners</strong> - Loading indicators</li>
</ul>
</div>

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 10px; color: white;">
<h3>🔒 Security Features</h3>
<ul>
<li>🎭 <strong>Credential Masking</strong> - Hidden passwords</li>
<li>🔐 <strong>Partial SSID Display</strong> - First 4 chars + ****</li>
<li>📝 <strong>Rich Logging</strong> - Timestamped events</li>
<li>🛡️ <strong>Safe Error Handling</strong> - No data leaks</li>
</ul>
</div>

</div>

---

## 📖 Documentation

### 🎨 Template System

<details>
<summary><strong>🔧 Template Configuration</strong></summary>

#### Available Variables

```jinja2
{{ customer_name }}      # Customer's full name
{{ account_number }}     # Account identifier
{{ ssid }}              # Wi-Fi network name
{{ password }}          # Wi-Fi password
{{ company_name }}      # Your company name
{{ support_phone }}     # Support contact
{{ service_type }}      # Service category
{{ technician_name }}   # Tech name
{{ technician_title }}  # Tech position
{{ technician_email }}  # Tech email
```

#### Template Example

```html
<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; border-radius: 5px;">
Welcome to {{ company_name }}, {{ customer_name }}! 🎉

Your {{ service_type }} internet is ready!

📶 Network: {{ ssid }}
🔑 Password: {{ password }}
📞 Support: {{ support_phone }}

{{ technician_name }}
{{ technician_title }}
</div>
```

</details>

### 🔧 Dependencies

<div align="center">

| Package | Version | Purpose |
|---------|---------|---------|
| ![Rich](https://img.shields.io/badge/rich-14.1.0+-brightgreen?style=flat-square) | Latest | Beautiful terminal UI |
| ![HTTPX](https://img.shields.io/badge/httpx-0.28.1+-blue?style=flat-square) | Latest | Modern HTTP client |
| ![Jinja2](https://img.shields.io/badge/jinja2-3.1.6+-red?style=flat-square) | Latest | Template engine |
| ![Python-dotenv](https://img.shields.io/badge/python--dotenv-1.1.1+-yellow?style=flat-square) | Latest | Environment management |

</div>

---

## 🛠️ Development

### 🧪 Running Tests

```bash
# Run security tests
python test_security.py

# Check code quality
pylint src/

# Format code
black src/
```

### 🔍 Debugging

The application includes comprehensive logging:

```python
# Rich logging with timestamps
[18:58:50] INFO Starting welcome message process
[19:01:05] INFO TextBee API client initialized
[19:01:07] INFO Message sent successfully via TextBee API
```

---

## 🤝 Contributing

<div align="center">

We welcome contributions! 🎉

[![Contributors](https://img.shields.io/github/contributors/H2OKing89/welcome-message-automation?style=for-the-badge)](https://github.com/H2OKing89/welcome-message-automation/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/H2OKing89/welcome-message-automation?style=for-the-badge)](https://github.com/H2OKing89/welcome-message-automation/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/H2OKing89/welcome-message-automation?style=for-the-badge)](https://github.com/H2OKing89/welcome-message-automation/pulls)

</div>

### 🎯 How to Contribute

1. 🍴 Fork the repository
2. 🌿 Create a feature branch
3. 💻 Make your changes
4. ✅ Add tests if needed
5. 📝 Update documentation
6. 🚀 Submit a pull request

---

<div align="center">

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ and ☕ by the ALLO Team**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/H2OKing89/welcome-message-automation)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://python.org)
[![Rich](https://img.shields.io/badge/Rich-Terminal-brightgreen?style=for-the-badge)](https://rich.readthedocs.io/)

*Transforming customer onboarding, one message at a time* ✨

</div>
