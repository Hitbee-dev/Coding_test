n = int(input())
result = 1
for i in range(1, n):
    result += i * result

print(result)