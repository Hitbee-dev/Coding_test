import math

while True:
    n = int(input())
    if(n == 1):
        print(1)
        continue
    elif(n == 0):
        break
    else:
        buffer = []
        cnt = 1
        count = 0
        for i in range(n, (2*n)+1):
            if(i <= 1):
                continue
            check = True
            for p in range(2, int(math.sqrt(i))+1):
                if(i % p == 0):
                    check = False
                    break
            if(check):
                if(i != n):
                    count += 1
        print(count)
