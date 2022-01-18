# 거스름돈2

# case1
# 1300 -> 500, 400, 400[3개]

# case2
# 800 -> 400, 400[2개]

arr = [500, 400, 100]
result = []
inputs = int(input())

# 500원짜리 2개, 1개, 0개 일때만 하면 되는거 아닌가? 어차피 그 이후론 의미x

def change(len):
    for i in range(len):
        money = inputs
        cnt = 0
        cnt += i
        money = money-(i*arr[0]) # 500원짜리 0, 1, 2개일 때
        for j in arr[1:]:
            if (money//j) >= 1: # 만약 나누어 진다면,
                cnt += money//j
                money = money%j
        if money >= 0:
            result.append(cnt)
    return min(result)

print(change(3))