num_pennis = int(input("Enter the number of pennis: "))
num_nickles = int(input("Enter the number of nickles:"))
num_dimes = int(input("Enter the number of dimes: "))
num_quarters = int(input("Enter the number of quarters: "))

PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

total_cents = (num_pennis * PENNY_VALUE) + (num_nickles * NICKEL_VALUE) + (
  num_dimes * DIME_VALUE) + (num_quarters * QUARTER_VALUE)
total_dollars = total_cents / PENNIES_IN_DOLLAR

if total_dollars > 1.0:
  print("Sorry, the amount you entered was more than one dollar")
elif total_dollars < 1.0:
  print("Sorry, the amount you entered is less than one dollar")

else:
  print(
    "Congratulations! \n The amount you entered was exactly one dollar! \n You win the game!!"
  )