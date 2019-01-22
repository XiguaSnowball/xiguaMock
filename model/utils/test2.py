import json
import random


def randomResult(dic_json):
    if isinstance(dic_json, dict):
        for key, value in dic_json.items():
            keyAfter, a, b, loopCountOfValue = rangeChack(key)
            valueRandom = value
            valueRandom_str = str(valueRandom)

            if (a and b) or loopCountOfValue:

                if isinstance(value, str):
                    valueRandom = value * (random.randint(a, b))

                elif isinstance(value, int) and valueRandom_str != 'True' and valueRandom_str != 'False':
                    valueRandom = random.randint(a, b)

                elif isinstance(value, float):
                    valueRandom = ("%.2f" % (random.uniform(a, b)))

                elif isinstance(value, list):
                    if a and b:
                        # 对应value的个数
                        count = random.randint(a, b)
                        valueRandom = random.sample(value, count)
                    elif loopCountOfValue:
                        valueRandom = value * loopCountOfValue
                    else:
                        valueRandom = value

                elif isinstance(value, dict):
                    countDic = random.randint(a, b)
                    valueRandom = dict(random.sample(value.items(), countDic))

                # 随机返回bool类型true或false
                elif isinstance(value, bool) and (valueRandom_str == 'True' or valueRandom_str == 'False'):
                    valueRandom = random.choice([True, False])

                dic_json[keyAfter] = valueRandom
                del dic_json[key]

            else:
                dic_json[keyAfter] = value

            randomResult(value)

    if isinstance(dic_json, list):
        for i in dic_json:
            randomResult(i)

    return dic_json


def rangeChack(key):
    mark1 = "|"
    mark2 = "-"
    mark3 = "+"
    rangeOfKeyStart = ""
    rangeOfKeyEnd = ""
    loopCount = ""
    keyAfter = key
    if mark1 in str(key):
        indexOfMark1 = key.index(mark1)
        # 总的范围
        rangeOfKey = key[indexOfMark1 + 1:]
        keyAfter = key[:indexOfMark1]

        # 判断是否为重复输出规则
        if mark3 in rangeOfKey:
            indexOfMark3 = rangeOfKey.index(mark3)

            if mark2 in rangeOfKey:
                indexOfMark2 = rangeOfKey.index(mark2)
                loopOfKeyStart = rangeOfKey[indexOfMark3 + 1:indexOfMark2]
                loopOfKeyEnd = rangeOfKey[indexOfMark2 + 1:]

            else:
                loopOfKeyStart = rangeOfKey[1]
                loopOfKeyEnd = rangeOfKey[indexOfMark3 + 1:]

            # 重复次数
            loopCount = random.randint(int(loopOfKeyStart), int(loopOfKeyEnd))
            return keyAfter, rangeOfKeyStart, rangeOfKeyEnd, loopCount

        # 随机的数量

        elif mark2 in rangeOfKey:
            indexOfMark2 = rangeOfKey.index(mark2)
            rangeOfKeyStart = rangeOfKey[0]
            rangeOfKeyEnd = rangeOfKey[indexOfMark2 + 1:]

        else:
            rangeOfKeyStart = rangeOfKey
            rangeOfKeyEnd = rangeOfKey

        return keyAfter, int(rangeOfKeyStart), int(rangeOfKeyEnd), loopCount

    else:
        return keyAfter, rangeOfKeyStart, rangeOfKeyEnd, loopCount


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

b = """

{"a|2":{"list":1,
"ccc":2,
"bbb":3,
"bool":true,
"xount":{"dfdfd|1-2":{
"a":1,"b":2,"c":3,"d":4
}}}

}
"""

a = json.loads(b)
len_3 = len(a)

dic = randomResult(a)
print(dic)
