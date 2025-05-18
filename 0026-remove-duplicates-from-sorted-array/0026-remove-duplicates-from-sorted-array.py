class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        len_nums=len(nums)
        k=0
        while i<len_nums:
            if nums.count(nums[i])>1:
                nums.remove(nums[i])
                len_nums=len(nums)
            else:
                k=k+1
            i=i+1
        return k