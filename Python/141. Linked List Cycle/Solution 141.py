def hasCycle(self, head):
        list= set()
        while head:
            if head in list:
                return True
            else:
                list.add(head)
                head=head.next
        return False
