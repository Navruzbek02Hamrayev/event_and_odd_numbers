#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=8566
num_one=var_int%10
num_two=var_int%100//10
num_three=var_int//100%10
num_four=var_int//1000
#Print the number of even digits in the variable "var_int".
print((num_one+1)%2+(num_two+1)%2+(num_three+1)%2+(num_four+1)%2)
