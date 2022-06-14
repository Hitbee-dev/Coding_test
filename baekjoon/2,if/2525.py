hour, min = list(map(int, (input().split())))
plus_min = int(input())

buf_hour = plus_min//60
buf_min = plus_min%60

if min+buf_min >= 60:
    buf_hour+=1
    min = (min+buf_min)-60
else:
    min += buf_min

if hour+buf_hour > 23:
    hour = abs((hour+buf_hour)-24)
else:
    hour += buf_hour

print(hour, min)