def isSymmetric(self, root):
    list=[]
    def check(root1,root2):
        if root1==None and root2==None:
            return
        elif root1==None or root2==None:
            list.append(1)
            return
        if root1.val!=root2.val:
            list.append(1)
            return
        check(root1.left,root2.right)
        check(root1.right,root2.left)
    
    check(root.left,root.right)
    if 1 in list:
        return False
    else:
        return True
