#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter no of terms"))
n1=0
n2=1
count=0
if n==1:
    print(n1)
else:
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


# In[ ]:




