def canConstruct(self, ransomNote, magazine):
        if len(magazine)<len(ransomNote):
            return False
        for char in magazine:
            if char in ransomNote:
                ransomNote= ransomNote.replace(char,"",1)
        if len(ransomNote)>0:
            return False
        else:
            return True
