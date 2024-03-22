total_sum = 0.0

while True:
  # Get user input as a number
  number = float(input("Enter a number (or -1 to quit): "))

  # Check if user entered -1 to quit
  if number == -1:
    break

  # Add the number to the total sum
  total_sum += number

# Print the total sum with two decimal places
print(f"The sum of all numbers is: {total_sum:.2f}")
