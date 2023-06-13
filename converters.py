"""
Converters
A converter takes as input a video in some format 
and produces as output a video in another format
Author: Aditi Sharma
Date: 19/3/2023
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
        weight = 1
        adj_list[vertex_1].append((vertex_2, weight))
        
    return adj_list    


def format_sequence(converters_info, source_format, destination_format):
    """returns the shortest sequence of formats 
    (and therefore converters) required in order to convert 
    a video from the source format to the destination format. 
    Does this using helper funtions"""
    
    converters_data, empty_list = get_data(converters_info)
    adj_list = make_list(converters_data, empty_list)    
    parent = dijkstra(adj_list, source_format)
    
    #find path from destination to source
    reverse_order = []
    this_vtx = destination_format
    while parent[this_vtx] != None and this_vtx != source_format:
        reverse_order.append(this_vtx)
        this_vtx = parent[this_vtx]
    if source_format == destination_format:
        return [source_format]    
    if this_vtx != source_format:
        return "No solution!"
    
    #reversing destination to source path
    reverse_order.append(this_vtx)
    order = []
    for i in range(len(reverse_order)-1, -1, -1):
        order.append(reverse_order[i])
    return order    


def test():
    """Test cases for assignment"""
    converters_info_str = """\
    D 2
    0 1
    """
    
    source_format = 0
    destination_format = 1
    
    print(format_sequence(converters_info_str, source_format, destination_format))
    # should get output: [0, 1]
    
    
    converters_info_str = """\
    D 2
    0 1
    """
    
    print(format_sequence(converters_info_str, 1, 1))
    #should get output: [1]
    
    converters_info_str = """\
    D 2
    0 1
    """
    
    print(format_sequence(converters_info_str, 1, 0))    
    #should get output: No solution!
    
    converters_info_str = """\
    D 5
    1 0
    0 2
    2 3
    1 2
    """
    
    print(format_sequence(converters_info_str, 1, 2))
    #should get output: [1, 2]
    
test()
