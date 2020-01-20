
#a) Round of the given floating point number. Example:  n=0.543 then round it next 
#   decimal number, i.e n=1.0 Use round() function
import math,random

x = 6.574
print("Round value of {} is: ".format(x), round(x))

# b) Find out the square root of a given number. (Use sqrt(x) function)
y = 9
print("Square root of {} is".format(y),math.sqrt(y))

#c) Generate random number between 0, and 1 ( use  random() function)
print("random value: -->",random.randint(0,1))

# d) Generate random number between 10 and  500. (Use uniform() function)
print("uniform value: -->",random.uniform(10,500))

#e) Explore all Math and Random module functions  on a given number/ List.
a = 2.73
print("ceil value: -->",math.ceil(a))
print ("floor value: -->",math.floor(a)) 
print ("absolute value: -->",math.fabs(a))
print ("factorial value: -->",math.factorial(int(a))) 
print ("copysign value: -->",math.copysign(5.5, -10))


print("random value: -->",random.randrange(0, 101, 2))
print("random choie: -->",random.choice(['win', 'lose', 'draw']))













