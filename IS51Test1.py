
"""
The program is trying to determine if Option1 or Option2 pays more money.
Option1 pays 100 dollars per day for 10 days. Option2 pays 1 dollar the first
day and eventually doubles each day for 10 days. Two functions will be used to
calculate the pay rate.
Function1 will calculate the amount for Option1, and Function2 will calculate
the amount for Option2.

Function1 will output 100 dollars * 10 days.
Function2 will loop 10 times, with each time doubling the amount and adding it to the total.

If the amount is equal, we will output to the user "Option 1 and Option 2 pays the same. "
If Option1 is better, we will output to the user "Option 1 is better. "
If Option2 is better, we will output to the user "Option 2 is better. "
"""

"""
#option1
return 100 * 10

#option2
  amount = 1
  list1 = []
  loop 10 times
    add amount to list1
    amount *= 2
  sum = sum of all items in loop
  return sum
# main
  var1 = option1
  var2 = option2

  if var1 = var2
    "Option 1 and Option 2 pays the same"
  if var1 < var2
    "Option 2 is better"
  else
    "Option 1 is better"


main
"""

def option1():
  return 100 * 10

def option2():
  amount = 1
  list1 = []
  for i in range(0, 10):
    list1.append(amount)
    amount *= 2
  print("list1", list1)
  total = sum(list1)
  return total
def main():
  answer = ""
  var1 = option1() #1000
  var2 = option2() #1023
  print("From main: Option 1 = $", var1, "Option 2 = $", var2)
  if var1 == var2:
    answer = "Option 1 and Option 2 pays the same"
  if var1 < var2:
    answer = "Option 2 is better"
  else:
    answer = "Option 1 is better"
  print(answer)


main()


