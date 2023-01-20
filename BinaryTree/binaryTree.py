class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


binaryTree = TreeNode("Drinks")
binaryTree.left = TreeNode("Hot")
binaryTree.right = TreeNode("Cold")


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)


preOrderTraversal(binaryTree)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data) 
    inOrderTraversal(rootNode.right)


inOrderTraversal(binaryTree)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data) 

postOrderTraversal(binaryTree)
