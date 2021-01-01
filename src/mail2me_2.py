import smtplib
from email.header import Header
from email.mime.text import MIMEText

sender = "guoyinzhi@foxmail.com"
receivers = ['775741842@qq.com']

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("Clay_Guo")
message['to'] = Header("郭寅之", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
