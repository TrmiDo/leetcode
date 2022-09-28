def longestPalindrome(self, s):
    single=[]
    long=0
    for character in s:
        if character in single:
            single.remove(character)
            long+=2
        else:
            single.append(character)
    if len(single)>0:
        long+=1
    return long
