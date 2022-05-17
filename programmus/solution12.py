'''
    오픈 채팅방을 개설한 사람을 위해 다양한 사람들이 들어오고 나가는 것을 지켜볼 수 있는 관리자 창을 만드는 것이 목적
'''

def solution(record):
    uid = {}
    state = []
    answer = []
    
    for i in record:
        state.append(i.split(" "))
    
    for i in state:
        if i[0] != "Leave":
            uid[i[1]] = i[2]
        
    for idx, i in enumerate(state):
        if i[0] == "Enter":
            answer.append(f"{uid[i[1]]}님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(f"{uid[i[1]]}님이 나갔습니다.")
    return answer