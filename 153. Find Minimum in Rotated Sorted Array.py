class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        res = nums[0]
        while l<= r:
            mid = (l+r)//2
            res = min(nums[mid], res)
            if nums[l] < nums[r]:
                res = min (res, nums[l])
                break
            if nums[l] <= nums[mid]:
                l = mid +1
            else:
                r = mid -1
        return res