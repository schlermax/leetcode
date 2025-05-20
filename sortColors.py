# Runtime 0 ms | Beats 100%
# Memory 17.56 MB | Beats 97.04%
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        balls = [0,0,0]
        start = 0
        col = 0
        for i in nums:
            balls[i] += 1
        for b in balls:
            for n in range(start, start+b):
                nums[n] = col
            col += 1
            start += b
        
        """loop = True
        while loop:
            loop = False
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    loop = True
                    nums[i], nums[i-1] = nums[i-1], nums[i]"""
                

        