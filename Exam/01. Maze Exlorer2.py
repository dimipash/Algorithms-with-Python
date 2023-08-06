def shortest_path(maze):
    queue = [(0, 0, 0)]
    visited = set()
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while queue:
        row, col, steps = queue.pop(0)
        if (row, col) == (len(maze) - 1, len(maze) - 1):
            return steps
        for x, y in directions:
            new_row, new_col = row + x, col + y
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze) and maze[new_row][new_col] != '#' and (
            new_row, new_col) not in visited:
                queue.append((new_row, new_col, steps + 1))
                visited.add((new_row, new_col))
    return -1


n = int(input())
if n <= 20:
    maze = [input() for _ in range(n)]
    print(shortest_path(maze))
