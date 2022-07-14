def sum67(nums):
  sum = 0
  toggle = False
  for x in nums:
    if x == 6:
      toggle = True
    if toggle == False:
      print(x)
      sum += x
    elif x == 7:
      toggle = False
  return sum

print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))