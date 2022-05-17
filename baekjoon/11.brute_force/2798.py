N, M = map(int, input().split()) #카드의 개수와 최대숫자
card_list = list(map(int, input().split())) #카드 숫자
result = 0
flag = 0
if(flag == 0):
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if(result < card_list[i]+card_list[j]+card_list[k] < M):
                    result = card_list[i]+card_list[j]+card_list[k]
                elif(card_list[i]+card_list[j]+card_list[k] == M):
                    result = card_list[i]+card_list[j]+card_list[k]
                    flag = 1              
print(result)

