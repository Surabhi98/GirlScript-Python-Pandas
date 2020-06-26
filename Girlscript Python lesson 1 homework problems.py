#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Hello World
print("hello world")


# In[2]:


#Variables
counter=100
miles=1000.0
name="john"
print(counter)
print(miles)
print(name)


# In[3]:


x="hello world"
print(x)
x=20
print(x)
x=20.5
print(x)
x=["apple","banana","cherry"]
print(x)
x=("apple","banana","cherry")
print(x)
x=range(6)
print(x)
x={"name":"John","age":36}
print(x)
x={"apple","banana","cherry"}
print(x)


# In[4]:


#Type Casting
x=int(1)
y=int(2.8)
z=int("3")

print(x)
print(y)
print(z)


# In[5]:


#operators
a=21
b=10
c=0
c=a+b
print("Line 1- Value of c is",c)
c=a-b
print("Line 2- Value of c is",c)
c=a*b
print("Line 3- Value of c is",c)
c=a/b
print("Line 4- Value of c is",c)
c=a%b
print("Line 5- Value of c is",c)

a=2
b=3
c=a**b
print("Line 6- Value of c is",c)

a=10
b=5
c=a//b
print("Line 7- Value of c is",c)


# In[6]:


#Boolean
print(10>9)
print(10==9)
print(10<9)


# In[11]:


#List
list=['abcd',786,2.23,'john',70.2]
tinylist=[123,'john']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list+tinylist)


# In[14]:


#Positive Numbers Program
num=float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num==0:
    print("Zero")
else:
    print("Negetive")


# In[15]:


#Leap year calculator
year=2000

if (year%4)==0:
    if (year%100)==0:
        if(year%400)==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")


# In[17]:


def function(fname):
    print(fname + " Refsnes")
function("Emil")
function("Tobias")
function("Linus")


# In[18]:


def info(name,age):
    print("Name: ",name)
    print("Age: ",age)
    return
info("Miki",21)


# In[19]:


#Random numbers
import random
print(random.randint(0,9))


# In[43]:


#Check if number is even or odd
num=float(input("Choose a number: "))
if num % 2 ==0:
    print("Number is even")
else:
    print("Number is odd")


# In[52]:


#Check if number is prime or not
def prime(n):
    if n==0 or n==1:
        return print(n,"is not a prime number")
    for i in range(2,n):
        if (n%i)!=0:
           return print(n,"is a prime number")
        else:
           return print(n,"is not a prime number")
prime(3)
prime(4)
prime(5)
prime(6)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




