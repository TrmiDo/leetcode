def levelOrder(self, root):
        list=[]
        def getting(root,level):
            if root==None:
                return
            if level>=len(list):
                list.append([])
            list[level].append(root.val)
            getting(root.left,level+1)
            getting(root.right,level+1)
        getting(root,0)
        return list
        
