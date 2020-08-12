# https://practice.geeksforgeeks.org/problems/inorder-traversal/1
# 
def inorder(root):
    lst = []
    if root:
        lst = inorder(root.left)
        lst.append(root.data)
        lst.extend(inorder(root.right))
    return lst
#iterative using stack
def inorder(root):
    ans,stack=[],[]
        while True:
            
            while root:
                stack.append(root)
                root=root.left
            if stack:
                node=stack.pop()
                ans.append(node.val)
                root=node.right
            else:
                return ans
# 
 def inorderTraversal(self, root):
        ans,stack=[],[(root,False)]
        
        while stack:
            node,visited=stack.pop()
            if node:
                if visited:
                    ans.append(node.val)
                else:
                    stack.extend([(node.right,False),(node,True),(node.left,False)]) #  a little change to make is post order
                    
        return ans
            
# threaded order traversal
        
#---------------------------------------------------------------------------------
# https://practice.geeksforgeeks.org/problems/postorder-traversal/1
# https://leetcode.com/problems/binary-tree-postorder-traversal/
def postorder(root):
    lst = []
    if root:
        lst = postorder(root.left)
        lst.extend(postorder(root.right))
        lst.append(root.data)
    return lst
# idea here is traverse preorder and visit right child first followed by left child
# limitation is : we are not actually visiting the tree's node in post rather just printing the correct 
# traversal result
#if you are asked to do some task by traversing the tree in the post order (say, free a tree), you cannot use this algorithm
#if there are topological dependencies among the nodes, the visiting order would be significant. Simply reversing the preorder result isn't right.
def postorder(root):
    stack=[root]
        ans=[]
        while stack:
            node =stack.pop()
            if node:
                ans.append(node.val)
                stack.extend([node.left,node.right])
        return ans[::-1]
# to overcome the limitation of avove post order traversal 

def postorder(root):
    ans,stack=[],[(root,False)]
        
    while stack:
        node,visited=stack.pop()
        if node:
            if visited:
                ans.append(node.val)
            else:
                stack.extend([(node,True),(node.right,False),(node.left,False)])
    return ans
            
#-------------------------------------------------------------------------
 
def preorder(root):
    lst = []
    if root:
        lst.append(root.data)
        lst.extend(preorder(root.left))
        lst.extend(preorder(root.right))
    return lst
# iterative preorder
def preorder(root):
    lst = []
    if root:
        stack=[root]
        while stack:
            node=stack.pop()
            if node :
                lst.append(node.data)
                stack.extend([node.right,node.left])
    return lst

