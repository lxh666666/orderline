# -*- coding: utf-8 -*-
SERVER_PORT = 8000
DEBUG = False
SQLALCHEMY_ECHO = False

#有可能你使用浏览器看到的一串字符串不是那么容易看懂的，这是因为python底层使用unicode编码。
#通过设置下面的参数可以解决这个问题。
JSON_AS_ASCII = False

AUTH_COOKIE_NAME = "mooc_food"

SEO_TITLE = "Python Flask构建微信小程序订餐系统"
##过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

MINA_APP = {
    'appid':'wxcda782b150fecd0e', # 小程序id
    'appkey': 'c7b9c340058b1fc9fbd2e7cd0830b71d',
    'paykey':'xxxxxxxxxxxxxx换自己的',
    'mch_id':'xxxxxxxxxxxx换自己的',
    'callback_url':'/api/order/callback'
}


UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain':'http://81.70.149.29:8000'
}


PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}