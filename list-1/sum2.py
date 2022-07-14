def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 0:
    return 0
  else:
    return nums[0]

print('sum2 of [1,2,3] -> ', sum2([1,2,3]))