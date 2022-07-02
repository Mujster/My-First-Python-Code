var="My Name Is Mujster -aka Mujtaba"
var2="And I am a student"

print(var,var2)
print("String 1 Slicing [:8]:\t",var[:8])
print("String 2 Slicing [:4]:\t",var2[:4])

print("String 1 Slicing skipping 2 letters [::2]:\t",var[::2])
print("String 2 Slicing skipping 2 letters [::2]:\t",var2[::2])

var=input("Enter your 1st string")
var2=input("Enter your 2nd string")

print(var,var2)

var=input("Enter your 1st Number")
var2=input("Enter your 2nd Number")

print(var,"+",var2,"=",int(var)+int(var2))
print(var,"*",var2,"=",int(var)*int(var2))