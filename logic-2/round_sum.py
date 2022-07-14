def round_sum(a, b, c):
  sum = 0
  for x in [a,b,c]:
    y = round10(x)
    print(y)
    sum += y
  return sum

def round10(num):
  mod = num % 10
  num -= mod
  if mod >= 5: num += 10
  return num

print(round_sum(16,17,14))