# # try & except 
# a = (int(input("Enter your 1st number")))
# b = (int(input("Enter your 2nd number")))
# try:
#     c = (a/b)
# except Exception as err:
#     print(f"wirte error problem this block{err}")
# v = a+b
# print(v)

# file = open(r"C:\Users\lenovo\Downloads\pythonBOOK (1).pdf.main.py")
# print(file.read())

#new file created (x): created the file error alredy exit
# open("pull.txt","x")

file = open("push.txt",'w')
file.write("this is my new file created on the using file hendaling ")
file.close()
