# -*- coding: utf-8 -*-
from flask import Flask

# app = Flask(__name__, static_url_path='', root_path='/data/soft/python3/pythonProjects/xiguaMock/xiguaMock/')

app = Flask(__name__, static_url_path='', root_path='../xiguaMock/')
# app.config['SQLALCHEMY_ECHO']=True


# 只有在app对象之后声明，用于导入view模块

# from xiguaMock.controller import testController
# from xiguaMock.controller import dbController
from xiguaMock.controller import mockServerController
from xiguaMock.controller import mockWebController

