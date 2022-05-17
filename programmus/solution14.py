import re

def solution(new_id):
    answer = ""
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)

    # 3단계
    new_id = re.sub(r"[.]{2}", ".", new_id)
    
    # 4단계
    new_id = new_id.strip(".")
        
    # 5단계
    if new_id == "":
        new_id = "a"
    
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[0:15]
    elif len(new_id) < 3:
        # 7단계
        if len(new_id) == 1:
            new_id = new_id+new_id+new_id
        elif len(new_id) == 2:
            new_id = new_id+new_id[1]
    new_id = new_id.strip(".")
    
    answer = new_id
    return answer

print(solution("...!@BaT#*....y.abcdefghijklm)"))