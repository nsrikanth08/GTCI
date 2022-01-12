class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def all_paths(root, sum):
    result = []
    find_paths_rec(root, sum, [], result)
    return result

def find_paths_rec(root, sum, current, result):
    if root is None:
        return
    
    current.append(root.val)

    if root.val == sum and root.left is None and root.right is None:
        result.append(list(current))
    
    else:
        find_paths_rec(root.left, sum - root.val, current, result)
        find_paths_rec(root.right, sum - root.val, current, result)
    
    del current[-1]
    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
            ": " + str(all_paths(root, required_sum)))

if __name__ == "__main__":
    main()