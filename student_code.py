import queue,math
def shortest_path(M,start,goal):
    q=queue.PriorityQueue()
    q.put((0,[start,0]))# total_score,[road,gScore]
    visited = set() # quick check is this path visited
    cameFrom={start:[-1,0]} #used for contraction of the path [cameFrom,gScore]
    while not q.empty():
        current = q.get()[1]
        visited.add(current[0])
        if current[0] == goal:
            return reconstruct_path(cameFrom,current[0])
        # current is a list - #of road,gScore
        # r is just a #of road
        for r in M.roads[current[0]]:
            if r not in visited:
                g = gScore(current,r,M)
                f = fScore(r,goal,M)
                if r in cameFrom and g<cameFrom[r][1]:
                    cameFrom[r]=[current[0],g]
                elif r not in cameFrom:
                    cameFrom[r]=[current[0],g]
                q.put((g+f,[r,g]))
    print("shortest path called")
    return "no path found"
                      
def gScore(fromRoad,toRoad,M):
    return fromRoad[1] + math.sqrt((M.intersections[fromRoad[0]][0] - M.intersections[toRoad][0])**2+(M.intersections[fromRoad[0]][1] - M.intersections[toRoad][1])**2)
def fScore(fromRoad,toRoad,M):
    
    return math.sqrt((M.intersections[fromRoad][0] - M.intersections[toRoad][0])**2+abs(M.intersections[fromRoad][1] - M.intersections[toRoad][1])**2)
def reconstruct_path(cameFrom,current):
    path = [current]
    while current in cameFrom:
        current = cameFrom[current][0]
        if current != -1:
            path.insert(0,current)
    return path
    