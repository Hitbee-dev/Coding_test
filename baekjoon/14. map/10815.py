get_num = int(input())
get_card = list(map(int, input().split()))
compare_num = int(input())
compare_card = list(map(int, input().split()))
result = [x*0 for x in range(compare_num)]

for i in range(get_num):
    if get_card[i] in compare_card:
        result[compare_card.index(get_card[i])] = 1
print(result)