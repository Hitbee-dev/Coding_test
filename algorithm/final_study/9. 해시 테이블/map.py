# 아래와 같은 문장을 입력받고, 사용되지 않은 알파벳을 출력하는 코드를 작성하라.

data = """
           the basic outfit of traditional inuit clothing consisted of a
           parka, pants, mittens, inner footwear, and outer boots, historically made
           from animal hide and fur. the inuit are a group of culturally related indigenous
           peoples inhabiting the arctic areas of the united states, canada, and greenland
       """

dic = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
    "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
    "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, " ": 0
}

for i in data:
    if i in dic:
        dic[i] += 1

def get_key(val):
    for k, v in dic.items():
        if v == val:
            result.append(k)
result = []
get_key(0)
print(result)
print(dic)