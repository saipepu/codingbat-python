def count_code(str):
  count = 0
  for x in range(len(str)-1):
    # print(str[x:x+4])
    # print(len(str[x:x+4]))
    if len(str[x:x+4]) == 4:
      print(str[x:x+2], str[x+3])
      if str[x:x+2] == 'co' and str[x+3] == 'e':
        print('yes again')
        count += 1
  return count

print(count_code('aaacodebbb'))