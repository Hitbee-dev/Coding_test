T = int(input())

for i in range(1, T+1):
    cnt = int(input())
    data = list(map(int, input().split(" ")))
    buf = []
    result = []
    for idx, j in enumerate(data):
        if buf == []:
            buf.append(j)
        elif j >= buf[-1]:
            buf.append(j)
        elif j < buf[-1]:
            result.append(buf)
            buf = []
            buf.append(j)
        if idx == len(data)-1:
            result.append(buf)
    sum = 0
    for index in result:
        for answer in range(len(index)):
            if len(index) == 1:
                pass
            else:
                sum += max(index)-index[answer]
    print(f"#{i} {sum}")

