# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Thank you" #pesan yang mau dikirim
 
# setup the parameters of the message
password = "Bismilah2021"
msg['From'] = "projectsolderku@gmail.com"
msg['To'] = "dimgusta@gmail.com"
msg['Subject'] = "Apa ini"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("successfully sent email")


#Catatan Penting :
#https://realpython.com/python-send-email/
# di refrensi diatas dikatakan :
# I’ll show you how to use SMTP_SSL() first, as it instantiates a connection 
# that is secure from the outset and is slightly more concise than the .starttls() alternative. 
# Keep in mind that Gmail requires that you connect to port 465 if using SMTP_SSL(), 
# and to port 587 when using .starttls().
#https://www.mailgun.com/blog/which-smtp-port-understanding-ports-25-465-587/

#Cek Server Gmail :
#https://stackabuse.com/how-to-send-emails-with-gmail-using-python/


#Refrensi Code dan Setting Email Agar Bisa Mengirim Email dengan Python:
#https://www.niagahoster.co.id/blog/cara-setting-smtp-gmail-gratis/
#https://www.hostinger.co.id/tutorial/apa-itu-ssl#:~:text=TLS%20adalah%20Transport%20Layer%20Security,antara%20website%20dan%20web%20browser.
#https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975
#https://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/

#metode SSL
#https://medium.com/@veronicayolandaa/sending-emails-using-python-bahasa-aa4cc6b20a7e