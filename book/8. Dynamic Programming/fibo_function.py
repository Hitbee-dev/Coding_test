d = [0] * 21

d[1] = 1
d[2] = 1
n = 20

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    print(d[i], end=" ")
print(d[n])