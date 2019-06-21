"""
Prepare and send e-mail
"""

import smtplib, re
import configparser
from email.mime.text import MIMEText
import os


class MailPrepare:

    def __init__(self):
        path = os.path.abspath(os.path.join('.', os.pardir))
        log_file = (os.path.dirname(__file__))
        log_file = re.sub('/business', '', log_file)
        print(log_file)
        for root, dirs, files in os.walk(log_file, topdown=False):
            for name in files:
                if name == 'config.ini':
                    config = configparser.ConfigParser()
                    config.read(os.path.join(root, name))
                    self.frommail = config['DEFAULT']['FROM_MAIL']
                    self.tomail = config['DEFAULT']['TO_MAIL']
                    self.password = config['DEFAULT']['PASSWORD']

    def send_mail(self, subject_info, message_info):
        """
        Send an email when is allowed to send info
        :return:
        """

        msg = MIMEText(message_info, 'plain')
        msg['Subject'] = subject_info
        msg['From'] = self.frommail
        msg['To'] = self.tomail

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(
            user=self.frommail,
            password=self.password
        )
        try:
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            flag = 0
        except:
            flag = 1
        server.quit()

        return flag

if __name__ == "__main__":
    col = MailPrepare()
    print(col.password)
    print(col.frommail)
    col.send_mail('TEST', 'vamos testar')