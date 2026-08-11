import calendar
import sys

if __name__ == '__main__':
    # sys.stdin.read().split() safely handles extra spaces or blank lines
    data = sys.stdin.read().split()
    if len(data) >= 3:
        month = int(data[0])
        day = int(data[1])
        year = int(data[2])
        
        day_index = calendar.weekday(year, month, day)
        print(calendar.day_name[day_index].upper())
