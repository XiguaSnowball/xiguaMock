from model.utils.sqlAlUtil import sqlAlUtil

session = sqlAlUtil.session

from imp import reload
from setting import app
import sys
import configparser
from flask_sqlalchemy import SQLAlchemy

reload(sys)

def getconfig():
    cf = configparser.ConfigParser()
    path = 'model/dbmodels/db.config'
    cf.read(path)
    _dburi = cf.get("database", "dbhost")
    return _dburi

app.config['SQLALCHEMY_DATABASE_URI'] = getconfig()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class mock_config(db.Model):
    """定义数据模型"""
    __tablename__ = 'mock_config'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    reqparams = db.Column(db.String(500))
    methods = db.Column(db.String(50))
    domain = db.Column(db.String(50))
    description = db.Column(db.String(50))
    resparams = db.Column(db.String(500))
    update_time = db.Column(db.TIMESTAMP)
    status = db.Column(db.Integer)
    ischeck = db.Column(db.Integer)
    project_name = db.Column(db.String(20))



# 新增一条数据
# 原生sql：insert  into mysql.hello_word(name,password) values("test2","1234")；
