def solution(n):
    cnt = 2
    num_set = set(range(n+1, 2*n+1)) #[리스트 생성] n보다 커야하니 n+1, 2n까지니까 2n+1
    for i in range(n, 2*n+1): #[소수 판별] 
        if i in num_set: #만약 생성한 리스트 안의 첫번째 원소부터 진행
            num_set -= set(range(cnt*2, 2*n+1, cnt)) #2의 배수부터 cnt값 만큼 2n+1까지 반복
            cnt += 1 #3, 4, 5 ... 등등 모든 배수 제거를 위한 카운트
    return len(num_set) #다 빼고 남은 리스트의 갯수 

while True:
    n = int(input())
    if(n == 0):
        break
    else:
        print(solution(n))