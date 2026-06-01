class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        op=[]
        mk=Counter(nums).most_common(k)

        for num,count in mk:
            op.append(num)
        return op
            