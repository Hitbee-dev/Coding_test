import random
import time
import math
def bubble_sort(list,N,M,num):
    if (N <= 10 and M <= 10):
        print("[T"+str(num)+"] <bublle sort>")
        print("L0: "+" ".join(list))
        for i in range(N-1):
            for j in range(N-i-1):
                if(int(list[j])>int(list[j+1])):
                    list[j],list[j+1] = list[j+1],list[j]
            print("L"+str(i+1)+": "+" ".join(list))
    else:
        print("<bublle sort>")
        time_temp = []
        for k in range(len(list)):
            start = time.time()
            for i in range(N - 1):
                for j in range(N - i - 1):
                    if (int(list[k][j]) > int(list[k][j + 1])):
                        list[k][j], list[k][j + 1] = list[k][j + 1], list[k][j]
            end = time.time()
            time_temp.append(end-start)
        print("Best : ",round(min(time_temp),5),"milliseconds")
        print("Worst : ", round(max(time_temp),5), "milliseconds")
        print("Average : ", round(sum(time_temp)/len(time_temp),5), "milliseconds")
def selection_sort(list,N,M,num):
    if (N <= 10 and M <= 10):
        print("[T" + str(num) + "] <selection sort>")
        print("L0: " + " ".join(list))
        for i in range(N-1):
            min_idx = i
            for j in range(i+1, N):
                if(int(list[min_idx])>int(list[j])):
                    min_idx = j
            list[i],list[min_idx] = list[min_idx], list[i]
            print("L"+str(i+1)+": "+" ".join(list))
    else:
        print("<selection sort>")
        time_temp = []
        for k in range(len(list)):
            start = time.time()
            for i in range(N - 1):
                min_idx = i
                for j in range(i + 1, N):
                    if (int(list[k][min_idx]) > int(list[k][j])):
                        min_idx = j
                list[k][i], list[k][min_idx] = list[k][min_idx], list[k][i]
            end = time.time()
            time_temp.append(end - start)
        print("Best : ", round(min(time_temp), 5), "milliseconds")
        print("Worst : ", round(max(time_temp), 5), "milliseconds")
        print("Average : ", round(sum(time_temp) / len(time_temp), 5), "milliseconds")

def insert_sort(list,N,M,num):
    if (N <= 10 and M <= 10):
        print("[T" + str(num) + "] <selection sort>")
        print("L0: " + " ".join(list))
        for i in range(1, N):
            for j in range(i,0,-1):
                if(int(list[j-1])>int(list[j])):
                    list[j], list[j-1] = list[j-1],list[j]
            print("L"+str(i)+": "+" ".join(list))
    else:
        print("<insert sort>")
        time_temp = []
        for k in range(len(list)):
            start = time.time()
            for i in range(1, N):
                for j in range(i, 0, -1):
                    if (int(list[k][j - 1]) > int(list[k][j])):
                        list[k][j], list[k][j - 1] = list[k][j - 1], list[k][j]
            end = time.time()
            time_temp.append(end - start)
        print("Best : ", round(min(time_temp), 5), "milliseconds")
        print("Worst : ", round(max(time_temp), 5), "milliseconds")
        print("Average : ", round(sum(time_temp) / len(time_temp), 5), "milliseconds")
def create_date():
    N,M = map(int,input("N, M: ").split())
    if(N<=10 and M<=10):
        arr = []
        sel_arr = []
        while len(arr) <N:
            num = str(random.randint(1,N))
            if num not in arr:
                arr.append(str(num))
        for i in range(M):
            if(i==0):
                sel_arr.append(sorted(arr))
                print("T"+str(i)+": "+" ".join(sorted(arr)))
            elif(i==1):
                sel_arr.append(sorted(arr,reverse=True))
                print("T"+str(i)+": "+" ".join(sorted(arr,reverse=True)))
            #elif(i==2):
            #    arr = ['1','5','2','4','3']
            #    sel_arr.append(arr)
            #    print("T" + str(i) + ": " + " ".join(sel_arr[i]))
            else:
                sel_arr.append(random.sample(arr,len(arr)))
                print("T" + str(i) + ": " + " ".join(sel_arr[i]))
        sel_num = int(input("T 선택: "))
        return sel_arr[sel_num], N, M, sel_num
    else:
        arr2 = []
        sel_arr2 =[]
        while len(arr2) <N:
            num = str(random.randint(1,N))
            if num not in arr2:
                arr2.append(str(num))
        for i in range(M):
            if(i==0):
                sel_arr2.append(sorted(arr2))
            elif(i==1):
                sel_arr2.append(sorted(arr2,reverse=True))
            else:
                sel_arr2.append(random.sample(arr2,len(arr2)))
        print(M,"test case inputs generated.")
        print(N,"integers in each test case.")
        return sel_arr2, N, M, -1

data, n, m, num = create_date()

bubble_data = data[:]
selection_data = data[:]
insert_data = data[:]

bubble_sort(bubble_data, n, m, num)
selection_sort(selection_data, n, m, num)
insert_sort(insert_data, n, m, num)
