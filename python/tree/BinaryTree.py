from BinaryTreeNode import BinaryTreeNode


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


# prints tree using in-order
def print_existing_tree(current_node):
    if current_node.left is not None:
        print_existing_tree(current_node.left)
    print(current_node.item, end=' ')
    if current_node.right is not None:
        print_existing_tree(current_node.right)


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


_3 = BinaryTreeNode(3)
insert(_3, 3)
insert(_3, 2)
insert(_3, 4)
print_existing_tree(_3)
print('\nTree contains 2? ', find(_3, 2))
print('\nTree contains 13? ', find(_3, 13))
preorder(_3)
