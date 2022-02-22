"""
    최대 K번의 바꿔치기 연산을 진행할 수 있는데,
    바꿔치기 연산이란 배열A에 있는 원소와 배열B에 있는 원소를 골라서 바꾸는 방법이다.
    최종목표는 배열A의 모든 원소의 합이 최대가 되도록 하는 것.
    N, K, 배열A, B가 주어질 때 배열A의 모든 원소의 합이 최대가 되도록 출력하여라.
"""

# 입력 예시     | 출력 예시
# 5 3         | 26
# 1 2 5 4 3   |
# 5 5 6 6 5   |

def lic(n, k, a, b):
    # 최대 K번 만큼 바꿔치기 연산 가능
    # 쉽게 생각해서 A배열에서 제일 작은수와 B배열의 제일 큰 수를 스위칭 하면 됨.
    for _ in range(k):
        if min(a) < max(b):
            buf = min(a)
            a[a.index(min(a))] = b[b.index(max(b))]
            b[b.index(max(b))] = buf
    return sum(a)

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

N, K = 5, 3
A = [1, 2, 5, 4, 3]
B = [5, 5, 6, 6, 5]
print(lic(N, K, A, B))