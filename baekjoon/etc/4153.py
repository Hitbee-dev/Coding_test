while True:
    n, m, k = map(int, input().split())
    if(n%3 == 0 and m%4 == 0 and k%5 == 0):
        print("right")
    else:
        print("wrong")
    if(n == 0 and m == 0 and k == 0):
        break
