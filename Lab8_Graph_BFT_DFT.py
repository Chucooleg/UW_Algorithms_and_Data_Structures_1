adj_list1 = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': ['h', 'i']
}

adj_list2 = {
    'a': ['b'],
    'b': ['c'],
    'c': ['d', 'c1'],
    'd': ['d1'],
    'd1': ['d2'],
    'c1': ['c2']
}

###############################################
def DFT(adj_list):
    # depth first traversal
    stack = ['a']

    while stack:
        node = stack.pop()
        print(node)
        if node in adj_list:
            neighbors = adj_list[node]
            stack += neighbors
            
DFT(adj_list1)

DFT(adj_list2)
###############################################
from queue import Queue

q = Queue(maxsize=0)


def BFT(adj_list):
    # breadth first traversal
    q = Queue()
    q.put('a')

    while not q.empty():
        node = q.get()
        print(node)
        if node in adj_list:
            neighbors = adj_list[node]
            for nei in neighbors:
                q.put(nei)
                
 BFT(adj_list1)
 BFT(adj_list2)
