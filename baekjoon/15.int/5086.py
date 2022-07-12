# 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.
import sys
input = sys.stdin.readline

flag = True
while flag:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x > y:
        if x % y == 0:
            print("multiple")
        else:
            print("neither")
    else:
        if y % x == 0:
            print("factor")
        else:
            print("neither")