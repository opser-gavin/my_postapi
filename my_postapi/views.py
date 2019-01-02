from django.http import HttpResponse

import json,smtplib,sys
from email.mime.text import MIMEText

def sendEmail(request):
    if request.method == 'POST':
        recv_data = json.loads(request.body)
        print(recv_data)
        subject = recv_data['data'][0]['subject']
        context = recv_data['data'][1]['context']
        tomail = recv_data['data'][2]['tomail']

        mail_host = 'smtp.139.com'
        mail_user = 'gavin.xinali'
        mail_pass = 'haohaizi@qusiba^'
        mail_postfix = '139.com'

        me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
        msg = MIMEText(context, _charset="utf-8")
        msg['Subject'] = subject
        msg['From'] = me
        msg['to'] = tomail
        try:
            s = smtplib.SMTP()
            s.connect(mail_host)
            s.login(mail_user,mail_pass)
            s.sendmail(me,tomail,msg.as_string())
            s.close()
            return HttpResponse('sendmail ok !')
        except:
            return HttpResponse('sendmail failed !')

    else:
        return HttpResponse('hhhhhh')


def sendWexin(request):
    pass

def sendDingding(request):
    pass

