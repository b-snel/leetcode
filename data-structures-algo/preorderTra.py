class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root, handler=None):
    """
    Performs a preorder traversal of a binary tree with a custom handler function.
    
    Args:
        root: The root node of the binary tree
        handler: A function that processes each node's value (default: None)
                If None, values are collected in a list
    
    Returns:
        List of values if no handler is provided, otherwise None
    """
    if handler is None:
        result = []
        def default_handler(val):
            result.append(val)
        handler = default_handler
    
    def preorder(node):
        if not node:
            return
        
        handler(node.val)  # Process current node
        preorder(node.left)  # Process left subtree
        preorder(node.right)  # Process right subtree
    
    preorder(root)
    return result if handler == default_handler else None

# Example usage:
if __name__ == "__main__":
    # Create a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Example 1: Default behavior - collect values in a list
    result = preorderTraversal(root)
    print("Default traversal:", result)  # Expected: [1, 2, 4, 5, 3]
    
    # Example 2: Custom handler that prints values
    preorderTraversal(root, lambda x: print(x, end=" "))  # Prints: 1 2 4 5 3
