def tree_paths_sum(root):
    
    if (root == None): 
        return 0
    return (root.value + tree_paths_sum(root.left) + tree_paths_sum(root.right))