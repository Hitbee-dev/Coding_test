# 1) 원소 찾기
def exists_in_rec(arr, target):
    if arr == []:
        return False
    elif arr[-1] == target:
        return True
    else:
        return exists_in_rec(arr[:-1], target)

# 2) n부터 m까지의 합
def sum_n_to_m_rec(n, m):
    if n == m:
        return n
    else:
        return sum_n_to_m_rec(n, m-1)+m

# 3) List Concatenation
def concat_rec(left, right):
    result = left[:]
    if right == []:
        return result
    else:
        result.append(right[0])
        return concat_rec(result, right[1:])

# 4-2에서 뜻하는 "이 함수"가 교수님께서 올려주신 재귀함수인지,
# 횟수를 세는 함수로 바꾼 함수인지 헷갈려서 4-2_1, 4-2_2 두개로 나누어 작성하였습니다.

# 4-1) <거리가 절반으로 감소한 횟수>
def shooting_rec(distance_left):
    result = []
    if not (isinstance(distance_left,list)):
        result.append(distance_left)
    else:
        result = distance_left
    if result[-1] < 0.01:
        print("shoot!")
        return len(result)
    temp = result[-1]/2.0
    result.append(temp)
    return shooting_rec(result)

# 4-2_1) Original Code를 반복문으로 바꾼 함수
def shooting_iter_origin(distance_left):
    while distance_left > 0.01:
        print(distance_left)
        distance_left = distance_left/2.0
    return distance_left

# 4-2_2) <거리가 절반으로 감소한 횟수>를 반복분으로 바꾼 함수
def shooting_iter(distance_left):
    counter = 1
    while distance_left > 0.01:
        counter += 1
        distance_left = distance_left/2.0
    return counter