# _*_ coding: utf-8 _*_

# 调试模式是否开启
# DEBUG = True
#
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# # session必须要设置key
# SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#
# # mysql数据库连接信息,这里改为自己的账号
# SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/bi_export"
from flask import Flask

# app = Flask(__name__, static_url_path='', root_path='/data/soft/python3/pythonProjects/xiguaMock/xiguaMock/')

app = Flask(__name__, static_url_path='', root_path='',static_folder='static')
# app.config['SQLALCHEMY_ECHO']=True


# 只有在app对象之后声明，用于导入view模块

from controller import mockWebController
from controller import mockServerController