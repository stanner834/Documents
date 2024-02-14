def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    #leap_year = is_leap(y)
    is_leap(y)
    if is_leap == True:
        if m == 2:
            return 29
    else:
        return month_days[m - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
if month == 0:
    print("You cannot enter 0 as a month.")
else:
    days = days_in_month(year, month)
    print(days)