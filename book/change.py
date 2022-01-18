# 거스름돈

changed = [500, 100, 50, 10]
money = int(input())
num = 0

def change(m, n, c):
    for i in c:
        if (m // i) >= 1: # 나눠진다면
            n += m//i
            m = m - ((m//i)*i)
    return n
    
print(change(money, num, changed))