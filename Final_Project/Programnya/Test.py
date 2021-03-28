import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# msg = MIMEMultipart()
# msg["Subject"] = "Example"
# msg["From"] = "me@example.com"
# msg["To"] = "malcom@example.com,reynolds@example.com,firefly@example.com"
# msg["Cc"] = "serenity@example.com,inara@example.com"
# body = MIMEText("example email body")
# msg.attach(body)
# smtp = smtplib.SMTP("mailhost.example.com", 25)
# smtp.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
# smtp.quit()


# https://answer-id.com/id/53557096
print(smtplib.help())