from maze import Maze
from collections import deque

# TODO: 1x1에서 동작 안 하는 버그가 있음

def shortest_path_length_opt(maze):
    que = deque([(maze.start_row, maze.start_col, 0)])
    visited = {(maze.start_row, maze.start_col)}
    while que:
        x, y, plen = que.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) == (maze.end_row, maze.end_col):
                return plen + 1

            if not maze.in_range(nx, ny) or \
                    not maze.is_empty(nx, ny) or \
                    (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            que.append((nx, ny, plen + 1))

    return -1


def shortest_path_opt(maze):
    initial_path = [(maze.start_row, maze.start_col)]
    que = deque([initial_path])
    visited = {initial_path[0]}
    while que:
        path = que.popleft()
        x, y = path[-1]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            npath = path + [(nx, ny)]

            if (nx, ny) == (maze.end_row, maze.end_col):
                return npath

            if not maze.in_range(nx, ny) or \
                    not maze.is_empty(nx, ny) or \
                    (nx, ny) in visited:
                continue

            visited.add(npath[-1])
            que.append(npath)

    return []
