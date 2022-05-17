import sys
for _ in range(3):
    sum = 0
    N = int(sys.stdin.readline()) # 앞에 나올 테스트케이스 개수
    for _ in range(N):
        num = int(sys.stdin.readline())
        sum += num

    if sum > 0:
        print("+")
    elif sum < 0:
        print("-")
    else:
        print("0")