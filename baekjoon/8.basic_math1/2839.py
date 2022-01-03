n = int(input())
i = 5
j = 3

i_cnt = 0
j_cnt = 0

def solution(i_cnt, j_cnt):
    # print(f"{i_cnt}, {j_cnt}, {i_cnt+j_cnt}")
    print(i_cnt+j_cnt)

# for n in range(1, 300):
#     print(f"No. {n}")
if(n%i == 0):
    print(n//i)
elif(n<3 or n==7 or n==4):
    print(-1)
elif(n == 9):
    print(n//j)
else:
    if(n%i == 1):
        case1 = n-6
        i_cnt = case1//i
        j_cnt = (n-case1)//j
        solution(i_cnt, j_cnt)
    elif(n%i == 2):
        case1 = n-12
        i_cnt = case1//i
        j_cnt = (n-case1)//j
        solution(i_cnt, j_cnt)
    elif(n%i == j):
        print((n//i)+1)
    elif(n%i == 4): 
        case1 = n-9
        i_cnt = case1//i
        j_cnt = (n-case1)//j
        solution(i_cnt, j_cnt)
    else:
        print(-1)