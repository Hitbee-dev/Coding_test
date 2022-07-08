import sys
input = sys.stdin.readline

N = int(input().strip())
N_arr = dict()
for i in map(int, input().split()):
    if i in N_arr:
        N_arr[i] += 1
    else:
        N_arr[i] = 1

M = int(input().strip())
for i in map(int, input().split()):
    if i in N_arr:
        print(N_arr[i], end = " ")
    else:
        print(0, end = " ")