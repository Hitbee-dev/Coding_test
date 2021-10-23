n = int(input())
result = []
for i in range(n):
    for j in range(n):
        if((i >= n/3 and i < (n/3)*2) and (j >= n/3 and j < (n/3)*2)): # 가운데 비우기
            result.append(" ")
        else:
            result.append("*")
    print("".join(str(_) for _ in result))
    result = []