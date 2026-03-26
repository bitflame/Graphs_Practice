import datetime
from enum import Enum, auto

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


# in-order traversal optimal version
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


#################8.3.2 Inorder, Preorder, and Postorder iterative
def inorder_iterative(start_node):
    if start_node is None:
        return []
    aux = Stack()
    result = []
    while start_node.left is not None:
        aux.push(start_node)
        start_node = start_node.left
    result.append(start_node.item)
    while not aux.isEmpty():
        node = aux.pop()
        if node.right is not None:
            result.append(node.item)
            temp = node.right
            if temp.left is not None:
                aux.push(temp)
                while temp.left is not None:
                    aux.push(temp.left)
                    temp = temp.left
            else:
                result.append(temp.item)
                continue
        else:
            result.append(node.item)
    return result


print(inorder_iterative(create_example_tree()))


def post_order_list(start_node):
    nodes_to_process = Stack()
    current_node = start_node
    last_visited_node = None
    result = []
    while current_node is not None or (not nodes_to_process.isEmpty()):
        if current_node is not None:
            nodes_to_process.push(current_node)
            current_node = current_node.left
        else:
            peek_node = nodes_to_process.peek()
            if peek_node.right is not None and last_visited_node != peek_node.right:
                current_node = peek_node.right
            else:
                last_visited_node = nodes_to_process.pop()
                result.append(last_visited_node.item)
                # action(last_visited_node.item)
    return result


print("result of postorder_iterative: ", post_order_list(create_example_tree()))


def inorder_iterative(start_node):
    nodes_to_process = Stack()
    current_node = start_node
    result = []
    while current_node is not None or (not nodes_to_process.isEmpty()):
        if current_node is not None:
            nodes_to_process.push(current_node)
            current_node = current_node.left
        else:
            current_node = nodes_to_process.pop()
            result.append(current_node.item)
            current_node = current_node.right
    return result


print("result of inorder_iterative: ", inorder_iterative(create_example_tree()))


def preorder_iterative(start_node):
    if start_node is None:
        return []
    result = []
    nodes_to_process = Stack()
    nodes_to_process.push(start_node)
    while (not nodes_to_process.isEmpty()) or current_node is not None:
        current_node = nodes_to_process.pop()
        if current_node is not None:
            result.append(current_node.item)
            nodes_to_process.push(current_node.right)
            nodes_to_process.push(current_node.left)
    return result


print("result of preorder_iterative: ", preorder_iterative(create_example_tree()))


def inoder_iterative_v2(root):
    stack = Stack()
    stack.push(root)
    result = []
    while not stack.isEmpty():
        current_node = stack.pop()
        if not current_node is None:
            if current_node.is_leaf():
                result.append(current_node.item)
                # print(current_node.item,end=' ')
            else:
                stack.push(current_node.right)
                stack.push(BinaryTreeNode(current_node.item))
                stack.push(current_node.left)
    return result


print("result of inorder_iterative: ", inoder_iterative_v2(create_example_tree()))


# have not tested the code below.
class Order(Enum):
    PREORDER = auto()
    INORDER = auto()
    POSTORDER = auto()


def traverse(root, order):
    stack = Stack()
    stack.push(root)
    result = []
    while not stack.isEmpty():
        current_node = stack.pop()
        if not current_node is None:
            if current_node.is_leaf():
                # print(current_node.item, end=' ')
                result.append(current_node.item)
            else:
                if order == Order.POSTORDER:
                    stack.push(BinaryTreeNode(current_node.item))
                stack.push(current_node.right)
                if order == Order.INORDER:
                    Stack.push(BinaryTreeNode(current_node.item))
                stack.push(current_node.left)
                if order == Order.PREORDER:
                    stack.push(BinaryTreeNode(current_node.item))
    return result


# This method also works for branch heights, not just root
def tree_height(root):
    if root is None:
        return 0
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return 1 + max(left_height, right_height)


print("Exercise 3 of chapter 8: Tree Height: ", get_height(create_example_tree()))


# method that returns the lowest common ancestor of a node by me
def find_lca(start_node, value1, value2):
    if start_node is None:
        return -1
    current_value = start_node.item
    if value1 > current_value and value2 > current_value:
        return find_lca(start_node.right, value1, value2)
    if value1 < current_value and value2 < current_value:
        return find_lca(start_node.left, value1, value2)
    return start_node.item


