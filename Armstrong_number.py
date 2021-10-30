# building the armstrong number : 
n = int(input("Enter the number to be checked : ")) #to take input from the user
num = n #The value of 'n' is going to change in the further program, so num == n to store original number
a = 0 # Initializating a variable where the sum of digits of the number will be stored. 
y = len(str(n)) # to get the length of the number. By converting the number into string and then finding its length. 
print()
for i in range(len(str(n))) : #To repeat the loop for the number of digits present in the number. 
    b = n%10 # to get the last digit of the number
    n = n//10 # to remove the last digit of the number
    a = a + (b**y) # to store the power of the number in the a and then add it. 

print("The sum of digits is : ",a)

if a == num : # if sum of powers of number matches to the original number than it is armstrong number. 
    print("It is an Armstrong Number. ")

else : 
    print("Not an Armstrong Number.")

print()

"""
Code by Atharv Rastogi. 
v 1.0.1
DO NOT CHANGE THIS.
"""
