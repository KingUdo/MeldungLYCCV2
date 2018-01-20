from email.mime.text import MIMEText
import smtplib
from flask import *

sender = 'onlinemeldung@lycc.de'
smtpserver = 'smtp.strato.de'
smtpusername = 'onlinemeldung@lycc.de'
smtppassword = 'onlinemeldung_LYCC1!'
usetls = True
### Create and Send EMAIL ###


def email_Seascape(Meldung):
	global sender, smtpserver, smtppassword, smtpusername, usetls
	msg = MIMEText(render_template('Meldung_Print_Seascape.html', Meldung = Meldung), 'html')
	msg['From'] = sender
	msg['To'] = Meldung["Email"]
	msg['Subject'] = 'Meldung für ' + Meldung["Veranstaltung"]

	server = smtplib.SMTP(smtpserver)
	if usetls:
		server.starttls()

	if smtpusername and smtppassword:
		server.login(smtpusername,smtppassword)
	#Send to Melder	
	server.sendmail(sender,Meldung["Email"],msg.as_string())

	#Send to Sportwart
	server.sendmail(Meldung["Email"],"sportwart@lycc.de",msg.as_string())

	server.quit()

def email(Meldung):
	global sender, smtpserver, smtppassword, smtpusername, usetls
	msg = MIMEText(render_template('Meldung_Print.html', Meldung = Meldung), 'html')
	msg['From'] = sender
	msg['To'] = Meldung["Email"]
	msg['Subject'] = 'Meldung für ' + Meldung["Veranstaltung"]

	server = smtplib.SMTP(smtpserver)
	if usetls:
		server.starttls()

	if smtpusername and smtppassword:
		server.login(smtpusername,smtppassword)

	server.sendmail(sender,Meldung["Email"],msg.as_string())

	#Send to Sportwart
	server.sendmail(Meldung["Email"],"sportwart@lycc.de",msg.as_string())

	server.quit()
