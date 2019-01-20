import json
import random


def json_txt(dic_json):
    if isinstance(dic_json, dict):
        # print("%s:%s" % (key, value))
        for key, value in dic_json.items():
            keyAfter, a, b = rangeChack(key)
            # print(a,b)
            valueRandom = value
            if a and b:
                # 对应value的个数
                count = random.randint(a, b)

                if isinstance(value, str):
                    valueRandom = value * (random.randint(a, b))

                elif isinstance(value, int):
                    valueRandom = random.randint(a, b)

                elif isinstance(value, float):
                    valueRandom = ("%.2f" % (random.uniform(a, b)))

                elif isinstance(value, list):
                    valueRandom = random.sample(value, count)
                    pass
                    # json_txt(value)

                elif isinstance(value, dict):
                    pass
                    # json_txt(value)

                elif isinstance(value, bool):
                    pass

                dic_json[keyAfter] = valueRandom
                del dic_json[key]

            else:
                dic_json[keyAfter] = value
            json_txt(value)

    if isinstance(dic_json, list):
        for i in dic_json:
            json_txt(i)

    return dic_json

def rangeChack(key):
    mark1 = "|"
    mark2 = "-"
    rangeOfKeyStart = ""
    rangeOfKeyEnd = ""
    keyAfter = key
    if mark1 in str(key):
        indexOfMark1 = key.index(mark1)
        # 总的范围
        rangeOfKey = key[indexOfMark1 + 1:]
        keyAfter = key[:indexOfMark1]
        # print(rangeOfKey)

        # 随机的数量
        if mark2 in rangeOfKey:
            indexOfMark2 = rangeOfKey.index(mark2)
            rangeOfKeyStart = rangeOfKey[0]
            # print(rangeOfKeyStart)

            rangeOfKeyEnd = rangeOfKey[indexOfMark2 + 1:]
            # print(rangeOfKeyEnd)

        else:
            rangeOfKeyStart = rangeOfKey
            # print(rangeOfKeyStart)

            rangeOfKeyEnd = rangeOfKey
            # print(rangeOfKeyEnd)

        return keyAfter, int(rangeOfKeyStart), int(rangeOfKeyEnd)

    else:
        return keyAfter, rangeOfKeyStart, rangeOfKeyEnd


a = """{
    "code":0,
    "data|1-3":{
    "aaaa":{
    "b|1-88":1
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

b = """{
"b|1-88":1,
"data":{
    "aaaa":[{"eee|1-20":2.11},{"ggg|1-20":1}],"fff|3":"成功","count|3":"d"
},
"ccc|1-8":"d"
}


"""

a = json.loads(b)
len_3 = len(a)

dic = json_txt(a)
print(dic)