def make_lca_example():
    _6 = BinaryTreeNode(6)
    _4 = BinaryTreeNode(4)
    _7 = BinaryTreeNode(7)
    _2 = BinaryTreeNode(2)
    _1 = BinaryTreeNode(1)
    _3 = BinaryTreeNode(3)
    _5 = BinaryTreeNode(5)
    _6.left = _4
    _6.right = _7
    _4.right = _5
    _4.left = _2
    _2.left = _1
    _2.right = _3
    return _6


bin_tree_root = make_lca_example()
print_existing_tree(bin_tree_root)
print("lca of 1 and 5; expected answer: 4, actual answer: ", find_lca(bin_tree_root, 5, 1))
print("lca of 1 and 5; expected answer: 4, actual answer: ", find_lca(bin_tree_root, 1, 5))


def make_char_tree():
    # makes MICHAEL
    root = BinaryTreeNode('M')
    root.left = BinaryTreeNode('I')
    root.right = BinaryTreeNode('C')
    root.left.left = BinaryTreeNode('H')
    root.left.right = BinaryTreeNode('A')
    root.right.left = BinaryTreeNode('E')
    root.right.right = BinaryTreeNode('L')
    return root


def make_int_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    return root


def level_order(start_node):
    if start_node is None:
        return []
    to_process = Queue()
    to_process.enqueue(start_node)
    result = []
    while not to_process.is_empty():
        current = to_process.dequeue()
        if current is not None:
            result.append(current.item)
            to_process.enqueue(current.left)
            to_process.enqueue(current.right)
    return result


root = make_int_tree()
print_existing_tree(root)
print(level_order(root))


def level_order_rec(start_node, to_process):
    if start_node is None:
        return []
    to_process = Queue()
    to_process.enqueue(start_node)
    result = []
    while not to_process.is_empty():
        current = to_process.dequeue()
        if current is not None:
            result.append(current.item)
            to_process.enqueue(current.left)
            to_process.enqueue(current.right)
    return result


print(level_order_rec(root, None))


def level_sum(start_node):
    if start_node is None:
        return 0
    to_process = Queue()
    to_process.enqueue(start_node)
    result = []
    level, sum = 0, 0
    while not to_process.is_empty():
        for i in range(to_process.size()):
            if to_process.is_empty(): break
            current_node = to_process.dequeue()
            sum += current_node.item
            if current_node.left is not None:
                to_process.enqueue(current_node.left)
            if current_node.right is not None:
                to_process.enqueue(current_node.right)
        result.append((level, sum))
        sum = 0
        level += 1
    return result


def level_sum_inden(start_node):
    if start_node is None:
        return {}
    result = {}
    to_process = Queue()
    to_process.enqueue((start_node, 0))
    while not to_process.is_empty():
        current_node_and_level = to_process.dequeue()
        current_node = current_node_and_level[0]
        level = current_node_and_level[1]
        if level not in result:
            result[level] = 0
        result[level] += current_node.item
        if current_node.left is not None:
            to_process.enqueue((current_node.left, level + 1))
        if current_node.right is not None:
            to_process.enqueue((current_node.right, level + 1))
    return result


def make_tree_level_sum():
    _4 = BinaryTreeNode(4)
    _2 = BinaryTreeNode(2)
    _6 = BinaryTreeNode(6)
    _1 = BinaryTreeNode(1)
    _3 = BinaryTreeNode(3)
    _5 = BinaryTreeNode(5)
    _8 = BinaryTreeNode(8)
    _7 = BinaryTreeNode(7)
    _9 = BinaryTreeNode(9)
    _4.left = _2
    _4.right = _6
    _2.left = _1
    _2.right = _3
    _6.left = _5
    _6.right = _8
    _8.left = _7
    _8.right = _9
    return _4


def level_sum_depth_first(root):
    results = {}
    traverse_depth_first(root, 0, results)
    return dict(sorted(results.items()))


def traverse_depth_first(current_node, level, results):
    if current_node:
        # preorder
        traverse_depth_first(current_node.left, level + 1, results)
        # inorder
        results[level] = results.get(level, 0) + current_node.item
        traverse_depth_first(current_node.right, level + 1, results)
        # postorder


root = make_tree_level_sum()
print(level_sum(root))
print(level_sum_inden(root))
print(level_sum_depth_first(root))


def rotate_left(node):
    if node.right is None:
        raise ValueError("Can't rotate left when root does not have a right child.")
    rc = node.right
    rlc = node.right.left
    rc.left = node
    node.right = rlc
    return rc


