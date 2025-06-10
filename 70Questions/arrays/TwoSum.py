 # Notes
 # Look to reduce repeated code for clearliness and readability
 def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i, v in enumerate(nums):
        if target-v in hash_map:
            return i, hash_map[target-v]
        else:
            hash_map[v] = i

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for index, val in enumerate(nums):
        diff = target - val
        if diff in hashMap:
            return [index, hashMap[diff]]
        hashMap[val] = index
