# Sample CLI Output

This shows what the enhanced Rich UI looks like when running the application:

```log
╭───────────────────────────────────────────╮
│ 🎉 company Welcome Message Automation 🎉 │
╰───────────────────────────────────────────╯

[18:58:50] INFO     Starting welcome message process
Customer Information
👤 Please enter the customer's name: John Doe
🔢 Please enter the customer's account number: 123456789
📶 Please enter the customer's SSID: Love My WIFI
🔐 Please enter the customer's password: 123456789
📱 Please enter the phone number to send the message to: 555-555-5555

      Customer Information      
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Field           ┃ Value             ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Name            │ John Doe          │
│ Account Number  │ 123456789         │
│ SSID            │ Love My WIFI      │
│ Password        │ ****              │
│ Phone Number    │ 555-555-5555      │
└─────────────────┴───────────────────┘

╭───────────────────────────────────────────── Message Preview ─────────────────────────────────────────────╮
│ Welcome to Company, John Doe! 🎉                                                                         │
│                                                                                                           │
│ We're excited to have you as part of the Company family. Your fast, reliable                              │
│ fiber internet is now up and running. Below are your Wi-Fi details:                                       │
│                                                                                                           │
│ 📶 Wi-Fi Network (SSID): Love My WIFI                                                                    │
│ 🔑 Password: 123456789                                                                                   │
│ 👤 Account Number: 123456789                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Send this message? [y/n]: y
✅ Message sent successfully!
📱 SMS Batch ID: 555555555555555555555555
👥 Recipients: 1
📋 Status: SMS added to queue for processing
```
