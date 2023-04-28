from datetime import datetime, date, timedelta
from collections import defaultdict

users = [{'Alfred': date(1990, 5, 1)}, {'Benjamin': date(1991, 4, 30)}, {'Christian': date(1992, 4, 29)},
         {'David': date(1993, 5, 1)}, {'Edmund': date(1994, 5, 5)}, {'Frank': date(1995, 5, 6)}]


def get_birthdays_per_week(users: list) -> None:
    today = datetime.now()
    birthday_folks = defaultdict(list)

    for one in users:
        name = list(one)[0]
        birthday = list(one.values())[0]
        celebration_day = date(today.year, birthday.month, birthday.day)

        if celebration_day.weekday() == 5:
            celebration_day += timedelta(days=2)
        elif celebration_day.weekday() == 6:
            celebration_day += timedelta(days=1)

        difference = celebration_day - today.date()
        if 0 <= difference.days <= 7:
            birthday_folks[celebration_day].append(name)

    if len(birthday_folks) == 0:
        print('Sorry guys')
    else:
        sorted_folks = dict(sorted(birthday_folks.items()))
        for day, folks in sorted_folks.items():
            print(f'{day.strftime("%A")}: {", ".join(folks)}')


if __name__ == '__main__':
    get_birthdays_per_week(users)
