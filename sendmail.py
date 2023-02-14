from distutils import filelist
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def getfilename(path):
    f_list = os.listdir(path)
    for i in f_list:
        if os.path.splitext(i)[1] == '.png':
            return i 
        else:
            return False

def sendmail(file):
    mail_host = 'smtp.qq.com'
    mail_user = '4897xxx@qq.com'
    mail_pass = 'xxxxx'
    sender = '4897xxx@qq.com'
    receivers = ['4897xxx@qq.com']
    #设置eamil信息
    #添加一个MIMEmultipart类，处理正文及附件
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receivers[0]
    message['Subject'] = 'dell_登录失败'

    with open(file,'rb')as fp:
        picture = MIMEImage(fp.read())
        #与txt文件设置相似
        picture['Content-Type'] = 'application/octet-stream'
        picture['Content-Disposition'] = 'attachment;filename="'+file+'"'
    #将内容附加到邮件主体中
    message.attach(picture)

    #登录并发送
    try:
        #smtpObj = smtplib.SMTP()
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(
            sender,receivers,message.as_string())
        print('success')
        os.remove(file)
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print('error',e)

path = 'D:\\code\\python\\video\\'
filename = getfilename(path)
if filename:
    sendmail(path+filename)
