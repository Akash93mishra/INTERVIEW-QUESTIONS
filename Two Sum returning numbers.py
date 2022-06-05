nums = [2, 8, 4, 7, 20]
target = 22
def twoSum(nums, target):
      map_dict = {}
      for i in range(len(nums)):
         if target - nums[i] in map_dict:
            return [map_dict[target - nums[i]], nums[i]]
         else:
            map_dict[nums[i]] = nums[i]
print(twoSum(nums, target))

