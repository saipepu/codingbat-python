def big_diff(nums):
  Nmax = max(nums)
  Nmin = min(nums)
  return Nmax-Nmin

#OG way
def og_big_diff(nums):
  largest = 0
  smallest = 0
  for x in nums:
    if largest < x:
      largest = x
    if smallest > x:
      smallest = x
  return largest - smallest