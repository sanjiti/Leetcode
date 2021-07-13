class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (r+l)//2
            if target == nums[mid]:
                return mid
            
            #if in left sorted array
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid +1 
                else:
                    r = mid-1
                
            # if in right sorted array
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid +1
        return -1