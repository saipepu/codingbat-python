def end_other(a,b):
  a = a.lower()
  b = b.lower()
  if len(a) >= len(b):
    big = a
    small = b
  else:
    small = a
    big = b

  if big[len(big)-len(small):len(big)] == small:
    return True
  else:
    return False

# def end_other(a,b):
#   return (b.lower().endswith(a.lower()) or a.lower().endswith(b.lower()))

print(end_other('Hiabc', 'abc'))