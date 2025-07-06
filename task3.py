## task 1
print(" **********  Your Mini CalculatorU **********")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
choice=input("Enter your choice (add, subtract, multiply, divide): ").strip().lower()
if choice == "add":
    result=(num1 + num2)
    print(f"Addition {result}")
elif choice == "subtract":
    result=(num1 - num2)
    print(f"Subtraction {result}")
elif choice == "multiply":
    result=(num1 * num2)
    print(f"Multiplication {result}")
elif choice == "divide":
    if num2 != 0:
        result=(num1 / num2)
        print(f"Division {result}")
    else:
        print("Error: Division by zero is not allowed.")


#------------------------------------------------------------------------------------------------------#

# task 2

print("Marks Calculator and Grade System")
sub1=float(input("Enter marks for Subject 1:"))
sub2=float(input("Enter MARKS FOR Subject 2:"))
sub3=float(input("Enter marks for Subject 3:"))    

total_marks=sub1+sub2+sub3
percentage=total_marks/3

if percentage >= 80:
    grade="A"
    print(f"Your Total marks are {total_marks} & Percentage is {percentage}%, A grade.")
elif percentage >= 70:
    grade="B"
    print(f"Your Total marks are {total_marks} & Percentage is {percentage}%,B grade.")
elif percentage >= 50:
    print(f"Your Total marks are {total_marks} & Percentage is {percentage}%,  C grade.")
    grade="C"
else:
    grade="Fail"
    print(f"Your Total marks are {total_marks} & Percentage is {percentage}%, Your Fail .")


#------------------------------------------------------------------------------------------------------#

#task 3

salary=float(input("Enter your salary:"))

if salary <0:
    salary=float(input("Error: Salary cannot be negative. Please enter a valid salary: "))
expenses=float(input("Enter your expenses:"))
saving=salary - expenses
if saving > 100000:
    print("well Saving")
elif saving < 9999 and saving > 5000:
    print("Good Saving")
else:
    print("try to save money")


#------------------------------------------------------------------------------------------------------#

#task 4
## user name is admin and password is 1234
print("Welcome to the Login System")

username=input("Enter your username:")
password=input("Enter your password:")
if username == "admin" and password == "1234":
    print("Login successful!")


#--------------------------------------------------------------------------------------------------------#

#task 5

attendance_percentage=float(input("Enter your attendance percentage: "))
marks=float(input("Enter your marks: "))
if attendance_percentage >= 75 and marks >= 50:
    print("Promoted.") 
else:
    print("Not Promoted.")


#--------------------------------------------------------------------------------------------------------#

#task 6
product=int(input("Enter the product quantity: "))
price=int(input("Enter price of the product: "))

if price < 1000 and product < 3:
    discount=0.15
elif price < 500 :
    discount=0.10
else:
    discount=0.0
total_price = product * price
discount_amount = total_price * discount
final_price = total_price - discount_amount
print(f"Total price: {total_price}, Discount: {discount_amount}, Final price: {final_price}")