#정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
#예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
# - 00시00분03초
# - 00시13분30초
#반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각이다.
# - 00시02분55초
# - 01시27분45초

#입력 조건
# - 첫째줄에 정수 N이 입력된다. (0 <= N <= 23)

#출력 조건
# - 00시00분00초부터 N시59분59초까지의 모든 시각중에서 3이하나라도 포함되는 모든 경우의 수를 출력한다.

#입력 예시
#5

#출력 예시
#11475

#시 = 24
#분 = 60
#초 = 60

#경우의 수는 24*60*60 = 86400가지

n = int(input("몇시59분59초까지 3이 하나라도 포함되는 경우의수를 찾을까요?: "))
count = 0

for i in range((n+1)):
    for j in range(60):
        for k in range(60):
            if "3" in str(i)+str(j)+str(k):
                count += 1
print(count)