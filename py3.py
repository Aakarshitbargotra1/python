# def isgreater(a,b):
#     if(a>b):
#         print("1st number is greater than 2nd number")
#     else:
#         print("2nd number is greater than 1st number")
# a=10
# b=84
# isgreater(a,b)
#
# def islesser(c,d):
#     if(c<d):
#         print("1st number is less than 2nd number")
#     else:
#         print("2nd number is less than 1st number")
# c=53
# d=75
# islesser(c,d)
#
# j= int(input("Enter the number"))
# for i in range(1,11):
#     print(j,"x",i,"=",j*i)

# k = "python"
# j = k[::-1]
# print(j)

# k ="naman"
# j= k[::-1]
# if(k == j):
#     print("The given string is pallindrom")
# else:
#     print("The given string is not pallindrom")

# k ="This a example of a string with multiple words"
# j = k.split(" ")
# l = len(j)
# print("The number of words is ",l)

# x = "this     is  a         new      string cout  the    elements"
# j = x.split()
# k = " ".join(j)
# print(k)

# list = [1 , 2, "Aakarshit", 5, "Bargotra"]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])
#
# if "Aakarshit" in list:
#     print("Yes")
# else:
#     print("No")

# a,b,c = input("Enter 3 the inputs").split()
# print(a,b,c)

# x = input("Enter the city name")
# y = "jammu"
# if y==x.lower().strip():
#     print("City found")
# else:
#     print("City not found")

# list = [
#     ["student name", "student Roll no.", "student class"],
#     ["student1 name", "student1 Roll no.", "student1 class"],
#     ["student2 name", "student2 Roll no.", "student2 class"]
# ]

# x = input("Enter a string")
# y = ("a","e","i","o","u","A","E","I","O","U")
# z = list(x)
# print(z)
# for i in z:
#         if i in y:
#             print("The vowels are",i)
#         else:
#             print("The consonants are",i)

#
# print("What is the capital of India?")
# print("A. NEW DELHI\t\tB. MUMBAI\nC. KOLKATA\t\tD. BENGALURU")
# i = input("Enter your choice:")
# if i=="A":
#     print("TRUE")
# else:
#     print("FALSE")


# def square(n):
#     '''Takes in a number and returns its square'''
#     print(n*n)
# square(6)
# print(square.__doc__)


# x = int(input("Enter the number to find the factorial of"))
# def factorial(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         return x * factorial (x-1)
# print(factorial(x))


#
# a = {1,5,3,5,3,567,8}
# for value in a:
#     print(value)


# list = ["Surgun","Arsh", "Sacchit","Aryan"]
# print(f"i invite {list[0]} to dinner")
# print(f"I invite {list[1]} to dinner")
# print(f"I invite {list[2]} to dinner")
# print(f"I invite {list[3]} to dinner")
# # print(f"{list[0]} can't make it to dinner")
# a = list[0]
# print(f"{a} can't make it to dinner")
# list[0] = "kanav"
# print(f"{list[0]} is coming to the dinner")
# list.insert(0 , "Uday")
# print(list)
# nlist = len(list)//2
# list.insert(nlist , "shubam")
# list.append("Harry")
# print(list)
#
# a = "Aakarshit"
# for i in a:
#     print(i)
#
# list = [1,2,3,4,5,6,7]
# print(list[::-1])