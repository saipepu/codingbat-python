def common_end(a, b):
  af = a[0]
  al = a[len(a)-1]
  bf = b[0]
  bl = b[len(b)-1]
  if af == bf or al == bl:
    return True
  else:
    return False

print(common_end([1, 2, 3], [7, 3]))