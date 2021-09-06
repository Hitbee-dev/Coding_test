#여행가 A는 N*N크기의 정사각형 공간위에 서있다.
#이 공간은 1x1크기의 정사각형으로 나누어져있다.
#가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는(N*N)이다.
#여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다.
#우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여있다.
#계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D중 하나의 문자가 반복적으로 적혀있다.
#각 문자의 의미는 다음과 같다.
#L: 왼쪽으로 한 칸 이동
#R: 오른쪽으로 한 칸 이동
#U: 위쪽으로 한 칸 이동
#D: 아래쪽으로 한 칸 이동
#이때 여행가 A가 N*N크기의 정사각형 공간을 벗어나는 움직임은 무시한다.
#예를들어 (1,1)위치에서 L, U을 만나면 무시한다.

#계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

#입력 조건
#1. 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
#2. 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동횟수 <= 100)

#출력 조건
#1. 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.

#입력 예시
#5
#R R R U D D

#출력 예시
#3 4

#해결
# n = int(input("공간의 크기를 입력해주세요: "))
# move = list(map(str, input("이동할 계획서를 입력 해 주세요: ").split()))
# data = []
# for i in range(n):
#     for j in range(n):
#         data += (i+1, j+1)

# i, j = 1, 1 #시작지점 (1, 1)

# if not (len(move) == 0):
#     for k in range(len(move)):
#         if(move[k] == "L"):
#             if not(j == 1):
#                 j = j-1
#         elif(move[k] == "R"):
#             if not(j == n-1):
#                 j = j+1
#         elif(move[k] == "U"):
#             if not(i == 1):
#                 i = i+1
#         elif(move[k] == "D"):
#             if not(i == n-1):
#                 i = i+1
            
# print(f"{i}, {j}")

#정답
#N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 입력 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if(plan == move_types[i]):
            nx = x+dx[i]
            ny = y+dy[i]
    #공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    #이동 수행
    x, y = nx, ny
print(x, y)
        
        