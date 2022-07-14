def cigar_party(cigars, is_weekend):
  if cigars < 40:
    return False
  elif cigars > 60 and is_weekend == False:
    return False
  else:
    return True

if cigar_party(70, False):
  print("Let's rock the party")
else:
  print('No Coc, Just Code tnght')