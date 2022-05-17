# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, AB, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 AB, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

# 예제 입력1
# 7 3
# 예제 출력1
# 10 4 21 2 1

n, m = map(int, input().split())
print(n+m)
print(n-m)
print(n*m)
print(n//m)
print(n%m)