 def preorderTraversal(self, root):
        list=[]
        def getting(root):
		#Checking if you reach the end of the node then you return
            if root==None:
                return  
			#Adding value
            list.append(root.val)
			#You go the left of the node first. When you reach the end of the left node the condition above will make sure you will return
            getting(root.left)
			#After finishing execute the rest of the left direction. It will return to this node and excute the right direction
            getting(root.right)
        getting(root)
        return list
