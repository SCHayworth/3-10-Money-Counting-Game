# Scope
Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The program should prompt the user to enter the number of pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program should congratulate the user for winning the game. Otherwise the program should display a message indicating whether the amount entered was more than or less than one dollar.

## Sample Run 1
    Enter the number of pennies: 5
    Enter the number of nickels: 3
    Enter the number of dimes: 3
    Enter the number of quarters: 2
    Congratulations!
    The amount you entered was exactly one dollar!
    You win the game!
  
## Sample Run 2
    Enter the number of pennies: 6
    Enter the number of nickels: 7
    Enter the number of dimes: 8
    Enter the number of quarters: 9
    Sorry, the amount you entered was more than one dollar.
    
# Pseudocode
    total = 0.0
    Prompt user for the number of pennies
    Calculate the value of the pennies
      penny value = number of pennies * 0.01
    Add penny value to total.
    Prompt user for number of nickels
    Caluclate the value of the nickels
      nickel value = number of nickels * 0.05
    Add nickel value to total.
    Prompt user for number of dimes
    Calculate the value of the dimes
      dime value = number of dimes * 0.1
    Add dime value to total
    Prompt user for the number of quarters
    Calculate the value of the quarters
      quarter value = number of quarters * 0.25
    Add quarter value to total
    IF total == 1.00
      print "Congratulations!"
      print "The amount you entered was exactly one dollar!"
      print "You win the game!"
    ELSE IF total > 1.00
      print "Sorry, the amount you entered was more than one dollar."
    ELSE
      print "Sorry, the amount you entered was less than one dollar."
