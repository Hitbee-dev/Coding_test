# 재귀함수를 사용하여 ["a", "b", "c"]로 만들수 있는 모든 경우의 수를 출력하라.

def req(s):
    if len(s) == len(data):
        return print(s)

    for i in data:
        req(s+i)

data = ["a", "b", "c"]
result = ""
req(result)