import datetime

def display_current_datetime ():
    current_date = datetime.datetime.now()
    return current_date

print(f"Current date and time: {display_current_datetime()}")

def calculate_future_date(number_of_days):
    current_date = display_current_datetime()
    duration = datetime.timedelta(days = number_of_days)
    future_date = current_date + duration
    return future_date

number_of_days = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date(number_of_days)}")