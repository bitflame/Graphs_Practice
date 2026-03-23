import datetime

from BasicDataStructures.src.MyQueue import Queue
from BinaryTreeNode import BinaryTreeNode
from Sandbox import Stack


def find(start_node, search_for):
    if start_node is None:
        return None
    if start_node.item < search_for:
        return find(start_node.right, search_for)
    if start_node.item > search_for:
        return find(start_node.left, search_for)
    return start_node


def insert(current_node, value):
    if current_node is None:
        return BinaryTreeNode(value)
    if value < current_node.item:
        current_node.left = insert(current_node.left, value)
    if value > current_node.item:
        current_node.right = insert(current_node.right, value)
    return current_node


# prints tree using level-order
def print_existing_tree(current_node):
    if current_node is None:
        return
    queue = Queue()
    queue.enqueue((current_node, 0))
    tree_height = get_height(current_node)
    lines = []
    level = 0
    node_line = ""
    connection_line = ""
    additional_left_spacing = ""
    while not queue.is_empty() and level < tree_height:
        current_node_and_level = queue.dequeue()
        current_node = current_node_and_level[0]
        node_level = current_node_and_level[1]
        line_length = subtree_width(tree_height - 1 - level)
        if level != node_level:
            level = node_level
            line_length = subtree_width(tree_height - 1 - level)
            lines.append(node_line)
            lines.append(connection_line)
            for i in range(len(lines)):
                lines[i] = "   " + additional_left_spacing + spacing(line_length) + lines[i]
            node_line = ""
            connection_line = ""
        node_line += draw_node(current_node, line_length)
        node_line += spacing_between_nodes(tree_height, level)
        connection_line += draw_connections(current_node, line_length)
        connection_line += spacing_between_connections(tree_height, level)
        # levleorder
        if current_node is not None:
            queue.enqueue((current_node.left, level + 1))
            queue.enqueue((current_node.right, level + 1))
        else:
            queue.enqueue((None, level + 1))
            queue.enqueue((None, level + 1))
    for line in lines:
        print(line)


def spacing_between_connections(tree_height, level):
    spacing_length = subtree_width(tree_height - level)
    return " " * spacing_length


def draw_connections(node, line_length):
    if node is None:
        return "   " + spacing(line_length) + "   " + spacing(line_length) + "   "
    connection = draw_left_connection_part(node, line_length)
    connection += draw_junction(node)
    connection += draw_right_connection_part(node, line_length)
    return connection


def draw_left_connection_part(node, line_length):
    if node.left is None:
        return "   " + spacing(line_length)
    else:
        return " |-" + draw_line(line_length)


def draw_line(line_length):
    return "-" * line_length


def draw_right_connection_part(node, line_length):
    if node.right is None:
        return spacing(line_length) + "   "
    else:
        return draw_line(line_length) + "-| "


def draw_junction(node):
    if node.left is None and node.right is None:
        return "   "
    elif node.left is None:
        return " +-"
    elif node.right is None:
        return "-+ "
    else:
        return "-+-"


def spacing_between_nodes(tree_height, level):
    spacing_length = subtree_width(tree_height - level)
    spacing = " " * spacing_length
    if spacing_length > 0:
        spacing += "   "
    return spacing


def draw_node(current_node, line_length):
    str_node = "   "
    str_node += spacing(line_length)
    str_node += stringify_node_value(current_node)
    str_node += spacing(line_length)
    return str_node


def stringify_node_value(node):
    if node is None:
        return "   "
    if node.item is None:
        return "   "
    node_value = str(node.item)
    if len(node_value) == 1:
        return " " + node_value + " "
    if len(node_value) == 2:
        return node_value + " "

    return node_value[0:3]


def subtree_width(heigth):
    if heigth <= 0:
        return 0
    leaf_width = 3
    spacing = 3
    max_num_of_leaves = pow(2, heigth - 1)
    width_of_tree = max_num_of_leaves * leaf_width + (max_num_of_leaves - 1) * spacing
    width_of_subtree = (width_of_tree - spacing) // 2
    return width_of_subtree


