def firstUniqChar(self, s):
        nonstr=[]
        str=[]
        for char in s:
            if char in nonstr:
                str.append(char)
                nonstr.remove(char)
            elif char in str:
                next
            else:
                nonstr.append(char)
        if len(nonstr)==0:
            return -1
        else:
            return s.index(nonstr[0])
                
