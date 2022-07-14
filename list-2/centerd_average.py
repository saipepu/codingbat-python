def centered_average(nums):
  Max = max(nums)
  Min = min(nums)
  del nums[nums.index(Max)]
  del nums[nums.index(Min)]
  for x in nums:
    if nums.count(x) >= 2:
      del nums[nums.index(x)]
  sum = 0
  for x in nums:
    sum += x
  return int(sum/len(nums))

print(centered_average([1,1,5,5,10,8,7]))