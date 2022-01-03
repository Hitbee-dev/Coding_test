a, b, v = map(int, input().split())
# print(v-(a-b))# 정상에 올라갔다가 밤에 내려오는 카운트까지 해버림(처음 쓴 답)
result = (v-b)//(a-b)
buffer = (v-b)%(a-b)
if(buffer == 0):
    print(result)
else:
    print(result+1)