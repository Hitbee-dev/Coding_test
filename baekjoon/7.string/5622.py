n = input()
result = 0

for i in range(len(n)):
    if(ord(n[i]) <= 67):
        result += 2
    elif(ord(n[i]) <= 70):
        result += 3
    elif(ord(n[i]) <= 73):
        result += 4
    elif(ord(n[i]) <= 76):
        result += 5
    elif(ord(n[i]) <= 79):
        result += 6
    elif(ord(n[i]) <= 83):
        result += 7
    elif(ord(n[i]) <= 86):
        result += 8
    elif(ord(n[i]) <= 90):
        result += 9

print(result+len(n))