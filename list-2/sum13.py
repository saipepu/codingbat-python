def sum13(nums):
  sum = 0
  if len(nums) == 0:
    return 0
  noSum = False
  for x in nums:
    if x == 13:
      if noSum == True:
        noSum = False
      noSum = True
    else:
      if noSum == True:
        noSum = False
        continue
      print(x)
      sum += x
  return sum

print(sum13([13, 1, 2, 13, 2, 1, 13]))