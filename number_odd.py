#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=5349
num_one=var_int%10
num_two=var_int%100//10
num_three=var_int//100%10
num_four=var_int//1000
#Print the number of odd digits in the variable "var_int
print((num_one)%2+(num_two)%2+(num_three)%2+(num_four)%2)
