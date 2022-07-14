def no_teen_sum(a, b, c):
  sum = 0
  for x in [a,b,c]:
    y = fix_teen(x)
    sum += y
  return sum

def fix_teen(n):
  if n >=13 and n<=19 and n!=15 and n!=16:
    return 0
  else:
    return n

print(no_teen_sum(2,13,1))