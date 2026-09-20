class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        n=None
        for k in dict:
            if dict[k]==1:
                n=k
                break
        if n is None:
            return -1
        for i in range(len(s)):
            if s[i]==n:
                return i