import random
import time

#Fuc
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

def titles(name, data): #반복코드 함수화
    if(input_n <= 10 and input_m <= 10):
        print("")  # 공백
        print(f"[T2] <{name} sort>")
        print(f"L0: {convert_string(data)}")

def bubble_sort(data): #버블 정렬
    titles("bubble", data)

    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if(data[j] > data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
        if(input_n <= 10 and input_m <= 10):
            print(f"L{i+1}: {convert_string(data)}")

def selection_sort(data): #선택 정렬
    titles("selection", data)
    
    for i in range(len(data)-1):
        min_data = i
        for j in range(i+1, len(data)):
            if(data[min_data] > data[j]):
                min_data = j
        data[i], data[min_data] = data[min_data], data[i]
        if(input_n <= 10 and input_m <= 10):
            print(f"L{i+1}: {convert_string(data)}")

def insertion_sort(data): #삽입 정렬
    titles("insertion", data)
    
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]

        if(input_n <= 10 and input_m <= 10):
            print(f"L{i+1}: {convert_string(data)}")

def setTime(names, times): #수행시간 출력
    print("")
    print(f"<{names} sort>")
    print(f"Best    : {min(times)*1000: .5f} milliseconds")
    print(f"Worst   : {max(times)*1000: .5f} milliseconds")
    print(f"Average : {(sum(times)*1000)/len(times): .5f} milliseconds")

#Main
input_n, input_m = map(int, input("N M = ").split())  # N M = {} {} 입력받기
print("")  # 공백

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
    bubble_sort(make_datas[2][:])  # 버블 정렬 결과 출력
    selection_sort(make_datas[2][:])  # 선택 정렬 결과 출력
    insertion_sort(make_datas[2][:])  # 삽입 정렬 결과 출력

else:
    names = ["bubble", "selection", "insertion"]

    for i in range(input_m):
        if(i == 0):
            make_datas[i].sort()
        elif(i == 1):
            make_datas[i].sort(reverse=True)
    print(f"{input_m} test case inputs generated.")
    print(f"{input_n} integers in each test case.")

    for k in range(len(names)):
        functions = [bubble_sort, selection_sort, insertion_sort]
        times = []
        for cnt in range(len(make_datas)): # 버블, 선택, 삽입 정렬 순으로 출력
            start = time.time()
            functions[k](make_datas[cnt][:]) 
            end = time.time()
            times.append(end-start)
        setTime(names[k], times)