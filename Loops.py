n = int(input("Enter a table number:- "))
for i in range(n,(n*10)+1,n):
    print(i)

s = "hello How are you"  
for i in range(len(s)):
    print(s[i])

#Q No. 2
n = int(input("Please tell me how many numbers you want to print:- "))
for i in range(n):
    print(f"{i+1}: hello world")
 
# Q No.3
n = int(input("tell the how many times number print"))
for i in range(n,0,-1):
    print(i)

# natural number sum
n = int(input("tell where do your sum:- "))
s = 0
for i in range(1,n+1):
    s = s + i
print(f"your sum of {s}")

# # Factorial
n = int(input("which number's of factorial:- "))
s = 1
for i in range(1,n+1):
    s = s * i
print(f"your factorial is {s}")

num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))
for i in range(num1,num2+1):
    if i%2==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")

n = int(input("Tell your range:- "))
even_sum = 0
odd_sum = 0
for i in range(1,n+1):
    if i%2==0:
        even_sum += i
    else:
        odd_sum += i
print(f"your even sum is {even_sum} and your odd sum is {odd_sum}")

#Q No. 7  fined factors
n = int(input("Tell the number to find factors:- "))
for i in range(1,n+1):
    if n % i==0:
        print(i)

# Q No. 8 all factors of SUM
n = int(input("Tell the sum of number factors:- "))
s = 0
for i in range(1, n+1):
    if n % i == 0:
        s += i
print(f"Your sum of factors is {s}")

# # Q No. 9 power of number
a = int(input("Enter the value :- "))
b = int(input("Enter the exponent:- "))
power = 1 # Initialize power to 1
for i in range(b):
    power *= a
print(f"Your result is {power}")

# Q No. 10 find the number prime or exponent
n = int(input("Tell the sum of number factors:- "))
for i in range(1,n+1):
    if n % i == 0:
        print("Sorry this number is composite:- ")

