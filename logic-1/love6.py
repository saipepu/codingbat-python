def love6(a,b):
  if 6 in [a,b] or abs(a-b) == 6 or a+b == 6:
    return True
  return False

print(love6(6,4))