import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    print 'Done...'
except:
    print 'Something went wrong...'

import smtplib

# try:
#     server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server_ssl.ehlo()   # optional
#     # ...send emails
# except:
#     print 'Something went wrong...'


#https://realpython.com/python-send-email/
#https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
#https://www.hostinger.co.id/tutorial/apa-itu-ssl#:~:text=TLS%20adalah%20Transport%20Layer%20Security,antara%20website%20dan%20web%20browser.