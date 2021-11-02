#for 문을 재귀함수로 바꾸는 방법

def arr_rec(n):
    if(n < 1):
        return n
    return n+arr_rec(n-1)

print(arr_rec(5))