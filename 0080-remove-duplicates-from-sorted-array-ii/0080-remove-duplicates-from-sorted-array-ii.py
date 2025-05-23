class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in set(nums):
            while nums.count(num)>2:
                nums.remove(num)
        return len(nums)