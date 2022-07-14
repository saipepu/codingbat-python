def make_chocolate(small, big, goal):
  bb = big * 5
  sb = small * 1
  if bb > goal:
    if goal%5 <= sb:
      return goal%5
    else:
      return -1
  elif goal%bb == 0 and bb == goal:
    return 0
  elif abs(goal-bb) <= sb:
    return abs(goal-bb)
  elif goal <= sb:
    return goal
  else:
    return -1
