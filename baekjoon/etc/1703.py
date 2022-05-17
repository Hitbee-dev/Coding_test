while True:
    n = list(map(int,input().split()))
    if(len(n) == 1):
        break
    else:
        result = n[1]
        for idx in range(1, len(n)-1):
            if(idx % 2 == 1):
                result = result-n[idx+1]
            else:
                result = result*n[idx+1]
        print(result)
