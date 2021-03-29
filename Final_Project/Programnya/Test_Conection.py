#mode .starttls()
import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # ...send emails
except:
    print 'Something went wrong...'


    

#mode SMTP_SSL() lebih aman
#import smtplib

# try:
#     server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server_ssl.ehlo()   # optional
#     # ...send emails
# except:
#     print 'Something went wrong...'


#https://stackabuse.com/how-to-send-emails-with-gmail-using-python/