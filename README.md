# OTP Verification System using SMTP

This project demonstrates a simple OTP (One-Time Password) verification system using Python. The script sends OTPs to a list of email addresses and asks the user to verify the OTP they received by entering it in the terminal.

## Features
- Sends OTPs via email to a list of recipients.
- User input required to verify OTP.
- The script checks the validity of the OTP entered by the user.
  
## Requirements
- Python 3.x
- Required Python libraries: `smtplib`, `random`, `email.mime.multipart`, `email.mime.text`

### Libraries Installation:
You may need to install the required libraries if they are not installed in your environment. Use `pip` to install them:

```bash
pip install smtplib
