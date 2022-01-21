import time

num = int(input())

def prints(n):
    for i in range(1, n+1):
        print(i)

start_time = time.time()
prints(num)
end_time = time.time()
print(f"수행시간: {end_time-start_time}")