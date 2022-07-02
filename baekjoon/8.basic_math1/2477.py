recycle = int(input()) # 반복 횟수
direction = []
result = []
flag = 0 # 정방향: 0, 역방향: 1

for i in range(6):
    x, y = map(int, input().split())
    direction.append(x)
    result.append(y)

max_index = result.index(max(result))
before_index = max_index - 1
if max_index == 5:
    after_index = max_index - 6
else:
    after_index = max_index + 1

if result[before_index] < result[after_index]: # 만약 +1 인덱스가 더 크다면
    flag = 1
max_index -= 6
if flag == 0:
    print(((result[max_index] * result[max_index-1]) - (result[max_index+2] * result[max_index+3]))* recycle)
else:
    print(((result[max_index] * result[max_index+1]) + (result[max_index+3] * result[max_index+4]))*recycle)
