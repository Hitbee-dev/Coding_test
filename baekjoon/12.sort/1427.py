n = int(input())
arr = list(map(int,str(n)))  
arr.sort(reverse=True) # 내림차순
for i in arr:
    print(i,end='')