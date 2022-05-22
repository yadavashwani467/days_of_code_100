#Add your code here
#fruits=["Apple","Peach","Pear"]
#for item in fruits:
#    print(item)

#Exercise 1: Average Height
#student_heights=input("Input a list of student heights").split()
#for n in range(0,len(student_heights)):
 #   student_heights[n]=int(student_heights[n])
#print(student_heights)

#Write your code below this row (to find average height)
#number_students=0
#sum_student_heights=0
#for item in student_heights:
 #   sum_student_heights=sum_student_heights+item
  #  number_students=number_students+1
#average_height=round(sum_student_heights/number_students)
#print(f"average height rounded to the nearest whole number = {average_height}")

#Exercise 2:Print sum of even numbers
#total=0
#for i in range(2,101,2):
 #   total+=i
#print(total)

#Exercise 3:Fizz Buzz challenge
#for i in range(1,101):
 #   if i%15==0:
  #      print("FizzBuzz")
   # elif i%5==0:
    #    print("Buzz")
    #elif i%3==0:
     #   print("fizz")
    #else:
     #   print(i)


#Final Exercise: Password Generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F'
'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input(f"How many symbols would you like?\n"))
nr_numbers=int(input(f"How many numbers would you like?\n"))

a=[]
for i in range(0,nr_letters):
    index=random.randint(0,len(letters))
    a.append(letters[index])
for j in range(0,nr_symbols):
    index=random.randint(0,len(symbols))
    a.append(symbols[index])
for k in range(0,nr_numbers):
    index=random.randint(0,len(numbers))
    a.append(numbers[index])
random.shuffle(a)
str1=""
print(str1.join(a))

