# 3) List Concatenation(리스트 연결)

# 두 배열 left, right가 주어지면 right의 원소들을 left에 추가하는 함수이다.
# - 앞에서와 같이 concat_rec()을 작성해보자.
# - 처음에 주어진 left, right 객체의 내용이 변하지 않도록 할 것
# - 처음에 주어진 left, right 객체의 내용이 변하는 경우 2점 중 1점만 부여

# Original Code
def concat(left, right): # left, right 각각 리스트를 받아옴
    result = left[:] # result에 left인덱스 전체를 넣음
    for x in right: # right 리스트 안의 값을 하나씩 꺼내옴
        result.append(x) # result에 right 리스트를 추가함
    return result # 다 끝나면 출력

# Revursive Code
def concat_rec(left, right):
    result = left[:]
    if right == []:
        return result
    else:
        result.append(right[0])
        return concat_rec(result, right[1:])

# Test Code
def compare(func1, func2, n, m):
    ret1 = func1(n, m)
    ret2 = func2(n, m)

    print(f"{func1.__name__}=>{ret1}")
    print(f"{func2.__name__}=>{ret2}")
    print(f"equal?={ret1 == ret2}")
    print()
compare(concat, concat_rec, [1,2,3,4], [1,5,2,3,5,1,2,3,1,4,3,4,8])