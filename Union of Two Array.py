class Solution:
    def doUnion(self,a,n,b,m):
        return len(set(a) | set(b))