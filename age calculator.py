import datetime
from dateutil.relativedelta import relativedelta


def ask_yes_no(question):
    answer = input(question).lower()
    while answer not in ("y", "n"):
        print("Invalid command (ENTER ONLY *y* or *n*)")
        answer = input(question).lower()
    return answer


def calculate_age(birth_datetime, now_datetime, include_time):
    age = relativedelta(now_datetime, birth_datetime)
    
    if include_time:
        print(f"\nYour age is {age.years} years {age.months} months {age.days} days {age.hours} hours {age.minutes} minutes and {age.seconds} seconds...\n")
    else:
        print(f"\nYour age is {age.years} years {age.months} months and {age.days} days...\n")


print("\n***AGE CALCULATOR***\n")

while True:
    age_calculate = ask_yes_no("Do you want to proceed (y/n): ")

    if age_calculate == "n":
        print("\nThanks for using the age calculator!")
        break

    birth_year = int(input("\nYour Year of birth: "))
    birth_month = int(input("Your Month of Birth (1 - 12): "))
    birth_date = int(input("Your date of birth (1 - 31): "))

    time_permission = ask_yes_no("Can you also provide the HOURS, MINUTES AND SECONDS of your birth (y/n): ")

    if time_permission == "y":
        birth_hour = int(input("Your hour of birth (0 - 23): "))
        birth_minute = int(input("Your minute of birth (0 - 59): "))
        birth_second = int(input("Your second of birth (0 - 59): "))

        birth_datetime = datetime.datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute, birth_second)
        now_datetime = datetime.datetime.now()

        calculate_age(birth_datetime, now_datetime, include_time=True)

    else:
        birth_datetime = datetime.date(birth_year, birth_month, birth_date)
        now_datetime = datetime.date.today()

        calculate_age(birth_datetime, now_datetime, include_time=False)
