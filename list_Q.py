#Q1: Write the sum & avg of the list elements

# numbers = [10,20,30,40,50]
# sum = 0
# for i in numbers:
#     sum = sum + i

# print(f"sum of your numbers is: {sum}")
# print(f"average of your numbers is: {sum/len(numbers)}")

#Q2: Find the maximum value in the list and the list of index numbers where it occurs

# a = [11,25,65,48,28,85,74,99,12]
# max = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i
# print(f"Maximum value is: {max} at index: {index}")

#Q3: Find the second largest value in the list

a = [55,10,95,100,65]
max = a[0]
max2 = a[0]
index = 0
index2 = 0

for i in range(len(a)):
    if a[i] > max:
        max2 = max
        
        index2 = i
