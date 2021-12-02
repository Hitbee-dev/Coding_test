# Test Case
phone_book = [
    ["119", "97674223", "1195524421"], 
    ["123","456","789"], 
    ["12","123","1235","567","88"]
    ]

# 1번째 풀이방법
# def solution(phone_book):
#     data = phone_book[0]
#     arr = len(phone_book)
#     for i in range(1, arr):
#         cnt = 0
#         lens = len(phone_book[0])
#         for j in range(len(phone_book[i])-lens+1):
#             if phone_book[i][cnt:lens] == data:
#                 return False
#             elif len(data) != (lens-cnt):
#                 break
#             cnt += 1
#             lens += 1
#     return True

# 채점 결과
# 정확성: 50.0
# 효율성: 4.2
# 합계: 54.2 / 100.0

# 2번째 풀이방법
# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if phone_book[i] in phone_book[i+1]:
#             return False
#     return True

# 채점 결과
# 정확성: 79.2
# 효율성: 16.7
# 합계: 95.8 / 100.0

# 3번째 풀이방법
# def solution(phone_book):
#     data = phone_book[0]
#     for i in range(1, len(phone_book)):
#         if data == phone_book[i][:len(data)]:
#             return False
#     return True

# 채점 결과
# 정확성: 62.5
# 효율성: 4.2
# 합계: 66.7 / 100.0

# 4번째 풀이방법
# def solution(phone_book):
#     phone_book.sort()
#     data = phone_book[0]
#     for i in range(1, len(phone_book)):
#         if data == phone_book[i][:len(data)]:
#             return False
#     return True

# 채점 결과
# 정확성: 70.8
# 효율성: 12.5
# 합계: 83.3 / 100.0

# 5번째 풀이방법
# def solution(phone_book):
#     data = hash(phone_book[0])
#     for i in range(1, len(phone_book)):
#         if(data == hash(phone_book[i][:len(phone_book[0])])):
#             return False
#     return True

# 채점 결과
# 정확성: 62.5
# 효율성: 4.2
# 합계: 66.7 / 100.0

# 6번째 풀이방법
# def solution(phone_book):
#     phone_book.sort()
#     data = hash(phone_book[0])
#     for i in range(1, len(phone_book)):
#         if(data == hash(phone_book[i][:len(phone_book[0])])):
#             return False
#     return True

# 채점 결과
# 정확성: 70.8
# 효율성: 12.5
# 합계: 83.3 / 100.0

# 7번째 풀이방법
# def solution(phone_book):
#     phone_book.sort(key=len)
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 return False
#     return True

# 채점 결과
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0

# 8번째 풀이방법
def solution(phone_book):
    dic = {}
    phone_book.sort()
    dic[phone_book[0]] = 1
    for i in range(1, len(phone_book)):
        if len(phone_book[i-1]) < len(phone_book[i]):
            if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
                return False
        elif len(phone_book[i-1]) > len(phone_book[i]):
            if phone_book[i] == phone_book[i-1][:len(phone_book[i])]:
                return False
    print(dic)
    
    return True
        
for i in range(len(phone_book)):
    print(solution(phone_book[i]))