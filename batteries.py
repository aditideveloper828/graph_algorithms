"""
Batteries
Determine the battery capacity required for vehicles.
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


def dijkstra(adj_list, start):
    """dijkstra based on algorithm in lectures"""
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [math.inf for i in range(n)]
    parent = [None for i in range(n)]
    distance[start] = 0
    while all(in_tree) != True:
        u_vtx = next_vertex(in_tree, distance)
        in_tree[u_vtx] = True
        for v_vtx, weight in adj_list[u_vtx]:
            if (in_tree[v_vtx] == False) and (distance[u_vtx] + weight) < distance[v_vtx]:
                distance[v_vtx] = distance[u_vtx] + weight
                parent[v_vtx] = u_vtx
    return distance

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


def min_capacity(city_map, depot_position):
    #shortest path
    """ takes the map of a city and the position of the depot,
    and returns the minimum battery capacity 
    required to make the trip specified in the problem statement.
    """
    map_data, empty_list = get_data(city_map)
    adj_list = make_list(map_data, empty_list) 
    distance = dijkstra(adj_list, depot_position)
    
    #calculating minimum battery capacity
    inf_removed_dist = []
    for i in distance:
        if i != math.inf:
            inf_removed_dist.append(i)
    max_distance = max(inf_removed_dist)
    min_capacity = max_distance * 4
    return min_capacity


def test():
    city_map = """\
    U 4 W
    0 2 5
    0 3 2
    3 2 2
    """
    
    print(min_capacity(city_map, 0))
    print(min_capacity(city_map, 1))
    print(min_capacity(city_map, 2))
    print(min_capacity(city_map, 3))    
    
    
test()