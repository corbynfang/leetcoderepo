# Contains Duplicates
# Set: is one of the 4 built-in data types in python used to store collections of data, the other 3 are List, Tuples, and Dicts.

# Problem: Check the list for duplicates
# Soultion: Time and Space O(N): iterate through the list and create a set, Space = size of set
# Sets are fast, Note that a empty Set cannot be created through [], it creates a dicts, unless you use varaiables

# This soultion is really slow. Need to make it faster by using algo.
def containsDuplicates(self, nums: List[int]) -> bool:
    if len(set(num)) == len(nums):
        return False
    else:
        return True


# Sorting Approach
def containsDuplicates(self, nums: List[int]) -> bool:
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i-1]:
            return True
    return False

# Hash Sets Approach (kidna like the first approach but more effiecent)
def containsDuplicates(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Using a Hash Map with dict / We iterate through the array and store each element as a key in a hash map. The value is associated with each key represents the count of occurrences of that element.
def containsDuplicates(self, nums: List[int]) -> bool:
    seen = {}
    for num in nums:
        if num in seen and seen[num] >= 1:
            return True
        seen[num] = seen.get(num, 0) + 1
    return False
