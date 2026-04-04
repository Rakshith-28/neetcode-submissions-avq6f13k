class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i in c:
                c[i]=c[i]+1
            else:
                c[i]=1
        
        s=sorted(c,key=c.get)
        return s[-k:]