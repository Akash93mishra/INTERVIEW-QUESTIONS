nums = [ 3, 1, 2, 4, 5 ]
target = 12
def threesum(nums, n, sum):
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (nums[i] + nums[j] + nums[k] == sum):
                    print(nums[i], " ",
                          nums[j], " ",
                          nums[k], sep = "")
n = len(nums)
threesum(nums, n, target)



