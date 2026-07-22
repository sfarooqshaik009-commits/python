#program 1
"""
mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Total Marks =", total)
print("Average Marks =", average)

if average >= 40:
    print("Pass")
else:
    print("Fail")
"""
#Python program 2

# units = float(input("Enter the number of units consumed: "))

# if units <= 100:
#     bill = units * 1.5
# elif units <= 200:
#     bill = (100 * 1.5) + ((units - 100) * 2.5)
# else:
#     bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4.0)

# print("Electricity Bill = $", bill)

#program 3

# subject1 = 85
# subject2 = 78
# subject3 = 92

# total = subject1 + subject2 + subject3
# average = total / 3


# if average >= 90:
#     grade = 'A'
# elif average >= 75:
#     grade = 'B'
# elif average >= 60:
#     grade = 'C'
# elif average >= 50:
#     grade = 'D'
# else:
#     grade = 'Fail'

# print(f"Total Marks: {total}")
# print(f"Average Marks: {average:.2f}")
# print(f"Grade: {grade}")

# Input from the user
# n = int(input("Enter an integer: "))

# reverse = 0
# num = n  

# while n != 0:
#     remainder = n % 10
#     reverse = reverse * 10 + remainder
#     n = n // 10  

# print("Reversed number =", reverse)


# def count_even_odd_digits(num):
    
#     num_str = str(abs(num))
    
#     even_count = 0
#     odd_count = 0
    
#     for digit in num_str:
#         if digit.isdigit():
#             if int(digit) % 2 == 0:
#                 even_count += 1
#             else:
#                 odd_count += 1
                
#     return even_count, odd_count

# number = 123456789
# evens, odds = count_even_odd_digits(number)

# print(f"Number: {number}")
# print(f"Number of even digits: {evens}")
# print(f"Number of odd digits: {odds}")

#program 5
# product = "Laptop"
# quantity = 2
# price = 3000

# total = quantity * price
# discount = 600  
# final_amount = total - discount

# print("----------- BILL -----------")
# print(f"Product : {product}")
# print(f"Quantity : {quantity}")
# print(f"Price : {price}")
# print(f"Total : {total}")
# print(f"Discount : {discount}")
# print(f"Final Amount : {final_amount}")

#program 6

balance = 5000

while True:
    print("=" * 50)
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("=" * 50)

    try:
        choice = int(input("Enter a number: "))
    except ValueError:
        print("Don't enter alphabets or special symbols.")
        continue

    if choice == 1:
        print("Current balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("New balance:", balance)

    elif choice == 3:
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdraw successful.")
            print("Current balance:", balance)
        else:
            print("Insufficient balance.")

    elif choice == 4:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")

