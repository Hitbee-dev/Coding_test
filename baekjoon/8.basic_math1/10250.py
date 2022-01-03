k = int(input())

for i in range(k):
    h, w, n = map(int, input().split())
    cnt = 1
    buffer = ""
    while n//h != 0:
        cnt += 1
        n = n-h

    if(n == 0):
        n = h
        cnt -= 1
    if(cnt < 10):
        buffer = str(n)+"0"+str(cnt)
    else:
        buffer = str(n)+str(cnt)
    print(int(buffer))