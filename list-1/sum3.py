def sum3(nums):
  sum = 0
  for x in nums:
    sum += x
  return sum

print(f"{'>'*5} Output: ", sum3([1,2,3]) , f"{'<'*5}")