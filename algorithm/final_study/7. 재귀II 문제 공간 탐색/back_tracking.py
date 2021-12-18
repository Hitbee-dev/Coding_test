# 재귀함수를 사용하여 ["a", "b", "c"]로 만들수 있는 모든 경우의 수를 출력하라.
# 단, 중복 x
# 백트래킹 형식으로 변경

def req(s):
    global used_data

    if len(s) == len(data):
        return print(s)

    for i in data:
        if i not in used_data:
            used_data.add(i)
            req(s+i)
            used_data.remove(i)

data = ["a", "b", "c"]
result = ""
used_data = set()
req(result)