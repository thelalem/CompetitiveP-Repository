class Solution:
    def doUnion(self,a,n,b,m):
        set_a = set(a)
        set_b = set(b)
        print(len(set_a | set_b))