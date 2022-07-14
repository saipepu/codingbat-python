def has22(nums):
  for x in range(len(nums)):
    nums[x] = str(nums[x])
  nums = ''.join(nums)
  return True if '22' in nums else False

print(has22([1,2,2]))