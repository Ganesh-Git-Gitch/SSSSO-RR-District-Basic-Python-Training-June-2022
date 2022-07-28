import datetime
from datetime import date



today_date=date.today()
year = int(input('When is your birthday? [YYYY] '))
month = int(input('When is your birthday? [MM] '))
day = int(input('When is your birthday? [DD] '))

if year>today_date.year :
    raise Exception("Please enter  valid date and year")

birth = datetime.date(year, month, day)
print("Birth: ", birth)

today = datetime.date.today()


print("Today: ", today)

if(
    today.month == birth.month
    and today.day >= birth.day
    or today.month > birth.month
):
    nextBirthdayYear = today.year + 1
else:
    nextBirthdayYear = today.year

nextBirthday = datetime.date(
    nextBirthdayYear, birth.month, birth.day
)

print("Next birthday: ", nextBirthday)

diff = nextBirthday - today

print("Days left for next birthday: ", diff.days)