from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Get the number of days from the user
days_to_add = int(input("Enter the number of days: "))

# Calculate the future date by adding days
future_date = today + timedelta(days=days_to_add)

# Format the date string (Saturday, February 06, 2021)
formatted_date = future_date.strftime("%A, %B %d, %Y")

# Print the formatted date
print(f"The date {days_to_add} days from now is: {formatted_date}")
