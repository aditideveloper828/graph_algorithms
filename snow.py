"""
Snow
Make sure all locations in the city are safely reachable and connected 
to each other so that essential services can be provided after snow. The 
goal is to clear the least amount of road surface
so that all locations are reachable.
Author: Aditi Sharma
Date: 20/3/2023
"""
import math


def next_vertex(in_tree, distance):
    """returns a closest vertex that is not yet part of the tree"""
    current_dist = math.inf
    counter = 0
    while counter < len(distance):
        if in_tree[counter] == False:
            closest_vertex = counter
            current_dist = distance[counter]
            counter = len(distance)
        counter += 1
        
            
    for i in range(len(distance)):
        if in_tree[i] == False and distance[i] < current_dist:
            closest_vertex = i
            current_dist = distance[i]
            
    return closest_vertex


def prim(adj_list, start):
    """making a minimum spanning tree according to Prim's algorithm as
    taught in lectures"""
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [math.inf for i in range(n)]
    parent = [None for i in range(n)]
    distance[start] = 0
    while all(in_tree) != True:
        u_vtx = next_vertex(in_tree, distance)
        in_tree[u_vtx] = True
        for v_vtx, weight in adj_list[u_vtx]:
            if (in_tree[v_vtx] == False) and (weight < distance[v_vtx]):
                distance[v_vtx] = weight
                parent[v_vtx] = u_vtx
    return parent
    
    
    
    
def get_data(physical_contact_info):
    """turns graph string into usable data and prepares empty adjacency list"""
    #seperate lines
    str_data = list(physical_contact_info.split('\n'))
    str_data = [x.strip() for x in str_data]
    str_data.pop()
    first_line = list(str_data[0].split(" "))
    dimention = int(first_line[1])
    adj_list = [[] for x in range(dimention)]
    str_data.pop(0)
    
    #change vertices to integers
    int_data = []
    for i in range(len(str_data)):
        line_data = list(str_data[i].split(" "))
        line_data = [int(x) for x in line_data]  
        int_data.append(line_data) 
    return int_data, adj_list
    

def make_list(data, adj_list):
    """makes adjacency list"""
    for line in data:
        #preparing vertex data
        vertex_1 = line[0]
        vertex_2 = line[1]
        
        #adding to adjacency list
        weight = line[-1]
        adj_list[vertex_1].append((vertex_2, weight))
        adj_list[vertex_2].append((vertex_1, weight))
    return adj_list    


def which_segments(city_map):
    """takes the map of the city and returns a list
    of road segments that must be cleared so that there
    is a clear path between any two locations and the
    total length of the cleaned-up road segments is minimised"""
    map_data, empty_list = get_data(city_map)
    adj_list = make_list(map_data, empty_list)
    parent = prim(adj_list, 0)
    
    #creating tuples for road segments
    segments = set()
    
    for i in range(len(parent)):
        if parent[i] != None:
            pair = sorted([i, parent[i]])
            segments.add(tuple(pair))
    return segments

def test():
    city_map = """\
    U 3 W
    0 1 1
    2 1 2
    2 0 4
    """

    print(sorted(which_segments(city_map)))

    city_map = """\
    U 1 W
    """

    print(sorted(which_segments(city_map)))


    city_map = """\
    U 4 W
    0 1 5
    1 3 5
    3 2 3
    2 0 5
    0 3 2
    1 2 1
    """

    print(sorted(which_segments(city_map)))

test()