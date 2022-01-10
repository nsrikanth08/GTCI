from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse(root):
    result = []
    if root is None:
        return result
    direction = True
    queue = deque()
    queue.append(root)
    while queue:
        currentLevel = deque()
        levelSize = len(queue)
        for _ in range(0, levelSize):
            current = queue.popleft()
            if direction:
                currentLevel.append(current.val)
            else:
                currentLevel.appendleft(current.val)
                
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(list(currentLevel))
        direction = not direction
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Level order traversal: " + str(traverse(root)))

if __name__ == "__main__":
    main()