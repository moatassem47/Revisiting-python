from datetime import datetime, timedelta
todays_date = datetime.now()
print(f"today is {todays_date.year}/{todays_date.month}/{todays_date.day}")

one_day = timedelta(days=1)
yesterday = datetime.now() - one_day
print(f"yesterday was: {yesterday.year}/{yesterday.month}/{yesterday.day}")

try:

 birthday =input("enter you birthday(dd/mm/yyyy)")
 birthday_format = "%d/%m/%Y"
 birthdate = datetime.strptime(birthday, birthday_format)

 if(birthdate>datetime.now()):
  print("this date didn't come yet")
 else:
   print(f"you are {abs(birthdate.year-2025)} years")
except:
 ValueError
 print("check if the date is correct")

