#!/usr/bin/env python
# coding: utf-8

# In[3]:


#calculator program for performing mathematical operations by using python

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
typeofoperation = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if typeofoperation == '+':
    result = a + b
elif typeofoperation == '-':
    result = a - b
elif typeofoperation == '*':
    result = a * b
elif typeofoperation == '/':
    result = a / b
else:
    print("Input character is incorrect")
print(a, typeofoperation , b, ":", result)


# In[ ]:




