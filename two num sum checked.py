input_list = [2,8,4,7,20]
target = 27
def twoSum(nums, target):
      map_dict = {}
      for i in range(len(nums)):
         if target - nums[i] in map_dict:
            return [map_dict[target - nums[i]],i]
         else:
            map_dict[nums[i]]=i
print(twoSum(input_list, target))

