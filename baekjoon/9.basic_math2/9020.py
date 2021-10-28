def prime():
    check = [False, False] + [True] * 10000 #최대 10000개

    for i in range(2, 101): #10000의 제곱수+1
        if check[i] == True:
            for j in range(i+i, 10000+1, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())
        case1 = n // 2
        case2 = case1
        for _ in range(10000):
            if check[case1] and check[case2]:
                print(case1, case2)
                break
            case1 -= 1
            case2 += 1

prime()