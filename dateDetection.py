import re

# Detect dates in the DD/MM/YYYY format
# Days range from 01 to 31
# Months range from 01 to 12
# Years range from 1000 to 2999
# If day or month are single digits, it has leading zero
# Store the strings into variables named month, day, and year
# Add code to detect if it is a valid date


dateDetectionRegex = re.compile(r'''(
  (0[0-9]|[1-2][0-9]|3[0-1])/                # DD/
  (0[0-9]|1[0-2])/                           # MM/
  (1[0-9][0-9][0-9]|2[0-9][0-9][0-9])        # YYYY
)''', re.VERBOSE)

def dateValidation():
  day = ''
  month = ''
  year = ''
  date = dateDetectionRegex.findall(input("Today's date (DD/MM/YYYY): "))

  for group in date:
    for i in range(len(group)):
      if i == 0:
        continue
      if i == 1:
        day = group[i]
      if i == 2:
        month = group[i]
      if i == 3:
        year = group[i]

  # 30 day months - April, June, September, November
    if (month == '04' or month == '06' or month == '09' or month == '11') and (int(day) >= 31):
      print('invalid date')
      break
    
  # February validation - 29 days
    elif (month == '02') and (int(day) > 29):
      print('invalid date')
      break
  # Leap years occur every even year divisible by 4
  ### Not years evenly divisible by 100
  ### Unless the year is also divisible by 400
    elif (month == '02' and day == '29'):
      if (not (int(year)%2 == 0)):
        print('invalid date')
        break
      elif ((int(year)%4 == 0) and (int(year)%100 != 0) or (int(year)%400 == 0)):
        print('date is valid')
    else:
      print('date is valid')


dateValidation()