def spacing(line_length):
    return " " * line_length


def get_height(node):
    if node is None:
        return 0
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return 1 + max(left_height, right_height)


def preorder(node):
    if node is None:
        return
    print(node.item, end=' ')
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.item)
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.item)


# _3 = BinaryTreeNode(3)
# insert(_3, 3)
# insert(_3, 2)
# insert(_3, 4)
# print_existing_tree(_3)
# print('\nTree contains 2? ', find(_3, 2))
# print('\nTree contains 13? ', find(_3, 13), '\n')


# preorder(_3)

def create_example_tree():
    a1 = BinaryTreeNode('a1')
    b2 = BinaryTreeNode('b2')
    c3 = BinaryTreeNode('c3')
    d4 = BinaryTreeNode('d4')
    e5 = BinaryTreeNode('e5')
    f6 = BinaryTreeNode('f6')
    g7 = BinaryTreeNode('g7')
    d4.left = b2
    d4.right = f6
    b2.left = a1
    b2.right = c3
    f6.left = e5
    f6.right = g7
    return d4


def create_number_tree():
    _4 = BinaryTreeNode("4")
    insert(_4, "2")
    insert(_4, "1")
    insert(_4, "3")
    insert(_4, "6")
    insert(_4, "5")
    insert(_4, "7")
    return _4


# print("Printing the example tree")
# print_existing_tree(create_example_tree())
now = datetime.datetime.now()
print(now)
formated = now.strftime("%Y-%m-%d %H:%M:%S")
print("Today's date and time - nice format: ", formated)
print(f"Today's date is: {datetime.date.today()}")
print(f"Today's date is: {datetime.date.today()}")
print_existing_tree(create_number_tree())


def create_integer_number_tree():
    _4 = BinaryTreeNode(4)
    insert(_4, 2)
    insert(_4, 1)
    insert(_4, 3)
    insert(_4, 6)
    insert(_4, 5)
    insert(_4, 7)
    return _4


print_existing_tree(create_integer_number_tree())


# return a list of tree items according to in-order
def to_list(node):
    if node is None:
        return []
    aux = Stack()
    aux.push(node)
    result = []
    while True:
        while node.left is not None:
            node = node.left
            aux.push(node)
        if aux.isEmpty():
            break
        node = aux.pop()
        result.append(node.item)
        while (not aux.isEmpty()) and node.right is None:
            node = aux.pop()
            result.append(node.item)
        if aux.isEmpty() and node.right is None: break
        node = node.right
        aux.push(node)
    return result


_a = BinaryTreeNode('a')
_b = BinaryTreeNode('b')
_c = BinaryTreeNode('c')
_d = BinaryTreeNode('d')
_h = BinaryTreeNode('h')
_i = BinaryTreeNode('i')
_e = BinaryTreeNode('e')
_j = BinaryTreeNode('j')
_f = BinaryTreeNode('f')
_k = BinaryTreeNode('k')
_g = BinaryTreeNode('g')
_a.left = _b
_a.right = _c
_b.left = _d
_b.right = _e
_d.left = _h
_e.left = _i
_e.right = _j
_c.left = _f
_f.right = _k
_c.right = _g

print(to_list(_a))
print(to_list(create_example_tree()))


# in-order traversal
def to_list_update(start_node):
    if start_node is None:
        return []
    result = []
    result += to_list_update(start_node.left)
    result.append(start_node.item)
    result += to_list_update(start_node.right)
    return result


to_list_update(create_example_tree())


def to_list_preorder(start_node):
    if start_node is None:
        return []
    result = []
    result.append(start_node.item)
    result += to_list_preorder(start_node.left)
    result += to_list_preorder(start_node.right)
    return result


print(to_list_preorder(create_example_tree()))


def to_list_postorder(start_node):
    if start_node is None:
        return []
    result = []
    result += to_list_postorder(start_node.left)
    result += to_list_postorder(start_node.right)
    result.append(start_node.item)
    return result

print(to_list_postorder(create_example_tree()))
