def solution(id_list, report, k):
    buffer = []
    answer = []
    reports = []
    user = {}
    count = {}
    for i in id_list:
        user[i] = []
        count[i] = 0
        
    for i in report:
        report = i.split(" ")
        user[report[0]].append(report[1])
        
    for i in user.values():
        for j in count.keys():
            if j in i:
                count[j] += 1
    
    # 정지먹은 사람이라면 buffer에 추가
    for idx, (key, value) in enumerate(count.items()):
        if k <= value:
            buffer.append(key)
    
    for i in user.values():
        cnt = 0
        for j in buffer:
            if j in i:
                cnt += 1
        answer.append(cnt)    
    return answer