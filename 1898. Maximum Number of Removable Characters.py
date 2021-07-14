class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def issubarray(s, subseq):
            p1,p2 = 0,0
            while p1<len(s) and p2<len(subseq):
                if p1 in removed or s[p1] != subseq[p2]:
                    p1+=1
                    continue
                p1+=1
                p2+=1
            return p2 == len(subseq)
            
        
        res = 0
        l,r = 0, len(removable) -1
        while l<=r:
            m = (l+r)//2
            removed = set(removable[:m+1])
            if issubarray(s,p):
                res = max(res,m+1)
                l = m+1
                
            else:
                r = m-1
        return res