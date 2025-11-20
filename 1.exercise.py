#Name-HAYA QUAZI
#Enrollment- 0176Al231052
#Batch- 2027(5)
#Batch time- 10:30-12:10


#BASIC IF-ELSE PROBLEMS:

    
#Q1 Write a program to check whether a number is positive, negative, or zero.
num= int(input("Enter Number:"))
if num >0:
    print("Number is positive")
elif num <0:
    print("Number is negative")
else:
    print("Number is zero")


#Q2 Write a program to check whether a number is even or odd.
    num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


#Q3 Write a program to check if a given year is a leap year or not.
year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    print("Year is a Leap Year")
else:
    print("Year is Not a Leap Year")


#Q4 Write a program to find the greatest of two numbers.
    

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("a is greatest number")
elif b > a:
    print("b is greatest number")
else:
    print("Both numbers are equal")


#Q5Write a program to check whether a person is eligible to vote (age >= 18).
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


#Q6Write a program to check whether a given character is a vowel or consonant.
ch= input("Enter a character: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("This character is a Vowel")
else:
    print("This character is a Consonant")


#Q7Write a program to check if a number is divisible by 5.
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(" Number is divisible by 5.")
else:
    print("Number is not divisible by 5.")


#Q8Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number
num = int(input("Enter a number: "))
digits = len(str(abs(num)))
if digits == 1:
    print("Number is a single-digit number.")
elif digits == 2:
    print("Number is a two-digit number.")
else:
    print("Number has more than two digits.")


#Q9Write a program to check whether a student has passed or failed (passing marks = 40).
marks = int(input("Enter student's marks: "))
if marks >= 40:
    print("Result: Passed")
else:
    print("Result: Failed")


#Q10Write a program to find whether the entered number is a multiple of both 3 and 7.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Number is a multiple of both 3 and 7.")
else:
    print("Number is NOT a multiple of both 3 and 7.")



#LADDER IF & NESTED IF:

#Q1 Write a program to find the greatest among three numbers.
# Program to find the greatest among three numbers

# Take input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a >= b and a >= c:
    print(f"The greatest number is {a}")
elif b >= a and b >= c:
    print(f"The greatest number is {b}")
else:
    print(f"The greatest number is {c}")



#Q2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
age = int(input("Enter age: "))

if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
elif 20 <= age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior")


#Q3. Write a program to assign grades based on marks:90-100: A,75-89: B,50-74: C,35-49: D,<35: Fail.
marks = int(input("Enter marks (0-100): "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks <= 89:
    print("Grade: B")
elif 50 <= marks <= 74:
    print("Grade: C")
elif 35 <= marks <= 49:
    print("Grade: D")
else:
    print("Grade: Fail")


#Q4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")


#Q5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
ch = input("Enter a single character: ")

if len(ch) = 1:
    print("Please enter only one character")
else:
    if ch.isupper():
        print("The character is Uppercase.")
    elif ch.islower():
        print("The character is Lowercase.")
    elif ch.isdigit():
        print("The character is a Digit.")
    else:
        print("The character is a Special Character.")



#Q6. Write a program to calculate electricity bill based on units: Up to 100 units: ₹5 per unit, 101–200 units: ₹7 per unit, Above 200 units: ₹10 per unit.
units = int(input("Enter total units consumed: "))

if units <= 100:
    bill = units * 5
elif 101<= units <= 200:
    bill = units * 7
else:
    bill = units * 10

print(f"Total Electricity Bill: ₹{bill}")


#Q7. Write a program to determine the largest of four numbers using nested if.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    if a > c:
        if a > d:
            largest = a
        else:
            largest = d
    else:
        if c > d:
            largest = c
        else:
            largest = d
else:
    if b > c:
        if b > d:
            largest = b
        else:
            largest = d
    else:
        if c > d:
            largest = c
        else:
            largest = d

print(f"The largest number is {largest}")


#Q8. Write a program to check if a given year is a century year and also a leap year.
year = int(input("Enter a year: "))

if year % 100 == 0:
    print(f"{year} is a Century Year.")
else:
    print(f"{year} is NOT a Century Year.")

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")


#Q9. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9),Obese (30+).
bmi = float(input("Enter BMI value: "))

if bmi < 18.5:
    print("BMI Category: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("BMI Category: Normal")
elif 25 <= bmi <= 29.9:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")



#Q10. Write a program to display the smallest number among three using nested if.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a < b:
    if a < c:
        smallest = a
    else:
        smallest = c
else:
    if b < c:
        smallest = b
    else:
        smallest = c
print(f"The smallest number is {smallest}")




#FOR LOOP PROBLEMS:

#Q1. Write a program using a for loop to print all Armstrong numbers between 100 and 999.(Armstrong number:sum of cubes of digits equals the number itself. Example: 153 => 13+53+33 = 153).
print("Armstrong numbers between 100 and 999:")

for num in range(100, 1000):  
    d1 = num // 100      
    d2 = (num // 10) % 10  
    d3 = num % 10         
    if (d1**3 + d2**3 + d3**3) == num:
        print(num)



#Q2. Write a program to generate and display the first n prime numbers using a for loop.
#-------

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter how many prime numbers you want: "))

print(f"The first {n} prime numbers are:")

count = 0 
num = 2 

while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1


#Q3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
#--------
    

def digit_sum(num):
    return sum(int(d) for d in str(num))

print("Numbers between 1 and 500 divisible by 3 with digit sum ≤ 10:")

for i in range(1, 501):
    if i % 3 == 0 and digit_sum(i) <= 10:
        print(i, end=" ")



#Q4. Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:
n = int(input("Enter the height of the pyramid: "))

for i in range(1, n + 1):
   
    a = " " * (n - i)
    b = "*" * (2 * i - 1)
    print(a+b)


#Q5. Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once)using a for loop.
#--------

text = input("Enter a string: ").lower

alphabets = "abcdefghijklmnopqrstuvwxyz"
found = True

for ch in alphabets:
    if ch not in text:
        found = False
        break

if found:
    print("The string is a pangram.")
else:
    print("The string is NOT a pangram.")



#Q6. Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of prime numbers with a difference of 2, e.g., (3,5), (11,13)).
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Twin primes between 1 and 100 are:")
for num in range(2, 100):
    if is_prime(num) and is_prime(num + 2):
        print(f"({num}, {num+2})")


#Q7. Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop.
num = int(input("Enter a number: "))

sum_of_digits = 0
for digit in str(num):
    sum_of_digits += int(digit)

if num % sum_of_digits == 0:
    print(num, "is a Harshad number.")
else:
    print(num, "is not a Harshad number.")



#Q8. Write a program to generate Pascal’s Triangle up to n rows using a for loop.
    #---------
n = int(input("Enter number of rows: "))

for i in range(n):
    
    print(" " * (n - i), end="")

    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        
        value = value * (i - j) // (j + 1)

    print()



#Q9. Write a program using a for loop to display the sum of the series: 12 + 22 + 32 + ... + n2
n = int(input("Enter the value of n: "))

sum_series = 0

for i in range(1, n + 1):
    sum_series += i**2

print("Sum of the series 1^2 + 2^2 + ... +", n, "^2 =", sum



#Q10. Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.
#-------
      
num = int(input("Enter a number: "))

original_num = num
sum_of_factorials = 0

for digit in str(num):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    sum_of_factorials += fact


if sum_of_factorials == original_num:
    print(original_num, "is a Strong number.")
else:
    print(original_num, "is not a Strong number.")




#WHILE LOOP PROBLEMS:


#Q11. Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime.
#______

num = int(input("Enter a number: "))

rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed number:", rev)


if rev < 2:
    print(rev, "is not prime.")
else:
    is_prime = True
    i = 2
    while i <= rev // 2:
        if rev % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(rev, "is prime.")
    else:
        print(rev, "is not prime.")



#Q12. Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
#------
total_digit_sum = 0  

while total_digit_sum <= 100:
    num = int(input("Enter a number: "))

   
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)

    total_digit_sum += digit_sum
    print(f"Sum of digits of {num} = {digit_sum}, Total = {total_digit_sum}")

print("Stopping program. Total digit sum exceeded 100!")


#Q13. Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).
#______
num = input("Enter a number: ")

if num[0] == "0":
    print(num, "is NOT a Duck number (starts with zero).")
else:
    i = 0
    found_zero = False
    
    while i < len(num):
        if num[i] == "0":
            found_zero = True
            break
        i += 1

    if found_zero:
        print(num, "is a Duck number.")
    else:
        print(num, "is NOT a Duck number.")



#Q14. Write a program using a while loop to accept a number and check if it is a Happy number. (A number is  happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a  happy number.
#-------
num = int(input("Enter a number: "))

def sum_of_squares(n):
    s = 0
    while n > 0:
        digit = n % 10
        s += digit * digit
        n //= 10
    return s

seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    num = sum_of_squares(num)

if num == 1:
    print("It is a Happy number.")
else:
    print("It is NOT a Happy number.")



#Q15. Write a program using a while loop to find the largest prime factor of a given number.

num = int(input("Enter a number: "))
n = num
factor = 2
largest = 1

while n > 1:
    if n % factor == 0:
        largest = factor
        n //= factor   
    else:
        factor += 1
        
print("Largest prime factor of", num, "is:", largest)


#Q16. Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
#--------
while True:
    s = input("Enter a string: ")

    if s == s[::-1]:
        print(s, "is a palindrome! Program stopped.")
        break
    else:
        print(s, "is NOT a palindrome. Try again.")



#Q17. Write a program using a while loop to compute the sum of digits of a number until the result becomes a  single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.
#-------
num = int(input("Enter a number: "))

while num >= 10:   # repeat until single-digit
    sum_digits = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_digits += digit
        temp //= 10
    num = sum_digits   # update num with new sum

print("Digital root is:", num)



#Q18. Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even => n/2, if odd => 3n+1. Continue until n=1).
n = int(input("Enter a number: "))

print("Collatz sequence:")

while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

print(1)



#Q19. Write a program using a while loop to accept a number and check whether it is a Kaprekar number.(Kaprekar number: if square of the number can be split into two parts whose sum equals the number.Example: 452=2025 => 20+25=45).
#---------
num = int(input("Enter a number: "))

sq = num * num
d = len(str(num))

right_part = sq % (10 ** d)
left_part = sq // (10 ** d)

while True:
    if left_part + right_part == num:
        print(num, "is a Kaprekar number.")
    else:
        print(num, "is NOT a Kaprekar number.")
    break



#Q20. Write a program to simulate an ATM machine using a while loop where a user can:
#• Check balance
#• Deposit money
#• Withdraw money (only if balance is sufficient)
#• Exit
#Continue until the user chooses to exit.

#-------

balance = 0  

while True:
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposited:", amount, "| New balance:", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            balance -= amount
            print("Withdrew:", amount, "| New balance:", balance)

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1–4.")




































    
