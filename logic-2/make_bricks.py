def make_bricks(small, big, goal):
  bb = big * 5
  sb = small * 1
  if bb > goal:
    if (goal%5) <= sb:
      return True
    else:
      return False
  elif goal%5 == 0:
    return True
  elif abs(goal-bb) <= sb:
    return True
  elif goal <= sb:
    return True
  else:
    return False

print(make_bricks(3, 1, 9))