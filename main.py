import smtplib
from body import emailbody
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import pandas as pd

e = pd.read_excel("data.xlsx")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sr1498@srmist.edu.in','password')

body = emailbody
subject = "Gen-Y Webinar Certificate of Participation"
fromaddr='sr1498@srmist.edu.in'

for index, row in e.iterrows():
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    filename = row["image"]
    toaddr = row["emails"]
    msg.attach(MIMEImage(open(filename, 'rb').read()))
    server.sendmail(fromaddr, toaddr, msg.as_string())
    print(str(index+1)+"sent")

print(str(index+1)+" Emails sent successfully")

server.quit()
