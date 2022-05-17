tc = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
ra = [7, 9, 8, 14, 17]

def solution(s):
    if len(s) == 1:
        return 1
    result = ""
    answer = 1001
    for i in range(1, len(s)//2+1):
        start = 0
        end = i
        cnt = 1
        buf_num = []
        buf_str = []
        for _ in range(len(s)//i+1):
            if s[start:end] == "":
                break
            if s[start:end] == s[end:end+i]:
                cnt += 1
            else:
                buf_num.append(str(cnt))
                buf_str.append(s[start:end])
                cnt = 1
            start = end
            end = end+i

        for j in range(len(buf_num)):
            if buf_num[j] != "1":
                result += buf_num[j]+buf_str[j]
            else:
                result += buf_str[j]
        if answer > len(result):
            answer = len(result)
        result = ""
    # print(answer)
    return answer
        
for i in range(len(tc)):
    if solution(tc[i]) == ra[i]:
        print(f"#{i+1} True")
    else:
        print(f"#{i+1} False")