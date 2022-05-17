#어느 달력에서 토요일 날짜를 모두 더했더니 80이었다.
#이달 k일은 무슨 요일일까?

#입력 조건
#예외처리를 해야한다.
#이달 k일은 무슨요일인지 출력해야한다.

#출력 조건
#토요일 시작일: days
#k일: k
#월요일

weekdays = ["목", "금", "토", "일", "월", "화", "수"] #토요일이 2일이니, 0=목, 1=금, 2=토...Index지정

result = 0

days = int(input("토요일 시작일: "))
if not(days == 2):
    print("정답이 아닙니다.")

if(days==2):
    k = int(input("k일: "))
    result += days
    for i in range(4): #토요일은 5번 나와야 한다. 하지만 2일은 맨처음에 입력 해 주었으니, 4번만 더 반복
        if(k>7):
            k = k-7
        days += 7
        result += days

    print(f"{weekdays[k]}요일")