#숫자 카드 게임

#입력 조건
#1. 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.(1<= N, M M=100)
#2. 둘째 줄로부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10,000 이하의 자연수이다.

#출력 조건
#1. 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

#입력 예시1
#3 3
#3 1 2
#4 1 4
#2 2 2

#출력 예시1
#2

#입력 예시2
#2 4
#7 3 1 8
#3 3 3 4

#출력 예시2
#3

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    print(f"min: {min_value}")
    result = max(result, min_value)
    print(f"result: {result}")

print(result)