# T = "2"
# N = ["3", "4"]
# M = ["3 5 3", "3 7 5 8"]
# # for _ in range(int(T)-1):
# T = int(input())
# for _ in range(T):
#     cnt = 0
#     TN = int(input())
#     TM = list(map(int, input().split(" ")))
#     for i in range(len(TM)):
#         for j in range(len(TM)):
#             cnt += TM[i] % TM[j]
#
#     print(cnt)

T = "4"
N = ["1", "1", "4", "4"]
M = ["3", "2", "7 3 8 4", "7 4 8 4"]
def main():
    for _ in range(int(T)):
        cnt = 0
        flag = 0
        TN = int(N[_])
        TM = list(map(int, M[_].split(" ")))
        TM.extend([0, 0])
        print(TM)
        for i in range(TN-1):
            for j in range(i+1, TN):
                if TN < 3:
                    break
                else:
                    if i < j and i+1 == j:
                        print(TM[i], TM[j])
                        if TM[i] % 2 == 0 and TM[j] % 2 == 0:
                            print("둘 다 짝수")
                            if TM[i+1] % 2 == 0 and TM[j+1] % 2 == 0:
                                print("또 둘다 짝수 -1 반환필요")
                                if TN-1 != j:
                                    flag = -1
                            else:
                                cnt += 1
                        elif TM[i] % 2 == 1 and TM[j] % 2 == 1:
                            print("둘 다 홀수")
                            if TM[i+1] % 2 == 1 and TM[j+1] % 2 == 1:
                                print("또 둘다 홀수 -1 반환필요")
                                if TN-1 != j:
                                    flag = -1
                            else:
                                cnt += 1
                    # 0 1은 무시헤도 돼
        if flag == -1:
            print(f"#{_ + 1} {flag}")
        else:
            print(f"#{_+1} {cnt}")
if __name__ == "__main__":
    main()