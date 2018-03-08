#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Import smtplib for the actual sending function
import smtplib
import sys
from io import BytesIO

# Import the email modules we'll need
from email.mime.text import MIMEText
from config import *
from welcome import welcomeUser
from email.header import Header

def send(name, mail, token):
    activation_link = "https://neect.aauav.pt/register/?token=%s" % token
    fp = open("message.html", 'r')
    name = name.split(" ")[0].capitalize()

    msg = MIMEText(welcomeUser(fp.read(), name, activation_link), "html", "utf-8")
    #fp.close()

    # me == the sender's email address
    # you == the recipient's email address

    you = mail

    msg['Subject'] = Header("Ativação de conta myNEECT", 'utf-8')
    msg['From'] = "mail@example.com"
    msg['To'] = you

    # Send the message via our own SMTP server, but don't include the
    # envelope header.

    
    s = smtplib.SMTP(mail_server, mail_port)
    # for UA students mail server
    s.starttls()
    s.login(mail_login, mail_password)
    s.sendmail("mail@example.com", [you], msg.as_string()) #msg)
    s.quit()