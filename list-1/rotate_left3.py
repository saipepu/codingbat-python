def rotate_left3(nums):
  result = []
  for x in range(len(nums)):
    if x != 0:
      result.append(nums[x])
  result.append(nums[0])
  return result

print('[1, 2, 3] -> ', rotate_left3([1, 2, 3]))

#using del method
def rotate_left3(nums):
  x = nums[0]
  del nums[0]
  nums.append(x)
  return nums

print('[4, 2, 3] -> ',rotate_left3([4, 2, 3]))
