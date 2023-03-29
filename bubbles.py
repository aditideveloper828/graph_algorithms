"""
Bubbles
Determines covid bubbles for people.
Author: Aditi Sharma
Date: 20/3/2023
"""

from collections import deque

def bfs_loop(adj_list, queue, state):
    """main part of the bfs algorithm (performs breadth-first search)"""
    while len(queue) > 0:
        vertex = queue.popleft()
        for point, weight in adj_list[vertex]:
            if state[point] == "U":
                state[point] = "D"
                queue.append(point)
        state[vertex] = "P"



def connections(adj_list):
    """takes physical contact information
    about a group of people and determines the bubbles using 
    connected components algorithm as described in lectures"""
    n = len(adj_list)
    state =  ["U" for i in range(n)]
    queue = deque()
    components = []
    for i in range(n):
        if state[i] == "U":
            prev_state = state.copy()
            state[i] = "D"
            queue.append(i)
            bfs_loop(adj_list, queue, state)
            #need to complete this part
            differences = set()
            for i in range(n):
                if state[i] != prev_state[i]:
                    differences.add(i)
            components.append(differences)
            
    return components
            
    

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
        weight = None
        adj_list[vertex_1].append((vertex_2, weight))
        adj_list[vertex_2].append((vertex_1, weight))
        
    return adj_list    


def bubbles(physical_contact_info):
    #Connected components)
    """takes physical contact information
    about a group of people and determines the bubbles.
    Does this by calling helper functions"""
    physical_contact_data, empty_list = get_data(physical_contact_info)
    adj_list = make_list(physical_contact_data, empty_list)
    return connections(adj_list)


