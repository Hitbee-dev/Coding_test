import math 
n = int(input())
n_log = round(math.log(n, 3))
# print(n_log)
_patten = [
    ["*", "*", "*"],
    ["*", " ", "*"],
    ["*", "*", "*"]
]

_blank = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def _(x):
    return 'null' if x % 3 == 0 else x
    
map(_, [1, 4, 3, 4, 5, 6])

def is_blank(x, y):
    for i in range(1, n_log):
        if (x // (3 ** i) % 3 == 1 and y // (3 ** i) % 3 == 1):
            return True
    return False

for y in range(n): #27번 반복
    result = []
    for x in range(n): #27번 반복
        xp = x % 3 # 최소단위 x좌표
        yp = y % 3 # 최소단위 y좌표

        if is_blank(x, y):
            result.append(_blank[xp][yp])
        else:
            result.append(_patten[xp][yp])

    print("".join(str(_) for _ in result))