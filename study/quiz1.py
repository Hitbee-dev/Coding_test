#어느 달력에서 토요일 날짜를 모두 더했더니 80이었다.
#이달 13일은 무슨 요일일까?

#토요일이 2일부터 시작되어야 함
#토요일이 5번 나와야 한다.
#예외처리를 해야한다.
#이달 k일은 무슨요일인지 출력해야한다.

weekdays = ["목", "금", "토", "일", "월", "화", "수"] #토요일이 2일이니, 0=목, 1=금, 2=토...Index지정

result = 0

days = int(input("토요일은 몇일부터 시작되야 할까?: "))
if not(days == 2):
    print("정답이 아닙니다.")

if(days==2):
    k = int(input("k일은 무슨 요일인가?: "))
    print(f"days: 1주차 {days}일") #입력한 날짜
    result += days
    for i in range(4): #토요일은 5번 나와야 한다. 하지만 2일은 맨처음에 입력 해 주었으니, 4번만 더 반복
        if(k>7):
            k = k-7
        days += 7
        result += days
        print(f"days: {i+2}주차 {days}일") #날짜
        print(f"result: {result}") #토요일을 모두 더했을 때의 값

    print(f"요일: {weekdays[k]}")