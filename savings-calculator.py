#Simple savings calculator

def average(lst):
  total = 0
  for x in lst: #Loops trough every entry in the list
    total += x #Adds the given list entry to the total
  average = total / len(lst) #Calculates the average of the entries
  return average

goal = float(input("How much do you wish to save?")) 

def save(goal): #Function that takes your goal as input
  savings = 0
  amounts = [] #Monthly amounts will be appended to this list
  print("") #For better output
  print("Your goal is to save $ %s, your current savings are $ %s" % (
    goal, savings))
  print("")
  while savings < goal: #A loop that runs as long as your savings are less than the goal
    amount = float(input("How much have you saved this month?"))
    savings += amount 
    amounts.append(amount) #Adds the amount to the list in order to 
    #calculate the savings rate
    timeleft = (goal - savings) / average(amounts) 
    timeleft = str(timeleft)[0:4] #Cuts the number to two decimals
    #Time left = months left based on the average savings rate
    print("")
    print("So far you have saved: $ %s" % savings)
    print(
      "At this rate it will take you %s months to reach your goal" % timeleft)
    if savings >= goal: #When the goal is reached
      print("")
      print("Congratulations, you have reached your goal!")

save(goal) #Runs the savings function