def rotate_right(node):
    if node.left is None:
        raise ValueError("Can't rotate right when root does not have a left child.")
    lc = node.left
    lrc = node.left.right
    lc.right = node
    node.left = lrc
    return lc


def main():
    root = create_example_tree()
    print_existing_tree(root)
    print("\nRotate left")
    left_rotated_root = rotate_left(root)
    print_existing_tree(left_rotated_root)
    print("\nRotate right")
    right_rotated_root = rotate_right(rotate_right(left_rotated_root))
    print_existing_tree(right_rotated_root)


main()


def construction(values):
    if not values:
        return None
    mid_idx = len(values) // 2
    mid_value = values[mid_idx]
    new_node = BinaryTreeNode(mid_value)
    if len(values) == 1:
        return new_node
    new_node.left = construction(values[0:mid_idx])
    # can't say [mid_idx+1:] because length of values changes
    new_node.right = construction(values[mid_idx + 1:len(values)])
    return new_node


list_one = [1, 2, 3, 4, 5, 6, 7]
list_tow = [1, 2, 3, 4, 5, 6, 7, 8]
print('Here is list_one in Tree form: ')
print_existing_tree(construction(list_one))
print('Here is list_two in Tree form: ')
print_existing_tree(construction(list_one))
###########################
list_one_preorder = [4, 2, 1, 3, 6, 5, 7]
list_one_inorder = [1, 2, 3, 4, 5, 6, 7]


def reconstruct_clearer(preorder_values, inorder_values):
    if not preorder_values or not inorder_values:
        return None
    root_value = preorder_values[0]
    root = BinaryTreeNode(root_value)
    if len(preorder_values) == 1 and len(inorder_values) == 1:
        return root
    index = inorder_values.index(root_value)
    left_inorder = inorder_values[0:index]
    # todo -- why not inorder_values[index+1:]? test it later
    # right_inorder = inorder_values[index+1:]
    right_inorder = inorder_values[index + 1:len(inorder_values)]
    left_preorder = preorder_values[1:1 + index]
    right_preorder = preorder_values[1 + index:]
    # right_preorder = preorder_values[1+index:len(preorder_values)]
    root.left = reconstruct_clearer(left_preorder, left_inorder)
    root.right = reconstruct_clearer(right_preorder, right_inorder)
    return root


print_existing_tree(reconstruct_clearer(list_one_preorder, list_one_inorder))


##################### a very interesting algorithm using python list comprehension
def reconstruct_from_preorder_bst(preorder_values):
    if not preorder_values:
        return None
    root_value = preorder_values[0]
    root = BinaryTreeNode(root_value)
    # spliting
    left_values = [value for value in preorder_values if value < root_value]
    right_values = [value for value in preorder_values if value > root_value]
    root.left = reconstruct_from_preorder_bst(left_values)
    root.right = reconstruct_from_preorder_bst(right_values)
    return root


print_existing_tree(reconstruct_from_preorder_bst(list_one_preorder))


################################Exercise Nine###################################
def create_math_expression_tree():
    _plus_sign = BinaryTreeNode('+')
    _3 = BinaryTreeNode('3')
    _mult_sign = BinaryTreeNode('*')
    _7 = BinaryTreeNode('7')
    _minus_sign = BinaryTreeNode('-')
    second_7 = BinaryTreeNode('7')
    _1 = BinaryTreeNode('1')
    _plus_sign.left = _3
    _plus_sign.right = _mult_sign
    _mult_sign.left = _7
    _mult_sign.right = _minus_sign
    _minus_sign.left = second_7
    _minus_sign.right = _1
    return _plus_sign


def math_operator(node):
    if node is None:
        return None
    elif node.left is None and node.right is None:
        return node.item
    elif node.left is None:
        return node.right
    elif node.right is None:
        return node.left
    left_result = math_operator(node.left)
    right_result = math_operator(node.right)
    if left_result is not None and right_result is not None:
        return apply_operation(left_result, node.item, right_result)
    return None


def apply_operation(left_result, operator, right_result):
    if operator == '+':
        return int(left_result) + int(right_result)
    elif operator == '-':
        return int(left_result) - int(right_result)
    elif operator == '*':
        return int(left_result) * int(right_result)
    elif operator == '/':
        return int(left_result) / int(right_result)
    else:
        raise ValueError(operator, ' is not supported.')


