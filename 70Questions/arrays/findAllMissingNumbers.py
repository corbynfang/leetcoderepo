# Problem: Check the given list for missing numbers range(1, len(nums))
# Soultion: Time: O(n): iterate through the range and append the new list if not in given list: O(n) space.

# This Soultion is O(n) space
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    set_nums = set(nums)
    returned = []

    for i in range(1, len(nums) + 1): # iterate through the array using for loop
        if i not in set_nums:
            returned.append(i) # append
    return returned

# Notes
# This soultion is O(1) space (Constant space soultion)
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1

    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i+1)
    return res
