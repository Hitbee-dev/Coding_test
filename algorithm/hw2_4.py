# 4) 화살과 과녁의 거리

# 화살과 과녁의 거리가 절반씩 줄어든다고 생각하면 화살은 영원히 과녁에 다가간다.
# - 거리가 0.01보다 작아지면 과녁에 맞은 것으로 해 두자.
# - 이 함수가 <거리가 절반으로 감소한 횟수> 를 리턴하도록 수정 해 보자.
# - 이 함수를 반복문으로 바꿔보자: shooting_iter() 작성

# # Original Code
# def shooting_rec(distance_left):
#     if distance_left < 0.01:
#         return "shoot!"

#     print(distance_left)
#     return shooting_rec(distance_left/2.0)
# print(shooting_rec(100))

# 4-1) <거리가 절반으로 감소한 횟수>
def shooting_rec(distance_left):
    global counter
    counter += 1
    if distance_left < 0.01:
        print("shoot!")
        return counter

    # print(distance_left)
    return shooting_rec(distance_left/2.0)
counter = 0

# 4-2) 반복분으로 바꾼 함수
def shooting_iter(distance_left):
    counter = 1
    while distance_left > 0.01:
        counter += 1
        # print(distance_left)
        distance_left = distance_left/2.0
    return counter

# Test Code
def compare(func1, func2, n):
    ret1 = func1(n)
    ret2 = func2(n)

    print(f"{func1.__name__}=>{ret1}")
    print(f"{func2.__name__}=>{ret2}")
    print(f"equal?={ret1 == ret2}")
    print()
compare(shooting_rec, shooting_iter, 1012414312)