class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if ((nums[0] + nums[1] > nums[2]) == False):
            return 'none'


        dic = dict()
        for i in nums:
            if i not in dic:
                dic[i] = 1
        return_dic = {1: "equilateral", 2: "isosceles", 3:"scalene"}

        return return_dic[len(dic)]