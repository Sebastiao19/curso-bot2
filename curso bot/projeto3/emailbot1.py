from cgitb import text
import smtplib  
# simple mail transfor protocolo 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "bastiaofilho57@gmail.com"
toaddr = "anny1904mcv@gmail.com"

msg = MIMEMultipart()


msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = 'Venha connhecer a nossa escola!!!'

body = """ Inauguração da nossa escola de programação, hoje a noite as 20 hrs."""

msg.attach(MIMEText(body, 'plain'))

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, 'Miguel1906@#$.')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()



