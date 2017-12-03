import os
import smtplib
import unittest
# HTMLTestRunner.py 是基于 unittest 框架的一个扩展，（第三方公开的比较常用的文件，可以从网上下载），这个可支持 python3 的
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    # 用二进制方式写的 html，那么就要用二进制方法来读取
    f=open(path,'rb')
    mail_body=f.read()  #读取html报告的内容作为邮件的正文
    f.close()
    #先读取再转换
    #要想发邮件，我们要把二进制内容转换成  MIME 格式：多用途互联网邮件扩展
    # multipurse多用途，多目的；Internet互联网；Mail邮件；Extension扩展
    # MIME 是对邮件协议的一个扩展，使邮件不仅支持文本格式，还支持多媒体多种格式，例如图片、音频、二进制等文件
    msg=MIMEText(mail_body,'html','utf-8')  #将html报告的内容转换成MIME格式的文件
    #上面是邮件的正文，但是对于邮件来讲，出来正文，还需要有主题，发件人，收件人
    # msg['Subject']=Header()
    msg['Subject']=Header("自动化测试报告","utf-8")    #邮件主题
    #msg是字典类型，字典类似于数组，区别是 字典是无序的
    #如果想用客户端软件或者自己写代码登录邮箱，很多类型的邮箱都需要单独设置一个客户端授权码：
    #因为现在我没有设置授权码，所以发件箱现在用老师的，收件箱地址用自己的
    msg['From']='bwftest126@126.com'  #发件箱地址
    msg['to']='dy061951@126.com'  #收件箱

    #现在邮件内容已经准备好，开始发送邮件
    #发邮件的手动步骤：
    #1.打开邮箱登录页面，即连接邮箱服务器才能够登录邮箱
    #要想连接服务器，首先必须清楚网络传输协议
    # http，https，ftp，socket
    #除上述协议外，发送邮件的协议一般有三种，要先查看邮箱是支持哪种协议
    #126邮箱支持这些协议：pop3，smtp，imap
    #我们要选一种传输协议，用来发送邮件，smtp(单邮件传输协议)
    #首先导入smtplib的协议代码库
    smtp=smtplib.SMTP()  #实例化一个SMTP的对象
    smtp.connect("smtp.126.com")  #连接126邮箱的服务器名字地址

    #2.输入用户名密码登录邮箱
    smtp.login("bwftest126@126.com","abc123asd654")   #参数为：邮箱用户名的地址 和 密码

    #3.发送邮件
    #注意：如果是用smtp.sendmail()方法时，参数中的 msg 是 MIME 类型的，所以要转换成string的格式
    #sendmail()方法较高级，可多种设置，sendmessage设置比较单一，但两种方法发送邮件均好使
    smtp.send_message(msg, from_addr=msg['From'], to_addrs=msg['to'])
    # smtp.sendmail('bwftest126@126.com','245405102@qq.com',msg.as_string())
    #4.退出邮箱
    smtp.quit()
    print("邮件已发送成功")

if __name__ == '__main__':
    # 时间戳
    # str是string，f是format格式；strftime()通过这个方法可以定义时间的格式
    #
    now=time.strftime("%Y-%m-%d_%H-%M-%S")

    suite=unittest.defaultTestLoader.discover("./day_5","*Test.py")
    #unittest.TextTestRunner().run(suite)  #文本的测试用例加载器，返回的是以文本形式展示的结果
    #现在用 html 的测试用例运行器 最终会生成一个 html 格式的测试报告
    base_path=os.path.dirname(__file__) #代表查找当前此文件的路径
    path=base_path + "/report/report"+ now +".html"
    file=open(path,'wb')  #写入二进制
    # stream=sys.stdout 流为系统标准输出（二进制文件）  ,description=正文内容
    HTMLTestRunner(stream=file, title="海盗商城的测试报告", description="ceshihuanjing :Window Server 2008 + Chrome").run(suite)
    file.close()

    #这时生成的测试报告只显示类名和方法，只能给专业的人士看，我们应该把相关的手动测试用例标题加到报告中去
    #自动化测试用例是从手工测试用例中挑取出来的，手工用例怎么写就怎么编写代码，所以代码里应该要体现出手工测试用例的标题

    #新的测试报告会覆盖原来的测试报告，如果想把所有的测试报告保存起来怎么做？
    #解决：可以加一个时间戳 ，它会按照当前时间计算出一个数字，把数字放在上面作为文件名的一部分，那么久避免了文件名重复的问题

    #html测试报告已经生成，当测试用例全部执行完成，应该生成一封提醒邮件，通知发送所有关系测试结果的人
    #要把html报告作为邮件正文发送邮件
    send_mail(path)   #参数为 html 报告的路径
