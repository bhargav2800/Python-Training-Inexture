import smtplib

def email_module(recipient_mail,message):
	try:
		server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		my_mail = "181200107026@asoit.edu.in"
		server.login(my_mail, "28001398bhargav")
		message = str(message)
		server.sendmail(my_mail,recipient_mail,message)
		return True
	except Exception:
		return False