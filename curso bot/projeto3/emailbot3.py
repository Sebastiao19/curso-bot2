from cgitb import text
from fileinput import filename
from json import encoder
import smtplib  
# simple mail transfor protocolo 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "bastiaofilho57@gmail.com"
toaddr = "sabastiaorf31@gmail.com"

msg = MIMEMultipart()


msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Assista agora!!!"

html = """
<html>
    <body>
        <p>oi,<br>
        como vai você?!<br>
        <a href="https://www.youtube.com/watch?v=ojSvfWm5dl8&t=56s">clique aqui!!!</a>
        para assistir a aula


        </p>
    </body>
<html>
"""
part1 = MIMEText(html, "html")
msg.attach(part1)
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, 'Miguel1906@#$')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
