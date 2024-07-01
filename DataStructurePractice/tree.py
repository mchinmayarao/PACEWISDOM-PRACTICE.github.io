class Tree:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

     # Insert Node
    def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Tree(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Tree(data)
            else:
               self.right.insert(data)
      else:
         self.data = data
# Print the Tree
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)  
         res = res + self.inorderTraversal(root.right) #list concatination
      return res
    
# Root -> Left-> Right
    def preorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data) 
         res = res + self.preorderTraversal(root.left)
         res = res + self.preorderTraversal(root.right)
      return res
# Left-> Right -> Root
    def postorderTraversal(self, root):
      res = []
      if root:
         
         res = self.postorderTraversal(root.left)
         res = res + self.postorderTraversal(root.right)
         res.append(root.data) 
      return res

root = Tree(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.postorderTraversal(root))

def isBalanced(root):
    #the base condition is when a leaf node is encounterd
    #the leaf node is always balanced and the height is 0
    if root == None:
        return [True, 0]
    
    #recursive call is done until the leaf node is reached of both left
    #and right subtree
    left, right = isBalanced(root.left), isBalanced(root.right)

    #checking if the lower left and the right subtree are balanced 
    #along with current balance condition by calculating the difference
    #between the height of the left and right subtree i.e it should be 
    #always <= 1
    balanced = left[0] and right[0] and (abs(right[1] - left[1]))<=1

    #returning the balance of the tree along with the height of the tree
    return [ balanced , max(left[1], right[1])+1 ]


# isBalanced() testing code 
# root = Tree(1)
# root.left = Tree(2)
# root.right = Tree(3)
# root.left.left = Tree(4)
# root.left.right = Tree(5)

# print(isBalanced(root))


    
