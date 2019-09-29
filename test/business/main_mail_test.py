"""
Test routine
"""
import src.business.main_mail as mail
import pytest

class TestMailPrepare:

    def send_mail_test(self):
        subject = 'TESTE DA ROTINA'
        context = 'Parece que o e-mail foi enviado, certo?'
        check = mail.MailPrepare()
        log = check.send_mail(subject, context)
        assert log == 0

if __name__ == "__main__":
    log = TestMailPrepare()
    log.send_mail_test()
