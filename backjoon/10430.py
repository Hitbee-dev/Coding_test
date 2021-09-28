# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 (A+B)%C
# 둘째 줄에 ((A%C) + (B%C))%C
# 셋째 줄에 (A×B)%C
# 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

#예제 입력1
#5 8 4

#예제 출력1
#1
#1
#0
#0

n, m, k = map(int, input().split())
print((n+m)%k)
print(((n%k)+(m%k))%k)
print((n*m)%k)
print((n%k)*(m%k)%k)