def dfs(node, graph, viisited):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)


nodes = int(input())
edges = int(input())
graph = {node: [] for node in range(1, nodes + 1)}

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())

visited = set()

dfs(start_node, graph, visited)

unreachable_nodes = []
for node in graph.keys():
    if node not in visited:
        unreachable_nodes.append(node)

print(*sorted(unreachable_nodes), sep=' ')