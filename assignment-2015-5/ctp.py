import sys, copy

graph_file = open(sys.argv[1])
start_node = sys.argv[2]
destination_node = sys.argv[3]
blocked_edges_file = open(sys.argv[4])


#creating dictionaries from the input files

Graph {}
with graph_file as G:
    for line in G:
         x, y, w = line.split() # x, y = nodes, w = weight
		 if not x in Graph:
		   Graph[x] = {}
		   Graph[x][y] = w
		 if not y in Graph: #undirected graph
		   Graph[y] = {}
		   Graph[y][x] = w
	G.close()  
	
Edges {}
with blocked_edges_file as E:
    for line in E:
	   x, y = line.split() # x, y = nodes
	   Edges[x][y] = {}
	   Edges[y][x] = {} # undirected graph
	E.close()
	
def reposition (Graph, Edges): #deletes blocked edges from the graph
    for key in Edges:
	   if Edges[key] in Graph:
	      del Graph[key]
    return	
         
def Dijkstra(Graph, start_node, destination_node=None):
    # initializing the distance list
    dist = dict()
    previous_node = dict() #previous node in optimal path from source
    dist[start_node] = 0 #distance from source to source
    U = copy.deepcopy(Graph) # U = unvisited nodes
	
    def extract_min():
        min = None
        ret = None
        for key in dist:
            if key in U and ((dist[key] < min) if min != None else True):
                min = dist[key]
                ret = key
        if ret is not None:
            del U[ret]
        return ret
    while U:
        u = extract_min()
        for v in Graph[u]: # where v is still in U
            alt = int(dist[u]) + int(Graph[u][v])
            if v not in dist or alt < int(dist[v]): # a shorter path to v has been found
                dist[v] = alt
                previous_node[v] = u
    node_list = list()
    try:
        next = destination_node
        while True:
            node_list.insert(0,next)
            next = previous_node[next]
    except:
        pass
    return node_list, dist
    
print( Dijkstra( Graph, starting_node, destination_node))
