class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward=[]
        prd=1
        for i in nums:
            prd=prd*i
            forward.append(prd)
        
        backward=[]
        prd=1
        for i in nums[::-1]:
            prd=prd*i
            backward.append(prd)
        backward=backward[::-1]

        op=[backward[1]]
        for i in range(1,len(nums)-1):
            op.append(forward[i-1]*backward[i+1])
        op.append(forward[-2])

        return op