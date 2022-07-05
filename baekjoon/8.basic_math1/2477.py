recycle = int(input()) # 반복 횟수
result = []
values = []
dicts = {}

for i in range(6):
    x, y = map(int, input().split())
    result.append(x)    # 들어온 순서 대로 저장
    values.append(y)
    if x not in dicts.keys():
        dicts[x] = y
    else:
        dicts[x] = dicts[x], y
        
max_idx = []
for k, v in dicts.items(): # 중복되는 값 찾기
    if type(v) != tuple:
        max_idx.append(v)

if result[0] == result[4] and result[1] == result[5]:
    print((((max_idx[0] * max_idx[1])-(values[0] * values[5]))*recycle))
else:
    flag = True
    while flag is True:
        if result[0] == result[2] and result[1] == result[3]:
            print((((max_idx[0] * max_idx[1])-(values[1] * values[2]))*recycle))
            flag = False
        else:
            result.append(result[0])
            result.pop(0)
            values.append(values[0])
            values.pop(0)