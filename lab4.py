def get_user_input():
    heruistic ={}
    num_nodes=int(input("Enter total number of nodes:"))
    print("\n Enter Heuristic value h(n) for each node:")
    for _ in range (num_nodes):
        node = input("Node name:").strip().upper()
        h_val = float(input(f"Heuristic h({node}):"))
        heuristic = h_val
# 2.take inputs for graph
    graph = {node:[] for node in heuristic}
    num_edges = int(input("\n Enter total number of directed adge:"))
    print("\n Enter edges in format (from_nod to_node weight)")
    for i in range(num_edges):
        u,v,w=input(f"edge {i+1}:").strip().split()
        u,v= u.upper,v.upper()
        weight = float(w)
        graph.append((v,weight))
    return graph,heuristic

def astar(graph,heuristic,start,goal):
    open_list=[(start,0)]
    came_form={}
    g_cost ={start:0}

    while open_list:
        current = min(open_list,key=lambda x:x[1]+heuristic)
        list.remove(current)
        current_node=current[0]

    if current_node==goal:
        path=[goal]
        while current_node in came_form:
            current_node = came_form[current_node]
            path.append(current_node)
        path.reverse()
        return path,g_cost[goal]
    for neighbor ,cost in graph.get(current_node,[]):
        new_cost = g_cost[current_node]+cost

        if neighbor not in g_cost or new_cost <g_cost[neighbor]:
            g_cost[neighbor]= new_cost

