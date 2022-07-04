recycle = int(input()) # 반복 횟수
dicts = {}
min_length = []

for i in range(6):
    x, y = map(int, input().split())
    if x not in dicts.keys():
        dicts[x] = y
    else:
        min_length.append(y)
        dicts[x] = dicts[x], y

max_length = []
buf = []
for i in dicts.values(): # 제일 큰 넓이 구하기
    if type(i) != tuple:
        max_length.append(i)
    else:
        buf.extend(i)
print(((max_length[0] * max_length[1]) - (min_length[0] * (buf[buf.index(min_length[0])-3])))*recycle)
# 도대체 왜 틀렸는지 이유를 모르겠네 ㅡㅡ