import heapq
 
def dijskstra_worst(start, graph, current_distance):
    queue = [] # city, path distance and current path
    heapq.heappush(queue, (start, 0, [start]))
    
    visited = [start]
    best_distance = -1
    
    while queue:
        current_city, path_distance, current_path = heapq.heappop(queue)
        
        for city in graph[current_city].keys():
            if city in current_path and len(current_path) > 1: # Going back or the loop is completed
                # Testing if the path is good
                if len(current_path) == len(graph.keys()): # All the cities in the path
                    if best_distance == -1 or path_distance > best_distance: 
                        best_distance = path_distance
            else: # the city is a new one in the path
                aux_path = current_path.copy()
                aux_path.append(city)
                aux_distance = path_distance + graph[current_city][city]   
                heapq.heappush(queue, (city, aux_distance, aux_path))
    
    if current_distance == -1:
        return best_distance
    elif current_distance < best_distance:
        return best_distance
    else:
        return -1
    
def dijskstra(start, graph, current_distance):
    queue = [] # city, path distance and current path
    heapq.heappush(queue, (start, 0, [start]))
    
    visited = [start]
    best_distance = -1
    
    while queue:
        current_city, path_distance, current_path = heapq.heappop(queue)
        
        for city in graph[current_city].keys():
            if city in current_path and len(current_path) > 1: # Going back or the loop is completed
                # Testing if the path is good
                if len(current_path) == len(graph.keys()): # All the cities in the path
                    if best_distance == -1 or path_distance < best_distance:
                        best_distance = path_distance
            else: # the city is a new one in the path
                aux_path = current_path.copy()
                aux_path.append(city)
                aux_distance = path_distance + graph[current_city][city]   
                if current_distance == -1 or aux_distance < current_distance: # the path is still better
                    heapq.heappush(queue, (city, aux_distance, aux_path))
    
    if current_distance == -1:
        return best_distance
    elif current_distance > best_distance:
        return best_distance
    else:
        return -1
    

def number9_1():
    dataFile = open("data/day9.txt", "r")

    graph = {}    
    for line in dataFile:
        s_line = line.replace("\n", "")
        aux = s_line.split(" = ")
        cities = aux[0].split(" to ")
        distance = int(aux[1])
        
        if not cities[0] in graph.keys():
            graph[cities[0]] = {}
        graph[cities[0]][cities[1]] = distance
        
        if not cities[1] in graph.keys():
            graph[cities[1]] = {}
        graph[cities[1]][cities[0]] = distance
        
    cities = graph.keys()
    current_path_distance = -1
    for city in cities:
        res = dijskstra(city, graph, current_path_distance)
        if res != -1:
            current_path_distance = res
        
    print("Result day 9 part 1: The shortest path is " + str(current_path_distance))
    
def number9_2():
    dataFile = open("data/day9.txt", "r")

    graph = {}    
    for line in dataFile:
        s_line = line.replace("\n", "")
        aux = s_line.split(" = ")
        cities = aux[0].split(" to ")
        distance = int(aux[1])
        
        if not cities[0] in graph.keys():
            graph[cities[0]] = {}
        graph[cities[0]][cities[1]] = distance
        
        if not cities[1] in graph.keys():
            graph[cities[1]] = {}
        graph[cities[1]][cities[0]] = distance
        
    cities = graph.keys()
    current_path_distance = -1
    for city in cities:
        res = dijskstra_worst(city, graph, current_path_distance)
        if res != -1:
            current_path_distance = res
        
    print("Result day 9 part 2: The longest path is " + str(current_path_distance))
    
number9_1()
number9_2()
            
        
        