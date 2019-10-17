# Program 3-10 Money Counting Game
# Shaun Hayworth
# CIS 2
# 10-16-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/3-10-Money-Counting-Game

# Gets a number of pennies, nickels, dimes, and quarters from the user, and checks to see if they add to exactly one dollar.

# Initialize the accumulator variable
total = 0.0

# Prompt user for the number of pennies, and calculate the value by multiplying by 0.01
pennies = int(input('Please enter the number of pennies: '))
penny_value = pennies * 0.01

# Add penny_value to total
total += penny_value

# Prompt user for the number of nickels and calculate the value by multiplying by 0.05
nickels = int(input('Please enter the number of nickels: '))
nickel_value = nickels * 0.05

# Add nickel_value to total
total += nickel_value

# Prompt user for the number of dimes and calculate the value by multiplying by 0.1
dimes = int(input('Please enter the number of dimes: '))
dime_value = dimes * 0.1

# Add dime_value to total
total += dime_value

# Prompt user for the number of quarters and calculate the value by multiplying by 0.25
quarters = int(input('Please enter the number of quarters: '))
quarter_value = quarters * 0.25

# Add quarter_value to total
total += quarter_value

# Check if total is greater than, less than, or equal to one dollar and display an appropriate mesage.
if total == 1.00:
  print('Congratulations!')
  print('The amount you entered was exactly one dollar!')
  print('You win the game!')
elif total > 1.00:
  print('Sorry, the amount you entered was more than one dollar.')
else:
  print('Sorry, the amount you entered was less than one dollar.')
