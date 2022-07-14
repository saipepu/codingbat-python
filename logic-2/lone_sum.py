def lone_sum(a, b, c):
  arr = [a,b,c]
  sum = 0
  for x in arr:
    if arr.count(x) == 1:
      sum += x
  return sum


print(lone_sum(3,2,3))