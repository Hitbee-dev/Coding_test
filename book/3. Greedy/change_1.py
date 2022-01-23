# 거스름돈1

arr = [500, 100, 50, 10]
money = int(input())
num = 0

def change(m, n, a):
    for i in a:
        if (m // i) >= 1: # 나눠진다면
            n += m//i # 몫
            m = m%i # 나머지
    return n
    
print(change(money, num, arr))