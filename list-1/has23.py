def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False

print('has 2 or 3 in [4, 5] -> ', has23([4,5]))