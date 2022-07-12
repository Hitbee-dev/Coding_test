# Solution1

# get_num = int(input())
# get_card = list(map(int, input().split()))
# compare_num = int(input())
# compare_card = list(map(int, input().split()))
# result = [x*0 for x in range(compare_num)]

# for i in range(get_num):
#     if get_card[i] in compare_card:
#         result[compare_card.index(get_card[i])] = 1
# print(result)

# Solutuon2

# value1 = int(input())
# N = list(map(int, input().split()))
# value2 = int(input())
# M = list(map(int, input().split()))
# for i in M:
#     if i in N:
#         print(1, end = " ")
#     else:
#         print(0, end = " ")

# Solutuon3

value1 = int(input())
N = set(map(int, input().split()))
value2 = int(input())
for i in map(int, input().split()):
    if i in N:
        print(1, end = " ")
    else:
        print(0, end = " ")