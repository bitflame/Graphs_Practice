from typing import Optional, List


class TreeNode:
    def __init__(self, val: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        if not root:
            return 0;
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)
        return max(left_depth, right_depth)

    def print_tree(self, node: Optional[TreeNode]):
        if not node:
            return
        print(node.val, end=' ->')
        self.print_tree(node.left)
        # print_list(node.left)
        self.print_tree(node.right)

    def sameTree(self, p: Optional[TreeNode] = None, q: Optional[TreeNode] = None):
        if not p and not q:
            return True
        elif (p and not q) or (q and not p):
            return False
        elif p.val != q.val:
            return False
        left_res = self.sameTree(p.left, q.left)
        right_res = self.sameTree(p.right, q.right)
        return left_res and right_res

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symHelper(root.left, root.right)

    def symHelper(self, left, right):
        if not left and not right:
            # print('Both values are None, setting result to True')
            return True
        elif not left and right or left and not right:
            # print('left is None, and right is: ',right.val)
            return False
        elif left.val == right.val:
            # print("Left value: ", left.val, "Right value: ", right.val)    
            lft_result = self.symHelper(left.left, right.right)
            rt_result = self.symHelper(left.right, right.left)
        else:
            return False
        return lft_result and rt_result

    def buildTree(self, preorder: [List[int]], inorder: [List[int]]):
        # pre_index = 0
        # point out if there is a better way to build a hash table
        tree_map = {}
        for i, val in enumerate(inorder):
            tree_map[val] = i
        pre_index = 0
        inIndex = tree_map[preorder[pre_index]]
        node = TreeNode(preorder[pre_index])
        pre_index += 1
        inStart = 0
        inEnd = inIndex - 1
        pre_index, node.left = self.build_left_subtree(pre_index, preorder, inStart, inEnd, inorder, tree_map)
        pre_index, node.right = self.build_right_subtree(pre_index, preorder, inIndex+1, len(inorder)-1, inorder,tree_map)
        return node

    def build_left_subtree(self, pre_index: int, preorder: [int], inStart: int, inEnd: int, inorder: List[int],
                           tree_map: {}):
        if inStart > inEnd:
            return pre_index, None
        root_val = preorder[pre_index]
        pre_index += 1
        inIndex = tree_map[root_val]
        curr_node = TreeNode(root_val, None, None)
        pre_index, curr_node.left = self.build_left_subtree(pre_index, preorder, inStart, inIndex - 1, inorder,
                                                            tree_map)
        pre_index, curr_node.right = self.build_right_subtree(pre_index, preorder, inIndex + 1, inEnd, inorder,
                                                              tree_map)
        return pre_index, curr_node

    def build_right_subtree(self, pre_index: int, preorder: [int], inStart: int, inEnd: int, inorder: List[int],
                            tree_map: {}):
        if inStart > inEnd:
            return pre_index, None
        root_val = preorder[pre_index]
        pre_index += 1
        inIndex = tree_map[root_val]
        curr_node = TreeNode(root_val, None, None)
        pre_index, curr_node.left = self.build_left_subtree(pre_index, preorder, inStart, inIndex - 1, inorder,
                                                            tree_map)
        pre_index, curr_node.right = self.build_right_subtree(pre_index, preorder, inIndex + 1, inEnd, inorder,
                                                              tree_map)
        return pre_index, curr_node

    def build_Tree_Re(self, preorder: [List[int]], inorder: [List[int]]):
        pre_index = 0
        # point out if there is a better way to build a hash table
        tree_map = {}
        for i, val in enumerate(inorder):
            tree_map[val] = i
        inStart, inEnd = 0, tree_map[preorder[0]] - 1
        pass


print(
    "---------------------------------------Build Tree Preorder/Inorder-------------------------------------------------------")
print(
    "The result should match the preorder sequence due to how print_tree traverses it. Need to build a print tree function.")
s = Solution()
sample_tree = TreeNode(1, TreeNode(2), TreeNode(3))
preorder = [1, 2, 3]
inorder = [2, 1, 3]
res = s.buildTree(preorder, inorder)
print("Test 1  - Build Tree Preorder/Inorder expected:[1,2,3], actual: \n", s.print_tree(res))


sample_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
res = s.buildTree(preorder, inorder)
# print("Test 2 - Build Tree Preorder/Inorder expected:[1,2,3]: actual:", s.print_tree(sample_tree))
print("Test 2 - Build Tree Preorder/Inorder expected:[1,2,3]: actual:", s.print_tree(res))

preorder = [8, 3, 1, 6, 4, 7, 10, 14, 13]
inorder = [1, 3, 4, 6, 7, 8, 10, 13, 14]
res = s.buildTree(preorder, inorder)
print("Test 3  - Build Tree Preorder/Inorder expected:[8, 3, 1, 6, 4, 7, 10, 14, 13], actual: ", s.print_tree(res))


preorder = [-1]
inorder = [-1]
res = s.buildTree(preorder, inorder)
print("Test 4  - Build Tree Preorder/Inorder expected:-1, actual: ", s.print_tree(res))

print(
    "---------------------------------------Symmetric Tree Proble-------------------------------------------------------------")

tee = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
res = s.isSymmetric(tee)
print("Test 1 Is tree symmetric problem - expected True, actual: ", res)

tee = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
res = s.isSymmetric(tee)
print("Test 2 Is tree symmetric problem - expected True, actual: ", res)

# make a test that left.left.val is not the same as right.right.val or left.right.val!=right.left.val
tee = TreeNode(1, TreeNode(2), TreeNode(3))
res = s.isSymmetric(tee)
print("Test 3 Is tree symmetric problem - expected False, actual: ", res)

tee = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, TreeNode(4), None))
# tee = TreeNode(1)
# tee.left=TreeNode(2)
# tee.left.left=TreeNode(3)
# tee.right=TreeNode(2)
# tee.right.left=TreeNode(4)
res = s.isSymmetric(tee)
print("Test 4 Is tree symmetric problem - expected False, actual: ", res)

print(
    "------------------------------------Inverted Tree Problem-------------------------------------------------------------")
tee = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
s.print_tree(tee)
inverted_tree = s.invertTree(tee)
print("Test 1 InvertTree Problem - expected: actual:", end='')
s.print_tree(inverted_tree)
print()
print(
    "-------------------------------------Same Tree Problem----------------------------------------------------------------")
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
same_tree = s.sameTree(p, q)
print("Test 1 - expected: True, actaul: ", same_tree)
p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
same_tree = s.sameTree(p, q)
print("Test 2 - expected: False, actaul: ", same_tree)
l1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
s.print_tree(l1)
result = s.maxDepth(l1)
print("max depth: ", result)
