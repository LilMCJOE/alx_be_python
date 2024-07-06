import datetime
from datetime import timedelta

def display_current_datetime():
    current_datetime = datetime.datetime.now()
    formated_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formated_datetime}")
display_current_datetime()

def calculate_future_date():
    num_of_days = int(input("Enter the number of days to add to the current date:  "))
    current_date = datetime.datetime.now()
    days = timedelta(days=num_of_days)
    future_date = current_date + days
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {formatted_future_date}")
calculate_future_date()
