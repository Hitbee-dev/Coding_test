import math

def squared(list, num):
    return list[num]*list[num]

while True:
    data = list(map(int, input().split()))

    print(math.sqrt(squared(data, 0)+squared(data, 1)))