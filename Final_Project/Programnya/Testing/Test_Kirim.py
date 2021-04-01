import smtplib, ssl

port = 465  # menggunakan SSL agar lebih aman
smtp_server = "smtp.gmail.com" #server SMTP untuk gmail
sender_email = "projectsolderku@gmail.com"  # Enter your address
receiver_email = "dimgusta@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

try:
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.close()
    print ("Email sent!")
except:
    print ("Something went wrong...")