#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add (a,b):
    return a+b
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return(a/b)
def default(a,b):
    return "incorrect option"
switcher={
    1:add,
    2:diff,
    3:mul,
    4:div
}


# In[ ]:


a=int(input("enter the value1:"))
b=int(input("enter the value2:"))
if a>b:
    for i in range(b):
        print(i)
else:
    print("false")


# In[ ]:


a=int(input("enter the number:"))
while a>5:
    if a%2==0:
        print("even")
    else:
        print("odd")
while a<5:
    print("not valid")


# In[ ]:


def add(a,b):
    return a+b
n=int(input("enter the number:"))
g=int(input("eneter the number:"))
add(n,g)
    


# In[2]:


fruits=["apple","banana","cherry"]
print(fruits[1])


# In[3]:


fruits.append("orange")


# In[4]:


fruits


# In[5]:


fruits.remove("apple")


# In[6]:


fruits


# In[7]:


print(fruits[1:3])


# In[8]:


print(fruits[1])


# In[9]:


student={"name":"John","age":25,"courses":{"Math","Science"}}


# In[10]:


print(student["name"])


# In[11]:


student["age"]=26


# In[12]:


student["grade"]="A"


# In[13]:


del student["age"]
print(student["grade"])


# In[1]:


student={"name":"John","age":25,"courses":{"Math","science"}}
print(student['name'])


# In[10]:


student['age']=26


# In[14]:


student["grade"]="A"
print(student)


# In[12]:


del student["age"]


# In[13]:


print(student)


# In[15]:


for key,value in student.items():
    print(key,value)


# In[19]:


numbers={1,2,3,4,5}
numbers.add(6)


# In[21]:


evens={2,4,6,8}
union=numbers|evens
intersection=numbers-evens
print(intersection)


# In[ ]:


#file
with open("example.txt",'r')


# In[23]:


try:
    result=10/0
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid value")
finally:
    print("Thankyou!!")
    


# In[26]:


try:
    result=int("avc")
except (ZeroDivisionError,ValueError) as e:
    print("e")


# In[28]:


try:
    file=open("example.txt",'r')
    content=file.read()
except FileNotFoundError:
    print("The file was not found")
finally:
    if "file" is locals():
        file.close()
        print("File closed")


# In[29]:


def divide(a,b):
    if b==0:
        raise ValueError("The divisor cannot be zero")
    return a/b
try:
    result=divide(10,0)
except ValueError as e:
    print(e)


# In[30]:


def safe_divide(a,b):
    try:
        result =a/b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error:Both arguments must be numbers!")
    else:
        print(f"Resul:{result}")
    finally:
        print("Exection completed")
safe_divide(10,2)
safe_divide(10,0)


# In[33]:


#Calculate Average Mark of Student
one=int(input("enter M"))
two=int(input("enter E"))
three=int(input("enter P"))
four=int(input("enter C"))
five=int(input("enter T"))

avg=(one+two+three+four+five)/5
print("Average marks is",avg)


# In[34]:


n=2
for i in range(2):
    na=input("Enter the name:")
    one=int(input("enter M"))
    two=int(input("enter E"))
    three=int(input("enter P"))
    four=int(input("enter C"))
    five=int(input("enter T"))
    avg=(one+two+three+four+five)/5
    print("Average marks is",avg)



# In[42]:


#Find max and min value in a list
l=[1,2,3,4,5]
x=max(l)
print(x)
y=min(l)
print(y)


# In[55]:


#Counting the occurance of each word in a sentence
word="Hey folks i am very happy to announce the news to all"
v=word.split()
print(v)
hash_map={}
for wor in v:
    if wor not in hash_map:
        hash_map[wor]=1
    else:
        hash_map[wor]+=1
print(hash_map)
print(max(hash_map.values()))


# In[60]:


#palindrome
def isPalindrome(s):
    return s == s[::-1]

s = "nitin"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")


# In[70]:


#factorial
def facto(n):
    if n==1 or n==0:
        return 1
    else:
        print(n)
        return n*facto(n-1)
facto(5)


# In[ ]:




