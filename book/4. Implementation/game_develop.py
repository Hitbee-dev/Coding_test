# 게임 개발

""" 요약
    캐릭터는 동서남북 중 한 곳을 바라본다.
    맵의 각 칸은 (A, B)로 나타낼 수 있고,
    A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.(좌표)
    캐릭터는 동서남북으로 이동할 수 있고, 바다로 되어있는 공간에는 갈 수 없다.
    1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
    2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진한다.
    3. 왼쪽방향에 가보지않은 칸이 없다면 왼쪽방향으로 회전만 하고 다시 탐색한다.
    4. 만약 네 방향 모두 이미 가본 칸이거나, 바다로 되어있는 칸인 경우에는 바라보는 방향을 유지한 채로 한 칸 뒤로간다.
    5. 단, 이때 뒤쪽 방향이 바다인 칸이라면 움직임을 멈춘다.
    
    ※ 2번째 줄 0: 북쪽 | 1: 동쪽 | 2: 남쪽 | 3: 서쪽
    ※ 3번째 줄 0: 육지 | 1: 바다
    ※ 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
    캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
"""

# 입력 조건                                                 | 출력 조건
# 4 4      | 4 x 4 맵 생성                                  | 3
# 1 1 0    | (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
# 1 1 1 1  | 첫 줄은 모두 바다
# 1 0 0 1  | 둘째 줄은 바다/육지/육지/바다
# 1 1 0 1  | 셋째 줄은 바다/바다/육지/바다
# 1 1 1 1  | 마지막 줄도 모두 바다

position = list(map(int, input().split()))

def game(p):
    # 북 서 남 동
    see = [0, 1, 2, 3]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cp = list(map(int, input().split()))
    maps = []
    for _ in range(p):
        maps.append(list(map(int, input().split())))

    # 현재 위치
    x, y = cp[0], cp[1]

    # 보고있는 방향
    check = cp[2]
    sx, sy = x+dx[see[check]], y+dy[see[check]]

    cnt = 0
    flag = 0
    buffer = [str(x)+str(y)]
    while True:
        # 현재위치가 육지인지 바다인지(0: 육지 | 1: 바다)
        rp = maps[x][y]
        print(f"현재 좌표: {x}, {y} | 현재위치: {rp}")

        # 보고있는 위치가 육지인지 바다인지(0: 육지 | 1: 바다)
        mp = maps[sx][sy]
        print(f"보고있는 좌표: {sx}, {sy} | 보고있는 위치: {mp}")

        # 만약 보고있는 위치가 육지라면
        if mp == 0:
            # 만약 지나온 길이라면
            if str(sx)+str(sy) in buffer:
                flag += 1
                # 만약 동서남북을 다 둘러봤는데 이동할 수 있는곳이 없다면
                if flag == 4:
                    cnt += 1
                    flag = 0
                    # 만약 뒤로 한번 이동했는데도 이동할 수 있는곳이 없다면
                    if cnt == 2:
                        break
                    # 보고있는 방향으로 뒤로 한칸 이동
                    else:
                        check += 1
                        if check == 4:
                            check = 0
                        elif check == 5:
                            check = 1
                        print(check)
                        sx, sy = x+dx[see[check]], y+dy[see[check]]
                        print(f"막다른 길 이므로 {dx[see[check]]}, {dy[see[check]]}만큼 회전하고 {sx}, {sy}를 바라보겠습니다.")
                else:
                    check += 1
                    if check == 4:
                        check = 0
                    elif check == 5:
                        check = 1
                    print(check)
                    sx, sy = x+dx[see[check]], y+dy[see[check]]
                    print(f"들렸던 곳 이므로 {dx[see[check]]}, {dy[see[check]]}만큼 회전하고 {sx}, {sy}를 바라보겠습니다.")
                
            # 만약 지나온길이 아니라면
            else:
                flag = 0
                x, y = sx, sy
                sx, sy = x+dx[see[check]], y+dy[see[check]]
                print(f"육지이므로 {x}, {y}로 이동하고 {sx}, {sy}를 바라보고있습니다.")
                buffer.append(str(x)+str(y))
                print(buffer)
                cnt = 0
        
        # 만약 보고있는 위치가 바다라면
        else:
            flag += 1
            if flag == 4:
                cnt += 1
                flag = 0
                # 만약 뒤로 한번 이동했는데도 이동할 수 있는곳이 없다면
                if cnt == 2:
                    break
                # 보고있는 방향으로 뒤로 한칸 이동
                else:
                    check += 1
                    if check == 4:
                        check = 0
                    elif check == 5:
                        check = 1
                    print(check)
                    bfx, bfy = sx, sy
                    sx, sy = x+dx[see[check]], y+dy[see[check]]
                    print(f"막다른 길 이므로 {dx[see[check]]}, {dy[see[check]]}만큼 회전하고 {sx}, {sy}를 바라보겠습니다.")
                    x, y = x-dx[see[check]], y-dy[see[check]]
                    sx, sy = bfx, bfy
                    print(f"막다른 길 이므로 {x}, {y}로 이동하고, {sx}, {sy}를 바라보겠습니다.")
            else:
                check += 1
                if check == 4:
                    check = 0
                elif check == 5:
                    check = 1
                print(check)
                sx, sy = x+dx[see[check]], y+dy[see[check]]
                print(f"바다 이므로 {dx[see[check]]}, {dy[see[check]]}만큼 회전하고 {sx}, {sy}를 바라보겠습니다.")

        print()
        print("===============================")

    return len(buffer)

print(game(position[0]))