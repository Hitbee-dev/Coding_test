T = int(input())

for i in range(1, T+1):
    sum = 0
    cnt = int(input())
    data = list(map(int, input().split(" ")))
    price = 0
    for j in range(cnt, 1, -1):
        if price < data[j-1]:
            price = data[j-1]
        if price >= data[j-2]:
            sum += price - data[j-2]

    print(f"#{i} {sum}")