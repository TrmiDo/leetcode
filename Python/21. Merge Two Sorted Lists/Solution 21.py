def mergeTwoLists(self, list1, list2):
        if list1==None:
            return list2
        if list2==None:
            return list1
        if list1.val>list2.val:
            small=list2
            list2=list2.next
        elif list1.val<=list2.val:
            small=list1
            list1=list1.next
        
        small.next=self.mergeTwoLists(list1,list2)
        
        return small 
