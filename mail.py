import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "veridis95@gmail.com"
SMTP_PASSWORD = "Cf38vg93?!"
EMAIL_FROM = "veridis95@gmail.com"
EMAIL_TO = "julienremant95@gmail.com"
EMAIL_SUBJECT = "Alerte Veridis"
EMAIL_MESSAGE = "Attention, le module de surveillance a detecte une presence !"

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.starttls()
s.login(SMTP_USERNAME, SMTP_PASSWORD)
message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
s.sendmail(EMAIL_FROM, EMAIL_TO, message)
s.quit()