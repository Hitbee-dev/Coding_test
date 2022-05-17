pt = list(input())
et = list(input())
result = []
# 아스키코드로 a는 97 z는 122이다. 따라서 97~122까지이므로, -96해주면 됨
# for i in range(len(pt)):
#     print(ord(pt[i]))
while len(pt)>len(et): #암호화 키 갯수 맞춰주기
    et.extend(et)

for idx, i in enumerate(pt):
    if(i == " "):
        result.append(" ")
    elif(ord(i)-96 > (ord(et[idx])-96)):
        result.append(chr(ord(i)-(ord(et[idx])-96)))
    else:
        result.append(chr(122-((ord(et[idx])-96)-(ord(i)-96))))
print("".join(result))