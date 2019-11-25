# next_edge function retreives the next available edges from the graph for the given vertex 
def next_edges(graph,available_edges,vertex,graph_size):
    for j in range(graph_size):
        l=[vertex]
        if(g[vertex][j]!=0):
            l.append(j)
            available_edges.append(l)
    return 
# Function to returns next frontier edge with minimum cost 
def prim_frontier_edge(graph,available_edges,visited):
    min=9999999
    for edge in available_edges:
        if(graph[edge[0]][edge[1]]!=0):
             if((visited[edge[0]]==1 and visited[edge[1]]==0) and graph[edge[0]][edge[1]]<min):
               min=graph[edge[0]][edge[1]]
               i=edge[0]
               j=edge[1]
    visited[j]=1
    return [i,j]
#Function which removes the edges(selected Edges) from the available list for the given vertex
def update_frontier_edge(graph,available_edges,new_vertex,graph_size):
    for edge in available_edges:    
        if(edge[1]==new_vertex):
            available_edges.remove(edge)        
    next_edges(graph,available_edges,new_vertex,graph_size)
    return
def prims(graph,start):
    #initializing vertex list with start node
    vertex=[start]
    graph_size=len(graph)
    spanning_edges=[]
    available_edges=[]
    #finding next available edges to built Minimum Spanning tree 
    next_edges(graph,available_edges,start,graph_size)
    #List which keeps tracks whether a node is visited or not 
    visited=[]
    for i in range(graph_size):
        visited.append(0)
    visited[start]=1
    #Actual prims algorithm
    for i in range(graph_size-1):
        minimum_edge=prim_frontier_edge(graph,available_edges,visited)
        spanning_edges.append(minimum_edge)
        new_vertex=minimum_edge[1]
        vertex.append(new_vertex)
        update_frontier_edge(graph,available_edges,new_vertex,graph_size)
    total_cost=0
    for i in spanning_edges:
        total_cost=total_cost+graph[i[0]][i[1]]
    #Cost graph which store the cost of the edges that are present in the resultant Minimum spanning tree    
    mstree=[]
    #Initializing the resultant cost graph with value zero in all positions
    for i in range(graph_size):
        l=[]
        for j in range(graph_size):
            l.append(0)
        mstree.append(l)
    #only the cost of edges that are present in the spanning edges are copied    
    for i in spanning_edges:
        mstree[i[0]][i[1]]=graph[i[0]][i[1]]
    for i in spanning_edges:
        mstree[i[1]][i[0]]=graph[i[0]][i[1]] 
    print("The total cost is :",total_cost)
    print("The minimum spanning tree is ")
    for i in mstree:
        print(i)
    return mstree
graph_size=int(input("Enter the number of vertex"))
graph=[]
for i in range(graph_size):
    l=[]
    for j in range(graph_size):
        print("Enter the value for edge ",i,j)
        x=int(input())
        l.append(x)
    graph.append(l)
start=int(input("Enter the start vertex:"))
prims(graph,start)