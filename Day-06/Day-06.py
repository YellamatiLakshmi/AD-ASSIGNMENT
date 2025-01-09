#!/usr/bin/env python
# coding: utf-8

# In[3]:


l1 = [1,2,3,4,5,6]
list1 = l1[3:6]
print(list1,"\n")
print(l1[1::],"\n")
print(l1[1::4],"\n")
print(l1[::-1],"\n")
iterate_var = iter(l1)
print(iterate_var)


# In[4]:


for i in iterate_var :
    if i%2==0:
        print(i)


# In[17]:


def square(i):
    for i in range(i):
        i = i+1
    return i
res = square(10)
print(res)


# In[21]:


def square(i):
    for i in range(i):
        i = i+2
        yield i
square(10)
for i in square(10):
    print(i)


# In[22]:


def add(x,y):
    return x + y
res = add(10,20)
print(res)


# In[23]:


res = lambda x,y : x * y
print(res(10,20))


# In[27]:


multi = lambda x,y,z : x * y * z
print(multi(5,9,18))


# In[31]:


def sample(func):
    def wrapper(item):
        item = item.upper()
        return func(item)
    return wrapper
@sample
def process(item):
    return item

result = process
print(result("hello"))
print(result("good night 😴💤😪"))


# In[37]:


import pandas as pd
screen_time = [1,4,5,8,9,18,19,25]
std_name = ["a1","b2","c3","d4","e5","f6","g7","h8"]
id = [10,20,30,40,50,60,70,80]
dict1 = {"screen_time": screen_time, "std_name": std_name, "id": id}
print(dict1)
df = pd.DataFrame(dict1)
print("\n",df)


# In[40]:


df.head(3)


# In[41]:


df.head(7)


# In[44]:


df.tail(3)


# # create a dataframes product id, product_name, discount_percentage 
# with using lists and dictionares  create 20 rows from that
# get first 10 rows and last 10 rows

# In[7]:


import pandas as pd
product_id = ["p1","p2","p3","p4","p5","p6","p7","p8","p9","p10","p11","p12","p13","p14","p15","p16","p17","p18","p19","p20"]
product_name = ["prod1","prod2","prod3","prod4","prod5","prod6","prod7","prod8","prod9","prod10","prod11","prod12","prod13","prod14","prod15","prod16","prod17","prod18","prod19","prod20"]
discount_precentage = [1.6,2.8,4,3,1.9,7,2,5,4,4.3,2.9,9.3,1.8,2,5.3,6,2.6,4.7,1,6]
dict1 = {"product_id" : product_id,"product.name" : product_name, "discount_percentage" : discount_precentage}
print(dict1,"\n")
df = pd.DataFrame(dict1)
print(df)


# In[9]:


df.head(10)


# In[10]:


df.tail(10)


# In[ ]:




