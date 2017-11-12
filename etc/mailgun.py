def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "YOUR_API_KEY"),
        data={"from": "genduts_club@yahoo.com",
              "to": ["genduts_club@yahoo.com"],
              "subject": "Hello API",
              "text": "Testing some Mailgun awesomness!"})

import smtplib
from email.mime.text import MIMEText

def send_simple_message_smtp():
    msg = MIMEText('Testing some Mailgun awesomness')
    msg['Subject'] = "Hello SMTP"
    msg['From']    = "genduts_club@yahoo.com"
    msg['To']      = "genduts_club@yahoo.com"

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('heidy.madia@gmail.com', 'mailgun.com')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

send_simple_message();
