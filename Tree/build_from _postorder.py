# one can't build a tree without inorder , 
# inorder and any one of pre or post is sufficient
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/810963/beginner-Friendly-or-recursive-or-O(N2)-to-O(N)-or-handles-duplicates-values
# preorder is passed in reversed order to make pop O(1)
# code : Time O(N^2)
 def binaryTree(inorder,preorder):
    if inorder:
        root=inorder.index(preorder.pop())
        new=TreeNode(inorder[root])
        new.left=binaryTree(inorder[:root],preorder)
        new.right=binaryTree(inorder[root+1:],preorder)
        return new

        
# O(N) solution with hashmap handles duplicates
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def binaryTree(beg,end,preorder):
            if beg<=end:
                root=TreeNode(preorder.pop())
                pos=self.index[root.val].popleft()
                root.left=binaryTree(beg,pos-1,preorder)
                root.right=binaryTree(pos+1,end,preorder)
                return root
        
        
        self.index=collections.defaultdict(collections.deque)
        for i,val in enumerate(inorder):
            self.index[val].append(i)
        
        
        
        return binaryTree(0,len(preorder)-1,preorder[::-1])