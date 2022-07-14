def count_evens(nums):
  count = 0
  for x in nums:
    count += checkEvens(x)
  return count

def checkEvens(nums):
  return 1 if nums%2 == 0 else 0

print(count_evens([2,1,2,3,4]))