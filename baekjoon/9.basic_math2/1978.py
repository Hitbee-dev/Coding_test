#에라토스테네스의 체

import math
num_count = int(input())
num_list = list(map(int, input().split(' ')))
natural_num = list(range(2, 1001))
count = 0

if len(num_list) == num_count:
    for i in range(2, math.ceil(math.sqrt(1000))):
        for j in natural_num:
            if j / i == 1:                             
                pass
            elif j % i == 0:               
                natural_num.remove(j)           
for k in num_list:
    if k in natural_num:                       
        count += 1
print(count)