m = int(input())
ball = 1 #처음 공이 있는 위치
for _ in range(m):
    n = list(map(int, input().split()))
    if(n.count(ball) == 1):
        n.remove(ball)
        ball = n[0]
print(ball)
