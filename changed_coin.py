#거스름돈 주기

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types: # coin에 coin_types의 Index값을 넣음.
    count += n // coin # count에 n //(나누기 후 소수점을 버림)을 coin으로 나눔
    n %= coin # n값을 나누고 나머지를 구함
    print(f"n: {n}")

print(count)