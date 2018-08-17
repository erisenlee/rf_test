
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import os.path
from common.readConfig import ReadConfig
from common.utils import new_report
from settings import BASE_DIR


class Mail:
    
    @classmethod
    def read_config(cls, section, path=None):
        parser = ReadConfig()
        instance = cls.__new__(cls)
        parser.update_attr(instance, section)
        return instance

    def sendmail(self,subject,sendfile):
        # logger = Log(os.path.basename(__file__))
        
        with open(sendfile, 'rb') as f:
            mail_body = f.read()
        msg = MIMEMultipart()
        att1 = MIMEText(mail_body, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.split(sendfile)[-1])
        content='new'
        att2=MIMEText(content,'plain','utf-8')
        msg.attach(att1)
        msg.set_payload(att2)
        msg['From']=formataddr(["AutoTest",self.sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=self.receiver       #收件人邮箱账号
        msg['Subject'] = Header(subject, 'utf-8')
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.user, self.password)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
            # smtp.quit()
        except Exception as e:
            print('send mail error!', e)
        finally:
            smtp.quit()
 
def mail(subjct):
    m=Mail.read_config('Email')
    subject = 'Test Result'
    report_dir=os.path.join(BASE_DIR,'report')
    filepath = new_report(report_dir)
    m.sendmail(subject,filepath)



if __name__ == '__main__':
    # m = Mail.read_config('Email')
    # print(m.__dict__)
    mail('test result')    
    




