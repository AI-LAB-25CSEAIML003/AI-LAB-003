#--------------A* -----------------
def get_user_inputs():
    # 1 take input for heuristic values
    heuristic = {}
    num_nodes = int(input("enter total number of nodes : "))

    print("\nenter heuristic value h(n) for each node : ")

    for _ in range(num_nodes):
        node = input("node name : ").strip().upper()
        h_val = float(input(f"heuristic h({node}): "))
        heuristic[node] = h_val

    # 2 take input for graph edges
    graph = {node: [] for node in heuristic}

    num_edges = int(input("\nenter total number of directed edges : "))

    print("\nenter edges in format (from_node to_node weight): ")

    for i in range(num_edges):
        u, v, w = input(f"edge{i + 1} : ").strip().split()
        u, v = u.upper(), v.upper()
        weight = float(w)

        graph[u].append((v, weight))

    return heuristic, graph


def astar(graph, heuristic, start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:

        # select node with minimum f = g + h
        current = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )

        open_list.remove(current)

        current_node = current[0]

        # GOAL check & path reconstruction
        if current_node == goal:
            path = [current_node]

            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)

            path.reverse()

            return path, g_cost[goal]

        # neighbor explanation
        for neighbor, cost in graph.get(current_node, []):
            new_cost = g_cost[current_node] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node
                open_list.append((neighbor, new_cost))

    return None, float('inf')


# ------- main program --------------

if __name__ == "__main__":

    print("=== A* ALGORITHM INPUT SETUP ===\n")

    heuristic, graph = get_user_inputs()

    print("\n--- path finding ---")

    start = input("enter start node : ").strip().upper()
    goal = input("enter goal node : ").strip().upper()

    path, cost = astar(graph, heuristic, start, goal)

    print("\n=== RESULT ===")

    if path:
        print("shortest path:", "->".join(path))
        print("total path cost:", cost)
    else:
        print("path not found")