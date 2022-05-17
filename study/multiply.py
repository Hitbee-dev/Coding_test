# 곱셈은 내장함수가 없기 때문에 아래 함수를 사용하면 편하다.

def multiply(arr):
    return eval('*'.join(map(str, arr)))