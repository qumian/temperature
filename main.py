# -*- coding: utf-8 -*-
import lxml.etree as etree
import requests
import sys
import time
import io
import random

# 有饭邮件通知提醒程序
def send_email(msg_to, text_content):
    url = "http://113.31.114.67/qq/index.php?"
    datata = {"uid":msg_to,"msg":text_content}
    resr = requests.post(url=url,data=datata)

def geturl(name, account, password, qq):
    url = "https://cas.bzpt.edu.cn/login?service=https://xg.bzpt.edu.cn:2020/cas"
    headers = {
    'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
    r = requests.get(url, headers,verify=False)
    r.encoding = "utf-8"
#    print(r.status_code)# 1).将html内容转化成xpath可以解析 / 匹配的格式;
    html = r.text# print(type(html))# 生成选择器对象
    selector = etree.HTML(html)# 2).# //: 对全文进行扫描
# ////*[@id="fm1"]/div[2]/input[2]
# //div[@id="content"]
    str = selector.xpath('//input[@name="execution"]/@value')[0]# print(str)# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf8')
# 改变标准输出的默认编码# 登录时需要POST的数据
    data = {
    'lt': '',
    'execution': str,
    '_eventId': 'submit',
    'customerCode': '2_24',
    'accountTypeCode': '1_01',
    'username': account,
    'password': password,
    'captchaCod': ''
}
#设置请求头
    headers = {
    'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
#登录时表单提交到的地址（ 用开发者工具可以看到）
    login_url = 'https://cas.bzpt.edu.cn/login?service=https://xg.bzpt.edu.cn:2020/cas'
#构造Session
    session = requests.Session()
# 在session中发送登录请求， 此后这个session里就存储了cookie# 可以用prin(session.cookies.get_dict()) 查看
    resp = session.post(login_url, data, headers,verify=False)# 登录后才能访问的网页
    urll = 'https://xg.bzpt.edu.cn:2020/cosy/temperatureFill'
    urlT = 'https://xg.bzpt.edu.cn:2020/cosy/queryPersonInfo'
    respa = session.get(urlT).json()
    tww=["36.5","36.4","36.2","36.3","36.6","36.7"]
    int=random.randint(0,5)
#发送访问请求
    datat = {
    'tw': tww[int],
    'isCx': '2',
    'cxqksm': '',
    'bszz': '',
    'orgId': respa['data']['orgId'],
    'bjId': respa['data']['bjId'],
    'userId': respa['data']['userId'],
    'role': respa['data']['role']
}
    resp = session.post(urll, datat, headers).json()
    if resp["status"] == 200:
        print(name+"：体温上传成功" )
#收件人邮箱
        # text_content = "学院："+respa['data']['org']+"\n班级："+respa['data']['bj']+"\n姓名："+name +"\n学号："+respa['data']['xh']+"\n有饭提醒你："+ resp['data'] +"\n有饭微信公众号：有饭工作室 \n有饭微信小程序：有饭工具箱\n有钱终成眷属，没钱亲眼目睹"
        text_content = "学院："+respa['data']['org']+"\n班级："+respa['data']['bj']+"\n姓名："+name +"\n学号："+respa['data']['xh']+"\n有饭提醒你："+ resp['data'] +"\n有饭微信公众号：有饭工作室 \n有饭微信小程序：有饭工具箱\n \n有钱终成眷属，没钱亲眼目睹"
        send_email(qq,text_content)
    elif resp["status"] == 500:
        print(name+"：体温上传失败" )
#收件人邮箱
        text_content = "学院："+respa['data']['org']+"\n班级："+respa['data']['bj']+"\n姓名："+name +"\n学号："+respa['data']['xh']+"\n有饭提醒你："+ resp['data'] +"\n有饭微信公众号：有饭工作室 \n有饭微信小程序：有饭工具箱\n \n有钱终成眷属，没钱亲眼目睹"
        send_email(qq,text_content)

geturl("宋军歌", "201910070311", "026839", "2733411327")
