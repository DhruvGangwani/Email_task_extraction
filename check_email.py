# import required libraries
import imaplib
import email
from email.header import decode_header
import webbrowser
import os



def get_emails(user, password, count_email=20):
   # creata a imap object
   imap = imaplib.IMAP4_SSL("imap.gmail.com")

   # login
   result = imap.login(user, password)

   # Use "[Gmail]/Sent Mails" for fetching
   # mails from Sent Mails.
   imap.select('"[Gmail]/All Mail"', readonly = True)

   response, messages = imap.search(None, 'UnSeen')
   messages = messages[0].split()

   # take it from last
   latest = int(messages[-1])

   # take it from start
   oldest = int(messages[0])
   relevant_emails = "@companydomain.com"
   all_emails = list()
   

   for i in range(latest, latest-count_email, -1):
      res, msg = imap.fetch(str(i), "(RFC822)")
      for response in msg:
         if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            date = msg["Date"]
            from_email = msg["From"]
            subject = msg["Subject"]
            if relevant_emails in from_email:
               for part in msg.walk():
                  if part.get_content_type() == "text/plain":
                     body = part.get_payload(decode = True)
                     result = {"Date": date, "From_email": from_email, "subject": subject, "body": body}
                     all_emails.append(result)
   return all_emails


        

