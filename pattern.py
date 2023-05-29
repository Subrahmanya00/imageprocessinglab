#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(n+1,0,-1):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i-1):
		
			# printing stars
			print("* ",end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
pypart(n)


# In[15]:


# This is the example of print simple reversed right angle pyramid pattern  
rows = int(input("Enter the number of rows:"))  
k = 2 * rows - 2  # It is used for number of spaces  
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2   # decrement k value after each iteration  
    for j in range(0, i + 1):  
        print("* ", end="")  # printing star  
    print("")  


# In[22]:


rows = int(input("Enter the number of rows: "))  
# Outer loop will print number of rows  
for i in range(rows+1):  
    # Inner loop will print the value of i after each iteration  
    for j in range(i):  
        print(i, end=" ")  # print number  
    # line after each row to display pattern correctly  
    print(" ")  


# In[58]:


print("Print equilateral triangle Pyramid with characters ")  
s = 5  
asciiValue = 65  
m = (2 * s) - 2  
for i in range(0, s):  
    for j in range(0, m):  
        print(end=" ")  
    # Decreased the value of after each iteration  
    m = m - 1  
    for j in range(0, i+1):  
        alphabate = chr(asciiValue)  
        print(alphabate, end=' ')  
        # Increase the ASCII number after each iteration  
        asciiValue +=1
            
    print()  


# In[7]:


# number diamond pattern
size = 5
num = 4

# upside pyramid
for i in range(1, size + 1):
    # printing spaces
    for j in range(size, i - 1, -1):
        print(" ", end="")
    # printing star
    for k in range(0, i * 2- 1):
        print(num, end="")
        num += 1
    # set the number to 1
    num = 4
    print()
# downside pyramid
for i in range(1, size):
    # printing spaces
    for j in range(0, i+1):
        print(" ", end="")
    # printing star
    for k in range((size - i) * 2- 1):
        print(num, end="")
        num += 1
    # set num to 1
    num = 4
    print()


# In[ ]:




