def searchBST(self, root, val):
    if root==None:
        return 
    if root.val==val:
        return root
    return self.searchBST(root.left,val)or self.searchBST(root.right,val)
    
