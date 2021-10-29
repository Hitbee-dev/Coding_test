m = int(input())
ball = 1
for _ in range(m):
    n = list(map(int, input().split()))
    if(n.count(ball) == 1):
        n.remove(ball)
        ball = n[0]
print(ball)
