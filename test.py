import json

dic ={}

def json_txt(dic_json):
    if isinstance(dic_json, dict) :
        # 判断是否是字典类型isinstance 返回True false
        for key in dic_json:
            mark1 = "|"
            mark2 = "-"
            rangeOfKey =""
            if mark1 in str(key):
                indexOfMark1 = key.index(mark1)
                # 总的范围
                rangeOfKey = key[indexOfMark1 + 1:]
                # print(rangeOfKey)





            if isinstance(dic_json[key], dict):
                # print("字典  %s :%s" % (key, dic_json[key]))
                json_txt(dic_json[key])

                dic[key] = {
                    "range": rangeOfKey
                }

            # 如果dic_json[key]是数组类型
            elif  isinstance(dic_json[key], list):
                # print("数组 %s :%s" % (key, dic_json[key]))
                for i in dic_json[key]:
                    json_txt(i)


            else:
                rangeOfKey = ""

            dic[key] = {
                "range":rangeOfKey,
            }
            # dic[key[:indexOfMark1]] = {
            #     "range":rangeOfKey,
            # }

            print(dic)
                #
                # # 随机的数量
                # if mark2 in rangeOfKey:
                #     rangeOfKeyStart = rangeOfKey[0]
                #     print(rangeOfKeyStart)
                #
                #     rangeOfKeyEnd = rangeOfKey[-1]
                #     print(rangeOfKeyEnd)
                #
                # else:
                #     rangeOfKeyStart = rangeOfKey
                #     print(rangeOfKeyStart)
                #
                #     rangeOfKeyEnd = rangeOfKey
                #     print(rangeOfKeyEnd)
                #     dic[key] = dic_json[key]
            # 如果dic_json[key]依旧是字典类型







def randomResult(originalResult):
    print(originalResult)
    print(type(originalResult))

    formatResult = ''

    originalResult = json.loads(originalResult)



    for resultKey in originalResult.keys():
        print(resultKey)


if __name__ == '__main__':
    a = """{
    "code":0,
    "data|1-3":{
    "aaaa":{
    "b":1
    },
        "count":5,
        "responseList|2-3":[
            {
                "id":304,
                "nickName|6":[
                    "候春磊",
                    "小明",
                    "小兰"
                ],
                "createTimeStr":"2019-01-04 18:07:36"
            }
        ]
    }
}"""

    a = json.loads(a)

    # randomResult(a)
    json_txt(a)
    print("dic: " + str(dic))
