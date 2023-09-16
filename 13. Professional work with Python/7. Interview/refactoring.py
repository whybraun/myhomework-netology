import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailMsng:
    def __init__(self, gmail_smtp, gmail_imap, username, password):
        self.gmail_smtp = 'smtp.gmail.com'
        self.gmail_imap = 'imap.gmail.com'
        self.username = username
        self.password = password

    
    def send_email(self, subject, recipients, message):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.username, self.password)
        ms.sendmail(self.username, recipients, msg.as_string())
        ms.quit

    def recieve_mail(self, header=None):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.username, self.password)
        mail.list()
        mail.select('Inbox')
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message
    

if __name__ == '__main__':
    gmail_client = EmailMsng('smtp.gmail.com', 'imap.gmail.com', 'login@gmail.com', 'qwerty')

    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    gmail_client.send_email(subject, recipients, message)

    recieve_mail = gmail_client.recieve_mail()

