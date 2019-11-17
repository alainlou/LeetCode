class FindElements:
    
    def __init__(self, root: TreeNode):
        self.nums = set([0])
        if root.left != None:
            self.populate(root.left, 1)
        if root.right != None:
            self.populate(root.right, 2)

    def populate(self, node: TreeNode, value: int):
        self.nums.add(value)
        if node.left != None:
            self.populate(node.left, 2*value+1)
        if node.right != None:
            self.populate(node.right, 2*value+2)        
        
    def find(self, target: int) -> bool:
        return target in self.nums