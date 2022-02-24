# 성적이 낮은 순서로 학생 출력하기

# 입력 조건 | 출력 조건
# 2       | 이순신 홍길동
# 홍길동 95 |
# 이순신 77 |

# 딕셔너리를 활용
N = int(input())
NAMES, SCORES = [], []
data = {}
buffer = []
for _ in range(N):
    name, score = map(str, input().split())
    data[score] = name
result = sorted(data.items())
for _, name in result:
    print(name, end=" ")