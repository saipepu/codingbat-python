def caught_speeding(speed, is_birthday):
  if is_birthday == False:
    if speed <= 60:
      return 0
    elif speed <= 80:
      return 1
    else:
      return 2
  elif is_birthday == True:
    if speed <= 65:
      return 0
    elif speed <= 85:
      return 1
    else:
      return 2
  else:
    return 2

print(caught_speeding(60, False))