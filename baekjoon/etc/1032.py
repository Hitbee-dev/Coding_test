n = int(input())
m = list(input())
for i in range(n - 1):
    k = list(input())
    for j in range(len(m)):
        if m[j] != k[j]:
            m[j] = '?'
print(''.join(m))