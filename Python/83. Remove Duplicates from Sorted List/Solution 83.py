def deleteDuplicates(self, head):
        def remove(head,val):
            if head:
                if head.val==val:
                    return remove(head.next,head.val)
                else:
                    head.next=remove(head.next,head.val)
            return head
        return remove(head,"a")
