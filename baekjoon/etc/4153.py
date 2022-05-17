import math

while True:
    buffer = list(map(int, input().split()))
    buffer.sort()
    if(buffer[0] == 0 and buffer[1] == 0 and buffer[2] == 0):
        break
    else:
        if(math.sqrt((buffer[0]*buffer[0])+(buffer[1]*buffer[1])) == math.sqrt((buffer[2]*buffer[2]))):
            print("right")
        elif(math.sqrt((buffer[1]*buffer[1])+(buffer[2]*buffer[2])) == math.sqrt((buffer[0]*buffer[0]))):
            print("right")
        elif(math.sqrt((buffer[0]*buffer[0])+(buffer[2]*buffer[2])) == math.sqrt((buffer[1]*buffer[1]))):
            print("right")
        else:
            print("wrong")
        