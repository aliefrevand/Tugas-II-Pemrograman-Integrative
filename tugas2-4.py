grades = []

while True:
  grade = int(input("Enter a grade (or -1 to quit): "))

  if grade == -1:
    break

  grades.append(grade)

if grades:
  # Calculate average (rounded down using integer division)
  average = sum(grades) // len(grades)

  print(f"Average: {average}")
  for grade in grades:
    print(grade)
else:
  print("No grades entered.")
