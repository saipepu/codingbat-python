def same_first_last(nums):
  if nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False

print(same_first_last([1,2,1]))