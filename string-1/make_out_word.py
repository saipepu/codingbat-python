def make_out_word(out, word):
  left = out[0:2]
  right = out[2:len(out)]
  result = left+word+right
  return result