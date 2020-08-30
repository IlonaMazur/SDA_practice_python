#def dayByNumber(weekday):
#    if weekday == 0:
#        retyrn "Monday"
#    if weekday ==


# v2

import calendar
list(calendar.day_name)
('Monday')

print(calendar.day_name[3])


#v3
DayOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(DayOfTheWeek[1])

#v4 from class
def get_weekday_bynumb(weekday: int) -> str:
    days ={ 1 : 'Mon'
            2 : 'Tue'
            3 : 'Wed'
            4 : 'Thu'
            5 : 'Fri'
            6 : 'Sat'
            7 : 'Sun'}
    return days.get(weekday, 'incorrect value')

def main():
    print(get_weekday_bynumb(1))

if __name__ =="__main__":
    main()