def double_char(str):
  result = ''
  for x in str:
    result += x+x
  return result

print(double_char('The'))