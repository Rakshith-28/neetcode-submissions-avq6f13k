class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f=[]
        prd=1
        for i in nums:
            prd=prd*i
            f.append(prd)
        
        b=[]
        prd=1
        for i in nums[::-1]:
            prd=prd*i
            b.append(prd)
        b=b[::-1]

        op=[b[1]]
        for i in range(1,len(nums)-1):
            op.append(f[i-1]*b[i+1])
        op.append(f[-2])

        return op