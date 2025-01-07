#!/usr/bin/env python
# coding: utf-8

# # Write a Python program that takes a student's marks in three subjects as input.
# •	If the average is greater than or equal to 90, print "Grade: A".
# •	If the average is between 80 and 89, print "Grade: B".
# •	If the average is between 70 and 79, print "Grade: C".
# •	Otherwise, print "Grade: Fail".
# 

# In[4]:


sub1 = int(input("Enter marks of subject-01 : " ))
sub2 = int(input("Enter marks of subject-02 : " ))
sub3 = int(input("Enter marks of subject-03 : " ))
avg = (sub1 + sub2 + sub3)/3
if avg >= 90:
    print("Grade: A")
elif 80 <= avg < 90:  
    print("Grade: B")
elif 70 <= avg < 80:  
    print("Grade: C")
else :
    print("Grade : Fail")
    


# In[ ]:




