#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=5896
#Create a variable "sum_odd" and assign it 0.
sum_odd=(var_int%10)%2*(var_int%10)+(var_int%100//10)%2*(var_int%100//10)+(var_int//100%10)%2*(var_int//100%10)+(var_int//1000)%2*(var_int//1000)
#Find the sum of the odd digits in the variable "var_int".
print(sum_odd)
