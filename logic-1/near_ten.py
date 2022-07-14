def near_ten(num):
  x = num % 10
  if x <= 2 or 10-x <=2:
    return True
  return False

print(near_ten(12))