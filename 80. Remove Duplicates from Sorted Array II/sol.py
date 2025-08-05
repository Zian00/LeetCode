class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        count = 1
        for j in range(1, len(nums)):

            if nums[i] == nums[j] and count < 2:
                i += 1
                nums[i] = nums[j]
                count += 1
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                count = 1

        return i + 1
