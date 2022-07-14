def middle_way(a, b):
  mid_a = a[int(len(a)/2)]
  mid_b = b[int(len(b)/2)]
  return [mid_a, mid_b]

print('The middle way of [1,2,3] & [4,5,6] ->', middle_way([1,2,3],[4,5,6]))