testcase = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

def solution(s):
    arr = []
    cnt_arr = []
    result = []
    final = []
    answer = ""
    start = 0
    end = 1
    cnt = 1
    for i in range(1, len(s)): # 문자열 슬라이싱
        for _ in range(len(s)):
            if len(s[start:end]) != 0 and len(s[start:end]) >= i:
                arr.append(s[start:end])
            start = end
            end = start+i
        start = 0
        end = i+1
        result.append(arr)
        arr = []
    # print(result)

    for data in result:
        for i in range(len(data)-1):
            if data[i] == data[i+1]: # 앞의 원소와 뒤의 원소가 같다면
                cnt += 1 # cnt += 1
            else: # 앞의 원소와 뒤의 원소가 같지 않다면
                if cnt == 1: # 같은 원소가 없었다면
                    cnt_arr.append(data[i])
                else: # 같은 원소가 있었다면
                    cnt_arr.append(cnt)
                    cnt_arr.append(data[i])
                    cnt = 1
        
        if cnt != 1:
            cnt_arr.append(cnt)
            cnt_arr.append(data[i])
        else:
            cnt_arr.append(s.split(data[i])[-1])

        # 문자열의 갯수를 final 리스트 변수에 저장
        # print(cnt_arr)
        if len(data) == 1:
            cnt_arr=''.join(result[i])
            final.append(len(cnt_arr))
            # print(final)
        elif cnt_arr[-2] != 1:
            answer=''.join(str(_) for _ in cnt_arr)
            if len(answer) < len(s)//2+1:
                final.append(len(s))
            else:
                final.append(len(answer))
                # print(final)
        else:
            final.append(len(s))
            # print(final)
        cnt = 1
        cnt_arr = []
        answer = ""
    return min(final)
    # print(min(final))
    # print("==========================")

for _ in testcase:
    print(solution(_))