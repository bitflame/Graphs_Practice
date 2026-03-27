from tree.BinaryTreeNode import BinaryTreeNode


def subtree_width(height):
    if height <= 0:
        return 0
    leaf_width = 3
    spacing = 3
    max_num_of_leaves = pow(2, height - 1)
    width_of_tree = max_num_of_leaves * leaf_width + (max_num_of_leaves - 1) * spacing
    width_of_subtree = (width_of_tree - spacing) // 2
    return width_of_subtree


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


def spacing(line_length):
    return " " * line_length


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


def draw_line(line_length):
    return "-" * line_length


def fill_nodes_into_list(start_node):
    height = get_height(start_node)
    nodes = [None] * pow(2, height)
    traverse_and_mark(start_node, nodes, 0)
    return nodes


def traverse_and_mark(start_node, nodes, pos):
    if start_node is None:
        return
    if pos >= len(nodes):
        return
        # action
    nodes[pos] = start_node
    traverse_and_mark(start_node.left, nodes, pos * 2 + 1)
    traverse_and_mark(start_node.right, nodes, pos * 2 + 2)


def nice_print_v1(node):
    if node is None:
        return
    tree_height = get_height(node)
    all_nodes = fill_nodes_into_list(node)
    # traverse level by level
    offset = 0
    lines = []
    for level in range(tree_height):
        line_length = subtree_width(tree_height - 1 - level)
        # indent predecessor lines to the right
        for i in range(len(lines)):
            lines[i] = "   " + spacing(line_length) + lines[i]
        nodes_per_level = pow(2, level)
        node_line = ""
        connection_line = ""
        for pos in range(nodes_per_level):
            current_node = all_nodes[offset + pos]

            node_line += draw_node(current_node, line_length)
            node_line += spacing_between_nodes(tree_height, level)
            connection_line += draw_connections(current_node, line_length)
            connection_line += spacing_between_connections(tree_height, level)

        lines.append(node_line)
        lines.append(connection_line)

        # jump forward in the list
        offset += nodes_per_level

    for line in lines:
        print(line)


def spacing_between_nodes(tree_height, level):
    spacing_length = subtree_width(tree_height - level)
    spacing = " " * spacing_length
    if spacing_length > 0:
        spacing += "   "
    return spacing


def spacing_between_connections(tree_height, level):
    spacing_length = subtree_width(tree_height - level)
    return " " * spacing_length


def get_height(node):
    if node is None:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))


def create_tree():
    _f = BinaryTreeNode('F')
    _d = BinaryTreeNode('D')
    _h = BinaryTreeNode('H')
    _b = BinaryTreeNode('B')
    _i = BinaryTreeNode('I')
    _b = BinaryTreeNode('B')
    _a = BinaryTreeNode('A')
    _c = BinaryTreeNode('C')
    _f.left = _d
    _f.right = _h
    _d.left = _b
    _h.right = _i
    _b.left = _a
    _b.right = _c
    _d.left = _b
    return _f


root = create_tree()
nice_print_v1(root)
