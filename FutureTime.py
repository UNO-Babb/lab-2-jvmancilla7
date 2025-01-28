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

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  moreMins = 60

  totalMinutes = currentMinute + moreMins
  futureMinutes = totalMinutes % 60
  futureHours = (currentHour + totalMinutes // 60) % 24
  print(f"The future will be {futureHours:02}:{futureMinutes:02}")



  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
