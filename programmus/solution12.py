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
    data = []
    for i in record:
        data.append(i.split(" "))
    
    print(data)

    for i in range(len(record)):
        if "Enter" in record[i]: #만약 들어왔다면
            if f"Change {data[i][1]}" in  

    for j in record:
        if "Change uid4567" in j:
            print("ok uid")

solution(record)