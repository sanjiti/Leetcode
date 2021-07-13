class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1
        count = 0
        if nums==[]:
            return 0
        while p2 != len(nums):
            if nums[p1] == nums[p2]:
                p2+=1
                
            else:
                nums[p1+1] = nums[p2]
                p1+=1
                p2+=1
                count+=1
        return count+1
    