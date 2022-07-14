def cat_dog(str):
  cat = 0
  dog = 0
  for x in range(len(str) -1):
    if str[x:x+3] == 'cat':
      cat += 1
    elif str[x:x+3] == 'dog':
      dog += 1
  if cat != dog:
    return False
  else:
    return True