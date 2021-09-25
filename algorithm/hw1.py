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

def bubble_sort(data): #버블 정렬
    print("") # 공백
    print("[T2] <bubble sort>")
    print(f"L0: {convert_string(data)}")
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if(data[j] > data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
        print(f"L{i+1}: {convert_string(data)}")

def selection_sort(data): #선택 정렬
    print("")  # 공백
    print("[T2] <selection sort>")
    print(f"L0: {convert_string(data)}")
    for i in range(0, len(data)-1):
        buffer = i
        for j in range(i+1, len(data)):
            if(data[buffer] > data[j]):
                buffer = j
        data[i], data[buffer] = data[buffer], data[i]
        print(f"L{i+1}: {convert_string(data)}")

def insertion_sort(data): #삽입 정렬
    print("")  # 공백
    print("[T2] <insertion sort>")
    print(f"L0: {convert_string(data)}")
    for i in range(1, len(data)):
        buffer = data[i]
        j = i-1
        while j >= 0 and data[j] > buffer:
            data[j+1] = data[j]
            j = j-1
        data[j+1] = buffer
        print(f"L{i+1}: {convert_string(data)}")

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
    bubble_sort(make_datas[2][:])  #버블 정렬 결과 출력
    selection_sort(make_datas[2][:])  #선택 정렬 결과 출력
    insertion_sort(make_datas[2][:])  #삽입 정렬 결과 출력

else:
    for i in range(input_m):
        if(i == 0):
            make_datas[i].sort()
        elif(i == 1):
            make_datas[i].sort(reverse=True)
    print(f"{input_m} test case inputs generated.")
    print(f"{input_n} integers in each test case.")


