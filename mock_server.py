# -*- coding: utf-8 -*-
from imp import reload

from flask import jsonify, Flask, make_response, request
import sys, requests, json
import configparser
from flask_sqlalchemy import SQLAlchemy

reload(sys)

# 如果在mock_server中没有数据是否进行转发 0为是，非0为否
relay = 0
# 转发服务器地址
host1 = 'http://172.16.156.67:5202'



def getconfig():
    cf = configparser.ConfigParser()
    path = 'db.config'
    cf.read(path)
    _dburi = cf.get("database", "dbhost")
    return _dburi


app = Flask(__name__)
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

# todo:根据返回值构造随机数，list等
def randomResult(originalResult):
    print(originalResult)
    print(type(originalResult))

    formatResult = ''

    originalResult = json.loads(originalResult)

    for resultKey in originalResult.keys():
        print(resultKey)



    return formatResult

def checksize(domain, method):
    # 校验domain是否存在
    mock = mock_config.query.filter_by(domain=domain).first()
    # 校验method是否存在
    mock1 = mock_config.query.filter(mock_config.domain == domain,
                                     mock_config.methods == method).first()
    if not mock:
        return jsonify({"status": "fail", "msg": u"请求方法不存在"})
    elif not mock1:
        return jsonify({"status": "fail", "msg": u"请求方法对应的请求方式不存在"})


def checkpath(domain, varsvalue, method):
    # 字符格式转换
    method = method.lower()

    # 判断请求方法和模式是否匹配
    re = checksize(domain, method)
    if re is not None:
        return re

    # 获取发送请求入参
    if method == 'get':
        # 入参校验
        varsvalue1 = getvar_get(varsvalue)
        a = checkparams(domain, varsvalue1)
        return a

    elif method == 'post':
        # 入参校验
        varsvalue1 = varsvalue
        a = checkparams(domain, varsvalue1)
        return a

    else:
        result_json = {"status": "fail", "msg": u"暂不支持该类型请求方法"}
        return result_json


def checkparams(domain, varsvalue1):


    # 数据库中的预期请求参数
    mock_data = mock_config.query.filter(mock_config.status == 0, mock_config.domain == domain).all()

    for mock_data_item in mock_data:
        varsvalue2 = mock_data_item.reqparams
        # todo:
        # 入参格式校验
        # 0-不校验参数 1-校验参数格式
        # if mock_data.ischeck == 0:

        if mock_data_item.methods.lower() == 'get':
            if varsvalue1 == varsvalue2:
                if mock_data_item.resparams == '':
                    result_json = {"status": "fail", "msg": u"对应请求没有配置预期返回值"}
                    return result_json
                else:
                    formatResult = randomResult(mock_data_item.resparams)
                    result_json = {"status": "success", "msg": u"请求成功", "result": formatResult}
                    return result_json

        if mock_data_item.methods.lower() == 'post':
            # varsvalue1 = str(varsvalue1).replace("\t", "").replace("\r", "").strip()
            varsvalue2 = varsvalue2.replace("\t", "").replace("\r", "").strip()
            varsvalue3 = eval(varsvalue2)
            if str(varsvalue1) == str(varsvalue3):
                if mock_data_item.resparams == '':
                    result_json = {"status": "fail", "msg": u"对应请求没有配置预期返回值"}
                    return result_json
                else:
                    formatResult = randomResult(mock_data_item.resparams)
                    result_json = {"status": "success", "msg": u"请求成功", "result": formatResult}
                    return result_json

        continue
    result_json = {"status": "fail", "msg": u"该接口未激活或没有该入参对应的返回值"}
    return result_json


# 将调用时的入参字典转为与数据库格式匹配的字符串
def getvar_get(value):
    # value = value[::-1]
    # print(value)
    result = []
    for key in value:
        item = key + '=' + value[key]
        result.append(item)

    result_str = "&".join(result)
    return result_str


def getvar_post(value):
    # value = value[::-1]
    # print(value)
    result = []
    for key in value:
        item = key + '=' + value[key]
        result.append(item)

    result_str = "&".join(result)
    return result_str


# def getres(mock_data, npath, host):
#     varsvalue = request.args.to_dict()
#     params = getvar_get(varsvalue)
#     url1 = host + npath + '?'
#     if request.method == 'GET':
#         re = requests.get(url1, params=params)
#     else:
#         re = requests.post(url1, params=params)
#     return re, params


@app.route('/<path:path>/<path:path1>', methods=['GET', 'POST'])
def get_all_task(path, path1):
    npath = '/' + path + '/' + path1
    if request.method == 'GET':
        varsvalue1 = request.args
        varsvalue = varsvalue1.to_dict()
        # varsvalue = request.args.items().__str__()
        # print(varsvalue)
    else:
        varsvalue = json.loads(request.data)
        # varsvalue = request.form.items()

    r = checkpath(npath, varsvalue, request.method)

    if r['status'] == 'fail' and relay == 0:
        return jsonify(r)
        # result_msg = r['msg']
        # re1 = getres(request, npath, host1)
        # return re1[0].content

    else:
        result = json.loads(r['result'])
        return jsonify(result)


@app.route('/<path:path>', methods=['GET', 'POST'])
def get_all_task1(path):
    path = '/' + path
    if request.method == 'GET':
        varsvalue1 = request.args
        varsvalue = varsvalue1.to_dict()
        # varsvalue = request.args.items().__str__()
        # print(varsvalue)
    else:
        varsvalue = json.loads(request.data)
        # varsvalue = request.form.items()


    r = checkpath(path, varsvalue, request.method)

    if r['status'] == 'fail' and relay == 0:
        return jsonify(r)
        # result_msg = r['msg']
        # re1 = getres(request, npath, host1)
        # return re1[0].content

    else:
        result = json.loads(r['result'])
        return jsonify(result)



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'msg': 'fail', 'error': '404 Not found1111'}), 404)


@app.errorhandler(500)
def not_found(error):
    return make_response(u"程序报错", 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5203, threaded=True, debug=True)
