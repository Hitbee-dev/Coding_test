import math

def squared(list, num):
    return list[num]*list[num]
cnt = 0
while True:
    data = list(map(int, input().split()))
    if(data[0] == data[1] == data[2] == 0):
        break
    else:
        cnt += 1
        print(f"Triangle #{cnt}")
        if(data.index(-1) == 2):
            try:
                print(f"c = {math.sqrt(squared(data, 0)+squared(data, 1)):0.3f}")
            except:
                print("Impossible.")
        elif(data[0]>=data[2] or data[1]>=data[2]):
            print("Impossible.")
        elif(data.index(-1) == 0):
            try:
                print(f"a = {math.sqrt(squared(data, 2)-squared(data, 1)):0.3f}")
            except:
                print("Impossible.")
        elif(data.index(-1) == 1):
            try:
                print(f"b = {math.sqrt(squared(data, 2)-squared(data, 0)):0.3f}")
            except:
                print("Impossible.")


        print()