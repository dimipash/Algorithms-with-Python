import heapq


def shortest_path(roads, closed, start, end):
    graph = {}

    for road in roads:
        city1, city2, distance = road.split(' - ')
        distance = int(distance)

        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}

        graph[city1][city2] = distance
        graph[city2][city1] = distance

    for closed_road in closed.split(','):
        city1, city2 = closed_road.split('-')
        if city1 in graph and city2 in graph:
            graph[city1].pop(city2, None)
            graph[city2].pop(city1, None)

    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, city, path = heapq.heappop(queue)

        if city == end:
            print(' - '.join(path + [city]))
            print(cost)
            return

        if city not in visited:
            visited.add(city)
            for neighbour, neighbour_cost in graph[city].items():
                new_cost = cost + neighbour_cost
                new_path = path + [city]
                heapq.heappush(queue, (new_cost, neighbour, new_path))


r = int(input())
roads = [input() for _ in range(r)]
closed = input()
start = input()
end = input()

shortest_path(roads, closed, start, end)