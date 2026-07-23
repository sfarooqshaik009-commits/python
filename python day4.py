#program 1
# file = open("notes.txt", "w")
# file.write("hello")
# file.close()

#program 2
# a={'name': 'John', ''
# 'age': 30, 
# 'city': 'New York'}
# print(a["name"])
# print(a.keys())
# a['fee']=20000
# print(a)
# del a["city"]
# print(a)
# print(a.items())

#program3
# try:
#     num=int(input("Enter a number: "))
#     result=100/num
#     print(result)
# except ZeroDivisionError:
#     print(":error:cannot divide by zero")
# except ValueError:
#     print(":error:enter a valid number")

# else:
#     print("success:",result)
# finally:
#     print("exception completed")

#program 4
# def fibonacci(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         c = a + b
#         a = b
#         b = c

#     return a

# n = int(input("Enter a number: "))
# print("Fibonacci number is:", fibonacci(n))

#program 5
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# n=int(input("enter the number:"))
# print(fact(n))

#program 6
# '''a=lambda x:x**2
# print(a(5))'''

# '''
# a=[1,10,30,9,60,20,25]
# b=list(filter(lambda x:x%2==0,a)) #if we use !==0 odd num will be prited
# print(b)'''



# a=[1,10,30,9,60,20,25]
# b=list(filter(lambda x:x%2==0,a)) #if we use !==0 odd num will be prited
# c=list(map(lambda x:x**2,a))# power of 2 of all the elements in the list
# print(b)
# print(c)

#program 7
#def phone_number(num):   
#     if len(num) == 10 and num.isdigit():
#         print("Valid phone number")
#     else:
#         print("Invalid phone number")
# num = input("Enter a phone number: ")
# phone_number(num)

#program 8
# a=[1,1,2,3,4,5,5]
# print(set(a))
# marks={
#     'vamsi':90,
#     'charan':80,
#     'nithin':70,
#     'suresh':50
# }
# for name, value in marks.items():
#     if value > 50:
#         print(f"{name}: {value}")

#program 9
# a={1,2,2,1,3,4}
# a.add(5)
# print(a)

# a={1,2,2,1,3,4}
# a.remove(4)
# print(a)

# a={1,2,2,1,3,4}
# a.discard(5)
# print(a)


# a={1,2,2,1,3,4}
# a.pop()
# print(a)


# a={1,2,2,1,3,4}
# b={1,2,3,4,5,6}
# print(a|b)# union
# print(a&b)# intersection
# print(a-b)# difference
# print(a^b)# symmetric difference

#program 10
# a=input("Enter a character: ")
# count=0
# for i in a:
    
#     if i in 'aeiouAEIOU':
#         count+=1
        
# print("Total number of vowels:",count)