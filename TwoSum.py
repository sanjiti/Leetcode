class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        //Brute Force Aproach
        for p1 in range(0,len(nums)):
            for p2 in range(p1+1,len(nums)):
                if nums[p1]+nums[p2]==target:
                    return([p1,p2])
                    
                p2+=1
            p1+=1
            
        """
        hashdict = dict()
        for p1 in range(0,len(nums)):
            n=target-nums[p1]
            if n not in hashdict.keys():
                hashdict[nums[p1]] = p1
                
            else:
                return [p1, nums.index(n)]
            