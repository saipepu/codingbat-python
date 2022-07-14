def alarm_clock(day, vacation):
  weekdays = [1,2,3,4,5]
  weekends = [0,6]
  if vacation:
    if day in weekdays:
      return '10:00'
    else:
      return 'off'
  else:
    if day in weekdays:
      return '7:00'
    else:
      return '10:00'

print(alarm_clock(1, False))