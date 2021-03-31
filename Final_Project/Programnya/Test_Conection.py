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




#Program Bagus
# import smtplib, ssl
# port = 465  # menggunakan SSL agar lebih aman
# smtp_server = "smtp.gmail.com" #server SMTP untuk gmail
# sender_email = "projectsolderku@gmail.com"  # Enter your address
# receiver_email = "dimgusta@gmail.com"  # Enter receiver address



# password = input("Pasword E-mail : ")
# Judul = input("Judul E-mail : ")
# isi = input("Isi Email : ")
# message = """\
# Subject: Hi there

# This message is sent from Python."""



# try:
#     server = smtplib.SMTP_SSL(smtp_server, port)
#     server.ehlo()
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
#     server.close()
#     print ("E-mail Terkirim...")
# except:
#     print ("E-mail Gagal")