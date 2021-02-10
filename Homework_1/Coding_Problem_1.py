#Santiago Landaverde
#1856681

from datetime import date

def find_age(currentDate, birthDate):
    today = currentDate
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

print("Birthday Calculator")
print('Current Day')

month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))

print('Birthday')

birthday_month = int(input('Month: '))
birthday = int(input('Day: '))
birth_year = int(input('Year: '))

print("You are ", find_age(date(year, month, day), date(birth_year, birthday_month, birthday)), "years old")
if day == birthday and month == birthday_month:
    print("Happy Birthday!")