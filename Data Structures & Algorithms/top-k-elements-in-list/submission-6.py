class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mk=Counter(nums).most_common(k)
        op=[]
        for nums,count in mk:
            op.append(nums)
        return op