import random
def bubble_sort(list,N,num):
    print("[T"+str(num)+"] <bublle sort>")
    print("L0: "+" ".join(list))
    for i in range(N-1):
        for j in range(N-i-1):
            if(int(list[j])>int(list[j+1])):
                list[j],list[j+1] = list[j+1],list[j]
        print("L"+str(i+1)+": "+" ".join(list))

def selection_sort(list,N,num):
    print("[T" + str(num) + "] <selection sort>")
    print("L0: " + " ".join(list))
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if(int(list[min_idx])>int(list[j])):
                min_idx = j
        list[i],list[min_idx] = list[min_idx], list[i]
        print("L"+str(i+1)+": "+" ".join(list))

def insert_sort(list,N,num):
    print("[T" + str(num) + "] <selection sort>")
    print("L0: " + " ".join(list))
    for i in range(1, N):
        for j in range(i,0,-1):
            if(int(list[j-1])>int(list[j])):
                list[j], list[j-1] = list[j-1],list[j]
        print("L"+str(i)+": "+" ".join(list))

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
        print(M,"test case inputs generated.")
        print(N,"integers in each test case.")

data, n, m, num = create_date()

bubble_data = data[:]
selection_data = data[:]
insert_data = data[:]

bubble_sort(bubble_data, n, num)
selection_sort(selection_data, n, num)
insert_sort(insert_data, n, num)
