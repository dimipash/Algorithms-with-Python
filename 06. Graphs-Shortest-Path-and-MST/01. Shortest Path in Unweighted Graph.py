from collections import deque


def find_parent_by_node(graph, start_node, destination_node):
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    visited[start_node] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node == destination_node:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    return parent


def reconstruct_path(parent, destination_node):
    path = deque()
    node = destination_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return path


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

parent = find_parent_by_node(graph, start_node, destination_node)

path = reconstruct_path(parent, destination_node)

print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep=' ')
