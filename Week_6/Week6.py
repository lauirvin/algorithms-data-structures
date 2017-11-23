
class BinTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def tree_insert(tree, item):
    if tree == None:
        tree = BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left == None):
                tree.left = BinTreeNode(item)
                tree.left.parent = tree
            else:
                tree_insert(tree.left, item)
        else:
            if(tree.right == None):
                tree.right = BinTreeNode(item)
                tree.right.parent = tree
            else:
                tree_insert(tree.right, item)
    return tree
 # change search to return the needed node and its parent


def searchNode(tree, target):
    if tree.value == target:
        return tree
    elif target < tree.value:
        return searchNode(tree.left, target)
    else:
        return searchNode(tree.right, target)

def deleteNode(tree, value):
    parent = None
    node = searchNode(tree, value)
    
    #case 1: data not found
    if node is None or node.value != value:
        return False

    #case 2: no children
    elif node.left is None and node.right is None:
        if value < node.parent.value:
            node.parent.left = None
        else:
            node.parent.right = None
        return True

    #case 3: left child only

    elif node.left and node.right is None:
        if value < node.parent.value:
            node.parent.left = node.left
        else:
            node.parent.right = node.left
        return True

    #case 4: remove-node has right child only
    elif node.left is None and node.right:
        if value < node.parent.value:
            node.parent.left = node.right
        else:
            node.parent.right = node.right
        return True

    #case 5: remove-node has left and right children
    else:
        delNodeParent = node
        delNode = node.right
        while delNode.left:
            delNodeParent = delNode
            delNode = delNode.left

        node.value = delNode.value
        if delNode.right:
            if delNodeParent.value > delNode.value:
                delNodeParent.left = delNode.right
            elif delNodeParent.value < delNode.value:
                delNodeParent.right = delNode.right
        else:
            if delNode.value < delNodeParent.value:
                delNodeParent.left = None
            else:
                delNodeParent.right = None

def max(self, node):  # finding the max value (from the left subtree)
    root = node
    if node == None:
        node = self.node

    if node.left != None:
        node = node.left
    else:
        return node
    if node.right != None:
        return self.max(node=node.right)


def postorder(tree):
    if(tree.left != None):
        postorder(tree.left)
    if(tree.right != None):
        postorder(tree.right)
    print(tree.value)


def in_order(tree):
    if(tree.left != None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right != None):
        in_order(tree.right)


if __name__ == '__main__':

    t = tree_insert(None, 6)
    tree_insert(t, 10)
    tree_insert(t, 5)
    tree_insert(t, 2)
    tree_insert(t, 3)
    tree_insert(t, 4)
    tree_insert(t, 11)
    #print(searchNode(t, 11).value) - search value
    deleteNode(t, 4) # deleting the node 11
    in_order(t)
