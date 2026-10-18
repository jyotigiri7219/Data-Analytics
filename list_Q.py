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

# a = [55,10,999,95,100,65]
# max = a[0]
# max2 = a[0]
# index = 0
# index2 = 0
# for i in range(len(a)):
#     if a[i] > max:
#         max2 = max
#         max = a[i]
#         index2 = index
#         index = i
#     elif a[i] > max2:
#         max2 = a[i]
#         index2 = i
#print(f"maximum value is: {max} at index: {index} \n second maximum value is: {max2} at index: {index2}")

#Q4 the list shorted and not shorted list

# a = [10,20,30,35,40,45,50,55,60,59,70,75,80,85,90]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("List is not sorted")
#         break
# else:
#     print("List is sorted")

#Q5: Left rotate the list by 1st element , sift to last element

# a = [10,20,30,40,50]
# for i in range(len(a)-1):  #right rotate (len(a)-1,0,-1)
#     a[i],a[i+1] = a[i+1], a[i] #  a[i],a[i-1] = a[i-1], a[i] 

# print(a)

#Q6 N times of rotate elements in the list

# n = int(input("How many times want to rotate the list:"))
# a = [10,20,30,40,50]
# for i in range(n):
#     for i in range(len(a)-1):
#         a[i],a[i+1] = a[i+1], a[i]

# print(a)


#left roteat
# n = int(input("How many times want to left rotate the list"))
# a = [10,20,30,40,50]
# for i in range(n):
#     for i in range(len(a)-1,0,-1):
#         a[i],a[i-1] = a[i-1], a[i]   # swapping the elements [a,b = b,a] formula

# print(a)


 