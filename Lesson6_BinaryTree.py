#*Q1: Mirror image of a binary tree
# Write a recursive method that takes a tree node and morphs it to create a mirror image of the tree rooted at that node.

#Q2: Any path has a given sum
#*Write a recursive method that takes a tree node and an integer value, and returns:
#*- true if there is exists a path from the passed in node to any leaf in the tree that has the sum equal to passed in value
#*- false otherwise.

#*Q3: Compute height function
###

import collections

class Node:
    def __init__(self, input_value):
        self.value = input_value
        self.left = None
        self.right = None


def create_tree_1():
    root = Node(10)
    root.left = Node(7)
    root.right = Node(17)

    root.left.left = Node(4)
    root.left.right = Node(55)

    root.right.left = Node(44)
    root.right.right = Node(25)

    return root

def output_tree(root):
    if not root:
        return

    q = collections.deque()
    q.append(root)
    while len(q) > 0:
        n = q.popleft()
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

        print(f"{n.value} ")

    print("")


def mirrorize(node):
    if not node:
        return

    temp = node.left
    node.left = node.right
    node.right = temp

    mirrorize(node.left)
    mirrorize(node.right)


def do_mirror_stuff():
    root1 = create_tree_1()
    output_tree(root1)
    mirrorize(root1)
    output_tree(root1)


def any_path_to_leaf_has_sum(node, sum):
    if not node:
        return sum == 0

    return any_path_to_leaf_has_sum(node.left, sum - node.value) or any_path_to_leaf_has_sum(node.right, sum - node.value)


def do_path_has_sum_stuff():
    root1 = create_tree_1()

    for ii in range(1, 201):
        if any_path_to_leaf_has_sum(root1, ii):
            print("Tree has sum" + str(ii))


def tree_height(node):
    if not node:
        return 0

    height_of_my_left_sub_tree = tree_height(node.left)
    height_of_my_right_sub_tree = tree_height(node.right)
    my_height = 1 + max(height_of_my_left_sub_tree, height_of_my_right_sub_tree)
    # Could also be 1+ max(tree_height(node.left), tree_height(node.right))
    return my_height


def compute_height_stuff():
    root1 = create_tree_1()
    height_root_node = tree_height(root1) - 1
    print("Tree height is " + str(height_root_node))


def do_post_order(node):
    if not node:
        return

    do_post_order(node.left)
    do_post_order(node.right)
    print(f"{node.value}" )


def do_traversal_stuff():
    root1 = create_tree_1()

    print("Post order traversal:")
    do_post_order(root1)
    print("")
    print("-----------------")


do_mirror_stuff()
do_path_has_sum_stuff()
compute_height_stuff()
do_traversal_stuff()