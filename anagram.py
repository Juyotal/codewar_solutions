class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
   
        for c in t:
            if c not in count or count[c] == 0:
                return False
            else:
                count[c] -= 1
                
        return True
        

        