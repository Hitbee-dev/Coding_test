t = int(input()) # TestCase의 갯수


def recursive(data, sum_data):
    result = []
    if(len(data) == 1): # 만약 데이터가 1개 남았다면
        return sum_data  # 바로 값 리턴
    elif(len(data)%2 == 0): #만약 데이터 갯수가 짝수라면
        for x in range(0, len(data)-1, 2): # 0+1, 2+3 ... 짝수단위로 데이터를 2개씩 증가시켜야함
            result.append(data[x]+data[x+1]) # 0+1 / 2+3
            sum_data += data[x]+data[x+1]
        print(result)
        print(sum_data)
        recursive(result, sum_data)
    else: #만약 데이터 갯수가 홀수라면
        
        for x in range(0, len(data)-1, 2):  # 1+2, 3+4 ... 홀단위로 데이터를 2개씩 증가시켜야함
            result.append(data[x]+data[x+1]) # 0+1 / 2+3
            sum_data += data[x]+data[x+1]
        result.append(data[-1])
        print(result)
        print(sum_data)
        recursive(result, sum_data)
    

while t!=0:
    sum_data = 0
    len_k = int(input()) # k의 갯수
    k = list(map(int, input().split())) # k값 받아오기
    k.sort() # 순서대로 정렬
    
    print(recursive(k, sum_data))
    t -= 1
