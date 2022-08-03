def solution(name):
    # 아스키코드 값을 숫자로 변경 (A = 0, Z = 25)
    result = [ord(i)-65 for i in name]
    print(result)

    # 0이 시작되는 부분 ~ 끝나는 부분들 찾기
    se_flag = False
    start_zero = []
    end_zero = []

    for idx, i in enumerate(result):
        if se_flag == False and i == 0:
            se_flag = True
            start_zero.append(idx)
        elif se_flag == True and i != 0:
            se_flag = False
            end_zero.append(idx-1)
    print(start_zero, end_zero)

    # 거꾸로도 저장하기
    bse_flag = False
    bstart_zero = []
    bend_zero = []
    for idx, i in enumerate(reversed(result)):
        if bse_flag == False and i == 0:
            bse_flag = True
            bstart_zero.append(idx)
        elif bse_flag == True and i != 0:
            bse_flag = False
            bend_zero.append(idx-1)
    print(bstart_zero, bend_zero)

    # 만약, A로 끝나서 마지막 값이 들어가지 않았다면 마지막 인덱스 추가
    if len(start_zero) != len(end_zero):
        end_zero.append(len(result))
    print(start_zero, end_zero)

    # 거꾸로도 저장
    if len(bstart_zero) != len(bend_zero):
        bend_zero.append(len(result))
    print(bstart_zero, bend_zero)

    # 시작값과 끝값을 묶기
    branch = []
    for pair in zip(start_zero, end_zero):
        branch.append(pair)

    # 만약 0이 하나도 나오지 않았다면
    if branch == []:
        branch.append((21, 21))

    # 시작값과 끝값을 묶기
    bbranch = []
    for pair in zip(bstart_zero, bend_zero):
        bbranch.append(pair)

    # 만약 0이 하나도 나오지 않았다면
    # if branch == []:
    branch.append((21, 21))

    # 계산
    answer = []
    for s, e in branch:
        print("===============================")
        print(s,e)
        count = 0
        flager = False

        for idx, i in enumerate(result):
            #만약 0이 있는 범위라면 A개수 만큼 패스
            if idx == 0 and s == 0:
                count += 1
                print("pass")
                continue
            if idx >= s and idx <= e:
                if flager == False:
                    flager = True
                    if e == len(result):
                        break
                    count += idx-1
                print("pass")
                continue
            if 13 > i:
                count += i
            else:
                count += (26-i)
            count += 1
            print(count)

        count -= 1
        answer.append(count)
    print(answer)
    print(min(answer))

    for s, e in bbranch:
        print("===============================")
        print(s, e)
        count = 1
        flager = False

        for idx, i in enumerate(reversed(result)):
            #만약 0이 있는 범위라면 A개수 만큼 패스
            if idx == 0 and s == 0:
                count += 1
                print("pass")
                continue
            if idx >= s and idx <= e:
                if flager == False:
                    flager = True
                    if e == len(result):
                        break
                    count += idx-1
                print("pass")
                continue
            if 13 > i:
                count += i
            else:
                count += (26-i)
            count += 1
            print(count)

        count -= 1
        answer.append(count)
    print(answer)
    return min(answer)