# 문자열 재정렬

""" 요약
    알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어진다.
    이때, 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤,
    그 뒤에 [모든 숫자를 더한 값]을 이어서 출력한다.
    ex) K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력한다.
"""

strings = input()

def string_re(s):
    buf = []
    num = 0
    result = ""
    # 아스키코드 순으로 정렬하면 숫자가 더 앞에있으니 따로 리스트에 저장하여 나중에 합쳐준다.
    for i in s:
        if ord(i) <= 57:
            num += int(i)
        else:
            buf.append(ord(i))
    buf.sort()
    for i in buf:
        result += chr(i)
    result += str(num)
    return result

print(string_re(strings))