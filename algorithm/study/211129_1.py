class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
root = BST(30)
root.left, root.right = BST(20), BST(40)
root.left.left, root.left.right = BST(10), BST(25)
root.right.left, root.right.right = BST(35), BST(45)

#오름차순으로 출력
def bst_sorted(bst):
    if not bst:
        return

    bst_sorted(bst.left)
    print(bst.key)
    bst_sorted(bst.right)
print(bst_sorted(root))

#내림차순으로 출력
def bst_sorted_reverse(bst):
    if not bst:
        return

    bst_sorted_reverse(bst.right)
    print(bst.key)
    bst_sorted_reverse(bst.left)
print(bst_sorted_reverse(root))