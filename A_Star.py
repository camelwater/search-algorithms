from Algorithm import Algorithm
from PriorityQueue import PriorityQueue
from Graph import Graph
from A_Star_Node import A_Node
from math import sqrt
import time
# import pygame

def H(cur: A_Node, dest: A_Node):
    '''
    heuristic function (distance from node to another)
    '''
    return sqrt((cur.x - dest.x)**2 + (cur.y - dest.y)**2)

def D(cur: A_Node, neighbor: A_Node):
    '''
    edge weight between current node and neighbor
    LMAO edges aren't weighted so it's just 1
    '''
    return 1

def reconstruct_path(source: A_Node, dest: A_Node):
    '''
    Prints out the shortest path between the source and destination nodes.
    '''
    path = []
    node = dest
    if not node.get_prev() and node!=source: print("Failed to reconstruct path.")

    while node.get_prev():
        path.append(node)
        node = node.get_prev()
    
    path.append(source)
    printed_path = ""
    for n in path[::-1]:
        printed_path+=f"{n} -> "
    print(printed_path.rstrip(" -> "))

def A_star(source: A_Node, destination: A_Node):
    '''
    Finds the shortest path between the source and destination nodes using the A* search algorithm.
    '''
    pq = PriorityQueue()
    open_set = pq.PriorityQueue(source) #min-heap priority queue

    source.set_gScore(0)
    source.set_fScore(H(source, destination))

    while open_set.length()>0:
        current = open_set.extract_min()
        if current == destination:
            print(f"Found the shortest path from node {source} to node {destination} - {current.f_score} nodes long.\n")
            reconstruct_path(source, current)
            return 
        
        for neighbor in current.get_neighbors():
            eval_gScore = current.g_score + D(current, neighbor)
            if eval_gScore < neighbor.g_score:
                neighbor.prev = current
                neighbor.set_gScore(eval_gScore)
                neighbor.set_fScore(eval_gScore + H(neighbor, destination))
                if neighbor not in open_set.get_heap():
                    open_set.insert(neighbor)
    
    print("No path could be found.")

def main():
    graph = Graph(100, 100, algo=Algorithm.A_STAR)
    start = graph.get()[27][50]
    end = graph.get()[99][95]
    start_time = time.time()
    A_star(start, end)
    print("found in:", time.time()-start_time)

if __name__ == "__main__":
    main()