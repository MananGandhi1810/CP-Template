from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def find_girth(graph: Dict[int, List[int]]) -> int:
    girth = float("infinity")

    for start in graph:
        queue = deque([(start, start, 0)])
        visited = {start}
        parent = {start: start}

        while queue:
            vertex, prev, dist = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor == prev:
                    continue

                if neighbor in visited:
                    if neighbor != parent[vertex]:
                        cycle_length = dist + 1
                        girth = min(girth, cycle_length)
                else:
                    visited.add(neighbor)
                    parent[neighbor] = vertex
                    queue.append((neighbor, vertex, dist + 1))

    return girth if girth != float("infinity") else -1


def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in graph if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) == len(graph):
        return topo_order
    else:
        raise ValueError("Graph has at least one cycle, topological sort not possible")


def connected_components(graph: Dict[int, List[int]]) -> List[Set[int]]:
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(component)

    return components


def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    color = {}

    for start in graph:
        if start not in color:
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False

    return True
