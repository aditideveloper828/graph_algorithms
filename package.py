"""
Package
Determines build process for installing programs
Author: Aditi Sharma
Date: 20/3/2023
"""


def dfs_loop(adj_list, vertex, state, parent, stack):
    """main part of the dfs algorithm"""
    for point, weight in adj_list[vertex]:
        if state[point] == "U":
            state[point] = "D"
            parent[point] = vertex
            dfs_loop(adj_list, point, state, parent, stack)
    state[vertex] = "P"
    stack.append(vertex)


def topological_sorting(adj_list):
    """carries out topological sorting based on algorithm in lectures"""
    n = len(adj_list)
    state = ["U" for i in range(n)]
    parent = [None for i in range(n)]
    stack = []
    for vertex in range(n):
        if state[vertex] == "U":
            dfs_loop(adj_list, vertex, state, parent, stack)
    return stack


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
        
    return adj_list    



def build_order(dependencies):
    """takes a description of the dependencies between a
    number of programs and returns a valid order for the build process. 
    Does this using helper functions"""
    dependencies_data, empty_list = get_data(dependencies)
    adj_list = make_list(dependencies_data, empty_list)
    stack = topological_sorting(adj_list)
    order = []
    for i in range(len(stack)-1, -1, -1):
        order.append(stack[i])
    return order


def test():
    dependencies = """\
    D 2
    0 1
    """
    
    print(build_order(dependencies))
    dependencies = """\
    D 3
    1 2
    0 2
    """
    
    print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])    
    
    dependencies = """\
    D 3
    """
    # any permutation of 0, 1, 2 is valid in this case.
    solution = build_order(dependencies)
    if solution is None:
        print("Wrong answer!")
    else:
        print(sorted(solution))
        
test()