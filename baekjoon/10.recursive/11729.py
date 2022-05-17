def hanoi(n, start, end):
    if(n==1):
        print(start, end) #큰 원판이 하나만 남았을 때 이동위치 출력
        return

    #start와 end의 막대번호는 알고있지만, 나머지 하나가 어떤 막대인지 모르므로
    #6-start-end를 해주면 나머지 막대번호를 알 수 있다.
    hanoi(n-1, start, 6-start-end) #1개빼고 전부 1 -> 2로 이동(n-1)
    print(start, end) #1 -> 3으로 가장 큰 원판 하나 이동
    hanoi(n-1, 6-start-end, end) #2 -> 3으로 전부 이동

n = int(input())
print((2**n)-1) # 최소 이동가능 횟수
hanoi(n, 1, 3) #1, 2, 3의 장대 재귀함수