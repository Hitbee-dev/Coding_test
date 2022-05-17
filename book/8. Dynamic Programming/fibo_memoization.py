# 피보나치 수 메모이제이션 사용

# 0으로 된 리스트 21개 생성(1부터 시작하기 때문에 0의 갯수를 +1 해준다.)
d = [0]*21

def fibo(x):
    if x == 1 or x == 2:
        print(f"끝. value: {x}")
        d[x] = 1
        print(d)
        return 1
    elif d[x] != 0:
        print(f"이미 계산한 값: {d[x]}")
        print(d)
        return d[x]
    else:
        print(f"d[x]: {d[x]} = fibo({x}-1) + fibo({x}-2)")
        d[x] = fibo(x-1) + fibo(x-2)
        print(d)
        return d[x]

print(fibo(20))