import random
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!@#$%&*_{}[]/"
result=lower_case+upper_case+numbers+symbols
length=int(input("Enter the length of password:"))
password="".join(random.sample(result,length))
print("Generated Password:",password)