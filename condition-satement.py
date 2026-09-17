# Q No. 1
a = float(input("Please enter a firstnumber: "))
b = float(input("Please enter a second number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")


# Q No. 2
gen = input("Please enter a character m,f :- ")
if gen == 'm':
    print("Hello sir")
else:
    print("Hello madam")


#Q No. 3
num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")


#Q NO. 4 vote 
name = input("Please tell your name:- ")
age = int(input("Please tell your age:- "))
if age >= 18:
    print(f"{name} you are eligible for vote")
else:
    print(f"{name} you are after years {18-age} vote")


#Q NO. 5  leap year check
year = int(input("Please enter a year:- "))
if year % 400 == 0 and year % 100 == 0:
    print(f"{year} is a leap year")
elif year % 4==0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#Q No. 6 bill counting
bill = int(input("Please enter a total amount: -"))
if bill >= 1000 and bill <= 5000:
    print(f"Your bill  get 10% discount and your final amount is {bill * 90/100}")
elif bill >= 5000:
    print(f"Your bill  get 20% discount and your final amount is {bill * 80/100}")
else:
    print("Sorry No discount for your bill")