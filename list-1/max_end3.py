def max_end3(nums):
  first = nums[0]
  last = nums[len(nums) -1]
  if first >= last:
    max = first
  else:
    max = last

  for x in range(len(nums)):
    nums[x] = max
  return nums

print('The result of [4,7,2] -> ', max_end3([4,7,2]))