#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=8569
#Print the number of even digits in the variable "var_int".
print(int(var_int%1000%100%10%2==1),int(var_int%1000%100//10%2==1),int(var_int%1000//100%2==1),int(var_int//1000%2==1))

