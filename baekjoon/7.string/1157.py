# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1, 000, 000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

n = input()
buffer = []
cnt = []

for i in range(len(n)):
    buffer.append(n[i].upper())

set_buffer = list(set(buffer))

for j in range(len(set_buffer)):
    cnt.append(buffer.count(set_buffer[j]))

if(cnt.count(max(cnt)) > 1):
    print("?")
elif(cnt.count(max(cnt)) == 1):
    print(set_buffer[cnt.index(max(cnt))])