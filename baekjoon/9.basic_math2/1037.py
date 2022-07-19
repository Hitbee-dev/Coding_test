import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
print(min(arr) * max(arr))