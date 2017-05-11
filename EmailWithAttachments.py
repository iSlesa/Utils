import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'YOUR GMAIL ADDRESS'
password = 'YOUR GMAIL PASSWORD'
recipients = ['friend@example.com','honey@honeybee.com']
mail = MIMEMultipart()
mail['Subject'] = 'Email Subject'
mail['To'] = (', ').join(recipients)
mail['From'] = sender
path = '/path/to/the/directory'
os.chdir(path)
attachments = os.listdir(path)
for file in attachments:
	try:
		if not file.startswith('.') and not os.path.isdir(file):
			with open(file, 'rb') as fp:
				msg = MIMEBase('application', "octet-stream")
				msg.set_payload(fp.read())
				encoders.encode_base64(msg)
				msg.add_header('Content-Disposition', 'attachment', filename=file)
				mail.attach(msg)
	except:
		print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
		raise
body = 'Please find attached reports'
mail.attach(MIMEText(body,'plain'))
composed = mail.as_string()
try:
	with smtplib.SMTP('smtp.gmail.com', 587) as s:
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(sender, password)
		s.sendmail(sender, recipients, composed)
		s.close()
	print("Email sent!")
except:
	print("Unable to send the email")
	raise
