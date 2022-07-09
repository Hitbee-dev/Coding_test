import sys
input = sys.stdin.readline

S = input().strip()
buf = []
for i in range(len(S)):
    for j in range(len(S)):
        buf.append(S[i:j+1])
print(len(set(buf))-1)