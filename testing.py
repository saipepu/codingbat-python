def last2(str):
  l2 = str[len(str)-2:len(str)]
  appears = 0
  for x in range(len(str)):
    count = 0
    for y in range(len(l2)):
      if str[x] == l2[y] and len(str[x:len(str)]) >= len(l2):
        for z in range(len(l2)):
          if str[x+z] == l2[z]:
            count += 1
          else:
            count = 0
        if count == 2:
          appears += 1
  return appears - 1 if appears -1 >= 0 else 0

# print(last2('xxxasdxx'))

def array_count9(nums):
  nums = [str(x) for x in nums]
  return nums.count('9')

print(array_count9([1,9,9]))

def array_front9(nums):
  nums = [str(x) for x in nums]
  return True if ''.join(nums).find('9') < 4 and ''.join(nums).find('9') >= 0 else False

def string_match(a,b):
  count = 0
  for x in range(len(a)-1):
    if len(a[x:len(a)]) >= 2:
      print(a[x:x+2], b[x:x+2])
      if a[x:x+2] == b[x:x+2]:
        count += 1
        # print(a.index(a[x]+a[x+1]), end='')
        # print(b.index(b[x]+b[x+1]))
        # if a.index(a[x]+a[x+1]) == b.index(a[x]+a[x+1]):
        #   count += 1
  return count

print(string_match('aabbccdd', 'abbbxxd'))
# def collectIndexOfB(string, b):
#   indexes = []
#   for x in range(len(b)):
#     count = 0
#     for y in range(len(string)):
#       if b[x] == string[y] and len(b[x:len(b)]) >= len(string):
#         for z in range(len(string)):
#           if b[x+z] == string[z]:
#             count += 1
#           else:
#             count = 0
#         if count == 2:
#           print('yes')
#           indexes.append(b.index(b[x]))
#   return indexes

