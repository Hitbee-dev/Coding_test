n = int(input())
arr = []

for i in range(n):
    arr.append(input().strip())
set_arr = set(arr)
arr = list(set_arr)
arr.sort() # 정렬
arr.sort(key = len) # 길이 순 정렬

for i in arr:
    print(i)