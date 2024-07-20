#question 1
# def divisible():
#     for i in range(1500,2701):
#         if(i%7==0 and i%3==0):
#              print(i)
# divisible()      

#Question 2
# def temp():
#     y=int(input("enter 1 if you want to convert C to F and 2 F to C\n"))
#     if y==1:
#         temperature=float(input("enter temperature in celsisus"))
#         print((9/5)*temperature + 32)
#     elif y==2:
#         temperature=float(input("enter temperature in f"))
#         print((5/9)*temperature-32)
#     else:
#          print("invalid input enter 1 or 2")
# temp()


##Question 3
# def game():
#     y=int(input("guess the number"))
#     if y in range(1,10):
#         print("well guessed")

#     else:
#      print("again until the guess is correct")
# game()


#Question 4
# row=5
# for i in range(1,row+1):
#     print('*' * i)
# for i in range(row-1,0,-1):
#     print('*' * i)


#Question 5
# def reserve_word(word):
#     return word[::-1]
# user_input=input("enter the word")
# reserved_word=reserve_word(user_input)
# print("reservedword=",reserved_word)


#Question 6
# def count_number(number):
#     even_count=0
#     odd_count=0
#     for i in number:
#         if(i%2==0):
#             even_count=even_count+1
#         else:
#             odd_count=odd_count+1
#     return even_count,odd_count
# number=[1,2,3,4,5,6,7,8,9,11]
# even_count,odd_count=count_number(number)
# print("total even numbers",even_count)
# print("total odd number",odd_count)


#Question 7






#Question 8
# numbers=[0,1,2,3,4,5,6]
# for i in numbers:
#     if(i==3 or i==6):
#         continue
#     print(i)
    
    

#Question 9
# a=0
# b=1
# print(a)
# while b<=50:
#     print(b)
#     a,b=b,a+b
    

#Question 10
# def fizz_buzz():
#     for i in range(1, 51):
#         if i % 3 == 0 and i % 5 == 0:
#             print("fizzbuzz")
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#         else:
#             print(i)

# fizz_buzz()


#Question 10
# def 2d_array(m, n):
#     # Initialize the 2D array
#     array = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             row.append(i * j)
#         array.append(row)
#     return array
# m = 3
# n = 4
# result =2d_array(m, n)
# print(result)


#Question 11

# def read_and_print_lines():
#     lines = []
#     while True:
#         line = input("Enter a line (blank line to terminate): ")
#         if line == "":
#             break
#         lines.append(line.lower())
    
#     for line in lines:
#         print(line)

# read_and_print_lines()

    
#Question 12

# def binary_divisible_by_5(binary_sequence):
#     binary_numbers = binary_sequence.split(',')

#     divisible_by_5 = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]

#     print(','.join(divisible_by_5))

# input_sequence = input("Enter a sequence of comma separated 4-digit binary numbers: ")
# binary_divisible_by_5(input_sequence)


#Question 13

# def count_digits_and_letters(input_string):
#     digit_count = 0
#     letter_count = 0

#     for char in input_string:
#         if char.isdigit():
#             digit_count += 1
#         elif char.isalpha():
#             letter_count += 1

#     return digit_count, letter_count

# input_string = input("Enter a string: ")
# digits, letters = count_digits_and_letters(input_string)
# print("number of digits",digits)
# print("number of letters",letters)
    
#Question 14
import re
def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[$#@]', password):
        return False
    
    return True

password = input("Enter your password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Please ensure it meets the criteria.")