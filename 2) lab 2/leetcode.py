class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx=[]
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if(nums[i] + nums[j+1] == target):
                    idx.append(i)
                    idx.append(j+1)
                    break
            
        return idx


s1 = Solution()
nums = [2,5,5,11]
target = 10
index = s1.twoSum(nums, target)
print(index)

        