#FutureTime.py
#Name: Juan Mancilla Vargas
#Date:01/28/2025
#Assignment: FutureTime

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  moreMins = 5
  moreHours =12

  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60
  futureHour = (currentHour + moreHours + extraHour) % 24
  futureHour12 = (futureHour % 12)
  period = ["AM", "PM" ] [ (futureHour //12)%2]

  print(f"Future Time: {futureHour12:02} : {futureMins:02} {period}")

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
