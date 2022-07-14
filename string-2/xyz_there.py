def xyz_there(str):
  count = 0
  c = 'xyz'
  for x in range(len(str)):
    for y in range(len(c)):
      if str[x] == c[y] and len(str[x:len(str)]) >= len(c):
        for z in range(len(c)):
          if str[x+z] == c[z]:
            count += 1
          else:
            count = 0
        if count == 3 and str[x-1] != '.':
          return True
  return False
          

print(xyz_there('abc.xyzxyz.xyz'))