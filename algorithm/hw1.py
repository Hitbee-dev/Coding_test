#입력 데이터 생성
#- 양의 정수 N, M을 입력 받는다.
#- 1) N은 각 입력의 데이터 개수 No. of integers in each test case input
#     2 <= N <= 10,000,000
#- 2) M은 생성할 테스트 케이스의 개수 No. of test case inputs to be generated
#     3 <= M <= nPn <= 1,000
#- M개의 테스트 입력을 생성한다. generate M test case inputs
#- 1) 각 테스트 케이스에는 1, 2,... ,N이 저장된다.
#     Each test case includes N integers: 1, 2,... ,(N-1)
import random

input_n, input_m = map(int, input("N M = ").split()) #N M = {} {} 입력받기
print("") #공백

def make_data(n, m): #입력 데이터 생성 함수
    arr_m = []
    while(len(arr_m) < m):
        arr_n = []
        while(len(arr_n) < n):
            random_num = random.randint(1, n)
            if random_num not in arr_n:
                arr_n.append(random_num)
        arr_m.append(arr_n)
    return arr_m

def convert_string(convert_integer): #출력될 문자열
    buffer_string = [str(integer) for integer in convert_integer]
    return " ".join(buffer_string)

make_datas = make_data(input_n, input_m)
if(input_n <= 10 and input_m <= 10):
    for i in range(input_m):
        if(i == 0):
            make_datas[i].sort()
            print(f"T{i}: {convert_string(make_datas[i])}")
        elif(i == 1):
            make_datas[i].sort(reverse = True)
            print(f"T{i}: {convert_string(make_datas[i])}")
        else:
            print(f"T{i}: {convert_string(make_datas[i])}")
else:
    print(f"{input_m} test case inputs generated.")
    print(f"{input_n} integers in each test case.")