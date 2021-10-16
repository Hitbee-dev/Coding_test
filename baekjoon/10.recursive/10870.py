n = int(input())
buffer = [0, 1]
for i in range(2, n+1):
    buffer.append((buffer[i-2])+(buffer[i-1]))
if(n == 0):
    print(0)
elif(n == 1):
    print(1)
else:
    print(buffer[-1]) 