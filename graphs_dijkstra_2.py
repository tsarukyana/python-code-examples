"""
Using Hash table for show the implementation of
graph dijkstart algorithm
"""
graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")

parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

processed = []


def find_lowest_cost_node(_costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for _node in _costs:
        _cost = _costs[_node]
        if _cost < lowest_cost and _node not in processed:
            lowest_cost = _cost
            lowest_cost_node = _node
    return lowest_cost_node


if __name__ == '__main__':
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    print(processed)
