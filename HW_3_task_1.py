# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.


import datetime as dt

def get_days_from_today(date):
        try:
            users_date = dt.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return f"Verify correctness of your date"
        else:
            return (dt.datetime.today() - users_date).days

print(get_days_from_today("2005-02-06"))