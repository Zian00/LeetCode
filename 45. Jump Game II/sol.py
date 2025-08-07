class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        curr_end = 0
        furthest = 0

        for i in range(len(nums) -1):
            furthest = max(furthest, i+nums[i])
            if i == curr_end:
                jump_count += 1
                curr_end = furthest
        return jump_count