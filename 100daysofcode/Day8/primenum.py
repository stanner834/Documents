# def prime_checker(number):
#     is_prime = True

#     if number <= 1:
#         is_prime = False
#     else:
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break

#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# # Do NOT change any of the code below👇
# n = int(input())  # Check this number
# prime_checker(number=n)

#Prof solution
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")   
# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(number=n)