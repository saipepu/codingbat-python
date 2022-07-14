def count_hi(str):
  return str.count('hi')

#more OG way
def og_count_hi(str):
  sum = 0
  for x in range(len(str) -1):
    if str[x:x+2] == 'hi':
      sum += 1
  return sum
print(og_count_hi('asdfhi hi'))