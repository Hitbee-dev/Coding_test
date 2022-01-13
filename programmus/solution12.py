record = [
    "Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
    ]

result = [
    "Prodo님이 들어왔습니다.", 
    "Ryan님이 들어왔습니다.", 
    "Prodo님이 나갔습니다.", 
    "Prodo님이 들어왔습니다."
    ]

def solution(record):
    dic = {}
    arr = []
    result = []

    for i in record:
        state = i.split(" ")[0]
        uid = i.split(" ")[1]
        if state != "Leave":
            dic[uid] = i.split(" ")[2]

        if state == "Enter":
            arr.append(f"{uid}님이 들어왔습니다.")
        elif state == "Leave":
            arr.append(f"{uid}님이 나갔습니다.")
        else:
            pass

    for i in arr:
        for k, v in dic.items():
            if k in i:
                result.append(i.replace(k, v))
                print(k, v)
    # Change쪽에서 에러?
    # ID와 닉네임이 겹치는 경우 replace에서 섞일수있다..
solution(record)