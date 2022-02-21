from datetime import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta

def facorial(n):
    if n == 0:
        return 1
    return facorial(n-1) * n

print("Hello World")
s = input("Please enter your name:")
print("Hello " + s)
print("Your name has "+str(len(s)) + " letters. " + str(len(s)) + "! = " + str(facorial(len(s))))
s = parser.parse(input("Please, enter your birth date in format (DD.MM.YYYY):"))

year = datetime.now().year-s.year
days = datetime.now().day-s.day
if(days < 0):
    year -= 1
    days = 365 - s.day

print("Today is " + str(datetime.now().strftime('%d.%m.%y')) +", you are "+ str(year) +" year ("+str((datetime.now() - s).days)+" days) old.")

