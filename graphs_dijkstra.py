"""
dijkstra algorithm demo
graph size:6*6
node index start from 0
"""
graph_list = [[0, 2, 1, 4, 5, 1],
              [1, 0, 4, 2, 3, 4],
              [2, 1, 0, 1, 2, 4],
              [3, 5, 2, 0, 3, 3],
              [2, 4, 3, 4, 0, 1],
              [3, 4, 7, 3, 1, 0]]


def dijkstra(graph, src):
    # init
    visited = []
    distance = {src: 0}
    node = list(range(len(graph[0])))
    if src in node:
        node.remove(src)
        visited.append(src)
    else:
        return None
    for i in node:
        distance[i] = graph[src][i]
    prefer = src
    while node:
        _distance = float('inf')
        for i in visited:
            for j in node:
                if graph[i][j] > 0:
                    if _distance > distance[i] + graph[i][j]:
                        _distance = distance[j] = distance[i] + graph[i][j]
                        prefer = j
        visited.append(prefer)
        node.remove(prefer)
    return distance


if __name__ == '__main__':
    distance = dijkstra(graph_list, 0)
    print(distance)
