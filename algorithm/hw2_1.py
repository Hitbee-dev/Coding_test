# 1) 원소찾기

# Original Code
def exists_in(arr, target):
    for x in arr: # arr에 있는 값을 하나씩 가져온다.
        if x == target: # arr에 있는 값이 target과 같다면 True
            return True
    return False # 아니면 False반환

# Revursive Code
def exists_in_rec(arr, target):
    if arr == []:
        return False
    elif arr[-1] == target:
        return True
    else:
        return exists_in_rec(arr[:-1], target)

# Test Code
def compare(func1, func2, *args):
    ret1 = func1(*args)
    ret2 = func2(*args)

    print(f"{func1.__name__}=>{ret1}")
    print(f"{func2.__name__}=>{ret2}")
    print(f"equal?={ret1 == ret2}")
    print()
compare(exists_in, exists_in_rec, [1, 2, 3, 4, 5], 6)
