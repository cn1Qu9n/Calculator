#Run in Python 3.

#Intoduction and display of options
print("Made by cn1Qu9n.\n")
print("0: Exit\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n")

#Definitions of functions
def Input():
  global Operator
  Operator = input("Number of arithmetic operator you wish to use (0,1,2,3,4): ")
  if Operator == "0":
    print("Exiting...")
    exit()
  elif Operator == "1":
    print("Addition chosen.\n")
    Process()
  elif Operator == "2":
    print("Subtraction chosen.\n")
    Process()
  elif Operator == "3":
    print("Multiplication chosen.\n")
    Process()
  elif Operator == "4":
    print("Division chosen.\n")
    Process()
  else:
    print("Invalid input. Only numbers 0 to 4 are accepted. Please try again.\n")
    Input()

def Process():
  if Operator == "1":
    First_Number = int(input("First number: "))
    Second_Number = int(input("Second number: "))
    Answer = First_Number + Second_Number
    print("\nAnswer: " + str(Answer))
    print("\n")
    Resume()
  elif Operator == "2":
    First_Number = int(input("First number: "))
    Second_Number = int(input("Second number: "))
    Answer = First_Number - Second_Number
    print("\nAnswer: " + str(Answer))
    print("\n")
    Resume()
  elif Operator == "3":
    First_Number = int(input("First number: "))
    Second_Number = int(input("Second number: "))
    Answer = First_Number * Second_Number
    print("\nAnswer: " + str(Answer))
    print("\n")
    Resume()
  elif Operator == "4":
    First_Number = int(input("First number: "))
    Second_Number = int(input("Second number: "))
    Answer = First_Number / Second_Number
    print("\nAnswer: " + str(Answer))
    print("\n")
    Resume()

def Resume():
  Continue = input("Do you want to continue using the program (Yes/No)? ")
  if Continue == "Yes":
    print("\n")
    Input()
  elif Continue == "No":
    print("Exiting...")
    exit()
  else:
    print("Invalid input. Only \"Yes\" or \"No\" is allowed (Case sensitive). Please try again.")
    Resume()

#Start of functions
Input()
