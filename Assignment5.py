#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("\t\t\t\t\t Assignment 5\n")


# In[4]:


# Task 1

print("\t\t\t Task 1\n")
def factorial(num):
    if num != 1:
        return num * (factorial(num-1))
    else:
        return 1

value =int(input("Enter the num of factorial: "))

print(factorial(value))


# In[5]:


# Task 2

print("\t\t\t Task 2\n")

def fahad(str):
    
    UPPER_CASE = 0;
    
    LOWER_CASE = 0;
    for case in str:
        if case.isupper():
            UPPER_CASE += 1
        elif case.islower():
            LOWER_CASE+= 1
            
    print ("Original String : ", str)
    print ("No. of Upper case characters : ", UPPER_CASE)
    print ("No. of Lower case Characters : ", LOWER_CASE)

fahad('My Name Is jaffar abbas 12')


# In[6]:


# Task 3

print("\t\t\t Task 3\n")
def myprint(n):
    print(n, end = " ")

mylist = [1,2,3,4,5,6,7,8,9,10] 
  

for num in mylist: 
      

    if num % 2 == 0: 
       myprint(num)


# In[10]:


# Task 4

print("\t\t\t Task 4\n")

def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True
print(isPalindrome('ada'))


# In[12]:


# Task 5

print("\t\t\t Task 5\n")

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True     
    
value = int(input("Enter the prime number : "))
print(test_prime(value))


# In[13]:


# Task 6

print("\t\t\t Task 6\n")

def printmany(*param):

    print(*param)

printmany("My","Name","Is","Jaffar","Abbas")


# In[ ]:




