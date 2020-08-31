# v2
import calendar

list(calendar.day_name)

print(calendar.day_name[3])


# v1
def day_by_number(weekday: int) -> str:
    if weekday == 1:
        return "Monday"
    if weekday == 2:
        return "Tuesday"
    if weekday == 3:
        return "Wednesday"
    if weekday == 4:
        return "Thursday"
    if weekday == 5:
        return "Friday"
    if weekday == 6:
        return "Saturday"
    if weekday == 7:
        return "Sunday"


print(day_by_number(6))

# v3
DayOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(DayOfTheWeek[1])


# v4 from class
def get_weekday_bynumb(weekday: int) -> str:
    days = {1: 'Mon',
            2: 'Tue',
            3: 'Wed',
            4: 'Thu',
            5: 'Fri',
            6: 'Sat',
            7: 'Sun'}
    return days.get(weekday, 'incorrect value')


def main():
    print(get_weekday_bynumb(1))


if __name__ == "__main__":
    main()
