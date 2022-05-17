# 아래와 같은 리스트(배열)이 주어질 때 map()을 사용해서 아래 함수를 매핑해보자.

def map(dic):
    for i in dic:
        dic[i] = 2*(i**2) + 5*i - 20

    return dic
result = 0
dic = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
}
print(map(dic))