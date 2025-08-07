from datetime import datetime
# todays_date = datetime.now()
# print(f"today is {todays_date.day}")

# one_day = timedelta(days=1)
# yesterday = datetime.now() - one_day
# print(f"yesterday was: {yesterday}")
try:

 birthday =input("enter you birthday(dd/mm/yyyy)")
 birthday_format = "%d/%m/%Y"
 birthdate = datetime.strptime(birthday, birthday_format)

 if(birthdate>datetime.now()):
  print("this date didn't come yet")
 else:
   print(f"your birthday is on: {birthdate}")
except:
 ValueError
 print("check if the date is correct")

