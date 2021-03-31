import smtplib, ssl                                              #modul SMTLIB mode SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
port = 465                                                       #port untuk mode SSL 465  | TLS 587
smtp_server = "smtp.gmail.com"                                   #server SMTP untusk gmail
sender_email = "projectsolderku@gmail.com"                       #Email pengirim
receiver_email = ["dimgusta@gmail.com"]                          #email penerima bisa menggunakan list / string tapi beda cara aksesnya

msg = MIMEMultipart()
msg['From'] = sender_email                          
if (len(receiver_email) > 1) :                                  #mendeteksi jumlah email penerima di dalam list jika ada lebih dari satu maka 
    msg['To'] = ', '.join(receiver_email)                       #elemen email di dalam list akan digabung dengan separator , "dede@gmail.com , dimgusta@wkwkw.com"
else :
    msg['To'] = receiver_email[0]                               #jika elemen list hanya satu maka akan mengirim ke indeks 0 aja

#msg['To'] = receiver_email                                     #contoh deklarasi jika menggunakan satu string aja 
#msg["Cc"] = "  "                                               #optional jika ada email yang mau di CC

msg['Subject'] = "JUDUL PESAN DUA DUNIA"
body = "ini adalah pesan dari python"
msg.attach(MIMEText(body, 'plain'))

password = input("Pasword E-mail : ")

try:
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.ehlo()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.close()
    print ("E-mail Terkirim...")
except:
    print ("E-mail Gagal")

