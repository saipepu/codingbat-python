def in1to10(n, outside_mode):
  if outside_mode:
    return True
  elif 1<=n<=10:
    return True
  else:
    return False

print(in1to10())