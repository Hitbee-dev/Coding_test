# 1.
# 도감에 수록되어있는 포켓몬의 개수 N
# 내가 맞춰야 하는 문제의 개수 M
# N과 M의 최대 개수는 10만개

# 2~
# 포켓몬의 번호가 1번인 포켓몬부터 N번까지 한줄씩 입력으로 들어옴
# 이름은 모두 영어 + 첫글자 대문자
# 일부 포켓몬은 마지막 문자만 대문자 일 수도 있음
# 포켓몬 이름의 최대 길이는 20, 최소는 2

# N~
# M개의 줄에 내가 맞춰야 하는 문제가 입력으로 들어옴
# 문제가 알파벳으로만 들어오면 포케몬 번호를 출력해야하고,
# 숫자로 들어오면 문자로 출력해야함

# 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어짐

# solution1
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
collection = dict()
for i in range(N):
    data = input().strip()
    collection[data] = str(i+1)
    collection[str(i+1)] = data

for j in range(M):
    print(collection[input().strip()])

# solution2
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().strip().split())
# collection = dict()
# for i in range(N):
#     collection[input().strip()] = i+1
# reverse_collection = dict(map(reversed, collection.items()))

# for j in range(M):
#     data = input().strip()
#     if data.isalpha():
#         print(collection[data])
#     else:
#         print(reverse_collection[int(data)])