# Here is how book did it...
def evaluate(root):
    value = root.item
    if value == '+':
        return evaluate(root.left) + evaluate(root.right)
    elif value == '-':
        return evaluate(root.left) - evaluate(root.right)
    elif value == '*':
        return evaluate(root.left) * evaluate(root.right)
    elif value == '/':
        return evaluate(root.left) / evaluate(root.right)
    else:
        return int(value)


root = create_math_expression_tree()
print('Here is what the math operations tree looks like: ')
print_existing_tree(root)
result = math_operator(root)
print(result)

result = evaluate(root)
print("Here is the result of my copy of book's method")
print(result)


def evaluate_v2(node):
    value = node.item
    match value:
        case "+" | "-" | "*" | "/":
            val1 = evaluate_v2(node.left)
            val2 = evaluate_v2(node.right)
            return eval(str(val1) + value + str(val2))
        case _:
            return int(value)


result = evaluate_v2(root)
print("Here is the outcome of Evaluate Function - version two: ")
print(result)


######################################################################
# this tree passes the structural symmetry test but fails the value check
def create_tree_for_symmetry():
    _1 = BinaryTreeNode(1)
    _2 = BinaryTreeNode(2)
    _2_second = BinaryTreeNode(2)
    _3 = BinaryTreeNode(3)
    _3_second = BinaryTreeNode(4)
    _1.left = _2
    _1.right = _2_second
    _2.left = _3
    _2_second.right = _3_second
    return _1


symmetric_root = create_tree_for_symmetry()
print_existing_tree(symmetric_root)


def symmetry(node):
    if node is None:
        return True
    return symmetry_helper(node.left, node.right)


