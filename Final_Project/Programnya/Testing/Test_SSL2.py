import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "projectsolderku@gmail.com"
toaddr = "dimgusta@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "JUDUL PESAN DENGAN LAMPIRAN"
 
body = "ISI PESAN"
 
msg.attach(MIMEText(body, 'plain'))
# Lampiran, sesuaikan nama filename dengan nama di attachment
try :
    filename = "Nama_siswa.txt"
    attachment = open("Nama_siswa.txt", "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    msg.attach(part)
except:
    print("File tidak ditemukan ")

 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Bismilah2021")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()