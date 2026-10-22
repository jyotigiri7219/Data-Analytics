# class Factory:
#     def __init__(self,matrial,cycle,hero): #self is paeameter Factory to location call
#         self.matrial =  matrial
#         self.cycle =  cycle
#         self.hero =  hero
#         #print("this is a constructor use the")


# obj = Factory("big cycle",2,3) # object created
# obj2 = Factory("small cycle",4,5)

# print(obj.matrial,obj2.matrial)


# class animal:
#     gender = "Male"   #class atribute
#     def __init__(self, name, age):
#         self.name =  name  #instence atribute
#         self.age = age

#     def info(self):  #instance methods
#         print("this is instance methods")

#     @classmethod
#     def clmethod(cls): #class methods
#         print(f"this is a class method{cls.gender} calling the class atribute")

#     @staticmethod
#     def help():   #satic method
#         print("Hello i am a staticmethod")

# obj = animal("dog", 5)
# obj.clmethod()
# obj.info()
# obj.help()


# registertion student information 4 students

class Registration:
    def __init__(self,name,age,number,address):
        self.name = name
        self.age = age
        self.number = number
        self.address = address

    def info(self):
        print(f"hello your name is {self.name}\n your age is {self.age}\n your number is {self.number}\n your addres is {self.address}")

student1 = Registration("adarsh",14,1234567891,"dhaniv")


student1.info()


    