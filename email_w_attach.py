# gmail login: http://stackoverflow.com/questions/10147455/trying-to-send-email-gmail-as-mail-provider-using-python
import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import sys

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

send_from = USERNAME
send_to = [USERNAME]
text = "Your simulation results are attached as an image."
files = ['simulation.png']
subject = "Simulation results"
server="smtp.gmail.com:587"

assert type(send_to)==list
assert type(files)==list

msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = COMMASPACE.join(send_to)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = subject

msg.attach( MIMEText(text) )

for f in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(f,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)

smtp = smtplib.SMTP(server)
smtp.ehlo()
smtp.starttls()
smtp.login(USERNAME, PASSWORD)
smtp.sendmail(send_from, send_to, msg.as_string())
smtp.close()

