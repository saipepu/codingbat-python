def lucky_sum(a, b, c):
  sum = 0
  for x in [a,b,c]:
    if x != 13:
      sum += x
    else:
      break
  return sum

print(lucky_sum(1,13,3))