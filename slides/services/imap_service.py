import datetime
import email
import imaplib

class ImapService():
    def __init__(self, imap, username, password):
        self.imap = imap
        self.username = username
        self.password = password

    def connect(self):
        mail = imaplib.IMAP4(self.imap)	
        mail.login(self.username, self.password)
        mail.select("INBOX", readonly=True)
        return mail


    def getCountUnread(self):
        mail = self.connect();
        return len(mail.search(None, 'UnSeen')[1][0].split())

    def getLastUnread(self):
        mail = self.connect()
        emails = mail.search(None, 'UnSeen')[1][0].split()
        if len(emails) == 0:
            return {
                "sender": "",
                "sender_email": "",
                "subject": "No unread emails."
            }

        latest_email_uid = int(emails[-1])
        result, data = mail.fetch(str(latest_email_uid), '(BODY.PEEK[])')
        raw_email = data[0][1]

        email_message = email.message_from_bytes(raw_email);

        fromEmail = email.utils.parseaddr(email_message['From']);
        return {
            "sender": fromEmail[0],
            "sender_email": fromEmail[1],
            "subject": email_message['Subject']
        }
        