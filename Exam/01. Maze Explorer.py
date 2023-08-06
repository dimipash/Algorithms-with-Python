from collections import deque


def find_shortest_path(maze, n):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    queue = deque([(0, 0, 0)])
    visited = set([(0, 0)])

    while queue:
        i, j, d = queue.popleft()

        if maze[i][j] == 'E':
            return d

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != '#' and (ni, nj) not in visited:
                queue.append((ni, nj, d + 1))
                visited.add((ni, nj))

    return -1


n = int(input())
if n <= 20:
    maze = [input() for _ in range(n)]
    print(find_shortest_path(maze, n))

