class TreeNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        
        if not self.root:
            self.root = new_node
            return
        
        curr = self.root

        while curr:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
                continue
            elif key > curr.key:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
                continue
            else:
                curr.val = new_node.val
                break

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        
        curr = self.root

        while curr:
            if curr.key == key:
                return curr.val
            elif key < curr.key:
                if curr.left:
                    curr = curr.left
                    continue
                return -1
            elif key > curr.key:
                if curr.right:
                    curr = curr.right
                    continue
                return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root

        while curr:
            if curr.left:
                curr = curr.left
                continue
            return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root

        while curr:
            if curr.right:
                curr = curr.right
                continue
            return curr.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr, key):
        if not curr:
            return None
        
        if key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        elif key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                minNode = self.getMinNode(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr
    
    def getMinNode(self, root) -> int:
        curr = root

        while curr:
            if curr.left:
                curr = curr.left
                continue
            return curr


    def getInorderKeys(self) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.key)
            dfs(root.right)
        
        if self.root:
            dfs(self.root)
        return res