def symmetry_helper(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return symmetry_helper(left.left, right.right) and symmetry_helper(left.right, right.left)


print(symmetry(symmetric_root))


def symmetry_v2(node):
    if node is None:
        return True
    return symmetry_helper_for_value(node.left, node.right, False)


def symmetry_helper_for_value(left, right, check_value):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    check_value = left.item == right.item
    return check_value and symmetry_helper_for_value(left.left, right.right, check_value) and symmetry_helper_for_value(
        left.right, right.left, check_value)


print(symmetry_v2(symmetric_root))


# this is books implementation of check value:
def check_if_nodes_and_values_are_symmetric(left, right, check_value):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    # check values
    if check_value and not left.item == right.item:
        return False
    return (check_if_nodes_and_values_are_symmetric(left.right, right.left, check_value) and
            check_if_nodes_and_values_are_symmetric(left.left, right.right, check_value))


def invert(root):
    if root is None:
        return None
    invert_left = invert(root.left)
    invert_right = invert(root.right)
    root.right = invert_left
    root.left = invert_right
    return root


def invert_clearer(root):
    if root is None:
        return None
    root.left, root.right = invert_clearer(root.right), invert_clearer(root.left)
    return root


print('Here is the symmetric root: ')
print_existing_tree(symmetric_root)

print('Here is the mirror image of symmetric root:')
print_existing_tree(invert(symmetric_root))
print('Here is the output of invert_clearer: ')
print_existing_tree(invert_clearer(symmetric_root))


#################################check binary search exercise################################
def is_bst(node):
    if node is None:
        return True
    if node.is_leaf():
        return True
    if node.left.item > node.right.item:
        return False
    else:
        return is_bst(node.left) and is_bst(node.right)


def is_bst_book(node):
    if node is None:
        return True
    if node.is_leaf():
        return True
    is_left_bst = True
    is_right_bst = True
    is_left_bst = is_bst_book(node.left) and node.left.item < node.item
    is_right_bst = is_bst_book(node.right) and node.right.item > node.item
    return is_left_bst and is_right_bst


def is_bst_latest(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not min_val < node.item < max_val:
        return False
    return is_bst_latest(node.left, min_val, node.item) and is_bst_latest(node.right, node.item, max_val)


root = make_tree_level_sum()
print_existing_tree(root)
print(is_bst_latest(root))
root = make_int_tree()
print_existing_tree(root)
print(is_bst_latest(root))


#########################################completeness#######################################3
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def is_full(node):
    if node is None:
        return True
    return is_full_helper(node.left, node.right)


def is_full_helper(left_node, right_node):
    if left_node is None and right_node is None:
        return True
    if left_node is not None and right_node is not None:
        return is_full(left_node) and is_full(right_node)
    return False


def is_perfect(node):
    if node is None:
        return True
    height = get_height(node)
    return is_perfect_helper(node.left, node.right, height, 1)


def is_perfect_helper(left_node, right_node, height, current_level):
    if left_node is None or right_node is None:
        return False
    if left_node.is_leaf() and right_node.is_leaf():
        return on_the_same_height(left_node, right_node, height, current_level)
    return (is_perfect_helper(left_node.left, right_node.right, height, current_level + 1) and
            is_perfect_helper(right_node.left, right_node.right, height, current_level + 1))


def on_the_same_height(left_node, right_node, height, current_level):
    return get_height(left_node) + current_level == height and get_height(right_node) + current_level == height


########################################################################################################


def is_tree_perfect(node):
    if node is None:
        return True
    height = get_height(node)
    return perfect_helper(node.left, node.right, height, 1)


def perfect_helper(left, right, height, level):
    if left is None or right is None:
        return False
    if left.is_leaf() and right.is_leaf():
        return on_same_height(left, right, height, level)
    return perfect_helper(left.left, left.right, height, level + 1) and perfect_helper(right.left, right.right, height,
                                                                                       level + 1)


def on_same_height(left, right, height, current_level):
    return current_level + get_height(left) == height and current_level + get_height(right) == height


def make_tree_for_perfect():
    _4 = BinaryTreeNode(4)
    _2 = BinaryTreeNode(2)
    _6 = BinaryTreeNode(6)
    _1 = BinaryTreeNode(1)
    _3 = BinaryTreeNode(3)
    _5 = BinaryTreeNode(5)
    _7 = BinaryTreeNode(7)
    _4.left = _2
    _4.right = _6
    _2.left = _1
    _2.right = _3
    _6.left = _5
    _6.right = _7
    return _4


root = make_tree_for_perfect()
print_existing_tree(root)
print("#nodes: ", count_nodes(root))
print("is full?:", is_full(root))
print("is perfect?: ", is_tree_perfect(root))


####################################################################Complete Tree
def complete_tree(node):
    if node is None:
        return True
    height = get_height(node)
    return complete_tree_helper(node.left, node.right, height, 1)


def complete_tree_helper(left, right, height, current_level):
    if left is None and right is None:
        return True
    if left is None and right is not None:
        return False
    if (left.is_leaf() or right.is_leaf()) and height - current_level > 1:
        return False
    if left.is_leaf() and right.is_leaf():
        return nodes_are_on_same_level(left, right, height, current_level)
    return (complete_tree_helper(left.left, left.right, height, current_level + 1) and
            complete_tree_helper(right.left, right.right, height, current_level + 1))


def nodes_are_on_same_level(left, right, height, current_level):
    return get_height(left) + current_level == height and get_height(right) + current_level == height


def create_complete_tree():
    _4 = BinaryTreeNode(4)
    _2 = BinaryTreeNode(2)
    _6 = BinaryTreeNode(6)
    _1 = BinaryTreeNode(1)
    _3 = BinaryTreeNode(3)
    _5 = BinaryTreeNode(5)
    _7 = BinaryTreeNode(7)
    _4.left = _2
    _4.right = _6
    _2.left = _1
    _2.right = _3
    _6.left = _5
    _6.right = _7
    return _4


root = create_complete_tree()
print_existing_tree(root)
print('Expected answer is True, actual answer: ', complete_tree(root))


def create_incomplete_tree():
    _4 = BinaryTreeNode(4)
    _2 = BinaryTreeNode(2)
    _6 = BinaryTreeNode(6)
    _1 = BinaryTreeNode(1)
    _3 = BinaryTreeNode(3)
    _5 = BinaryTreeNode(5)
    _7 = BinaryTreeNode(7)
    _4.left = _2
    _4.right = _6
    _2.left = _1
    _2.right = _3
    # _6.left = _5
    _6.right = _7
    return _4


root = create_incomplete_tree()
print_existing_tree(root)
print('Expected answer is False, actual answer: ', complete_tree(root))


def create_incomplete_tree_v2():
    _4 = BinaryTreeNode(4)
    _2 = BinaryTreeNode(2)
    _6 = BinaryTreeNode(6)
    _1 = BinaryTreeNode(1)
    _3 = BinaryTreeNode(3)
    _5 = BinaryTreeNode(5)
    _7 = BinaryTreeNode(7)
    _4.left = _2
    _4.right = _6
    _2.left = _1
    _2.right = _3
    # _6.left = _5
    # _6.right = _7
    _1.left = _5
    _1.right = _7
    return _4


root = create_incomplete_tree_v2()
print_existing_tree(root)
print('Expecting this to be False: ', complete_tree(root))
