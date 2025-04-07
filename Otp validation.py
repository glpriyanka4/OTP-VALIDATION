import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
n=["priyankagangisetty44@gmail.com","glpriyanka540@gmail.com"]
for i in n:
    otp=random.randint(1111,9999)
    body=f"OTP for Verfication if {otp}"
    msg=MIMEMultipart()
    msg["From"]="priyankagangisetty44@gmail.com"
    msg["To"]= i
    msg["Subject"]="OTP FOR Validation"
    msg.attach(MIMEText(body,'plain'))
    
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("priyankagangisetty44@gmail.com","nywo ogyg zmha dkpk")
    server.send_message(msg)
    server.quit()
    
    cotp=int(input("Enter OTP recieved: "))
    if otp==cotp:
        print("OTP Verfication Success")
    else:
        print("Invalid OTP")

