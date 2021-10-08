import math

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    init_n = n
    max_cnt = int(math.sqrt(m-n))
    move1 = 0
    move2 = 0
    cnt = 0

    while n <= m:
        if(move1 != max_cnt):
            move1 += 1
        cnt += 1
        n = n+move1
        m = m-move1
        # print(f"cnt: {cnt}, front_move: {move1}, n: {n}, m: {m}")

    while m > init_n:
        if(m-move2 != 0):
            move2 += 1
        cnt += 1
        m = m-move2
        # print(f"cnt: {cnt}, back_move: {move2}, n: {n}, m: {m}")
    print(cnt)
