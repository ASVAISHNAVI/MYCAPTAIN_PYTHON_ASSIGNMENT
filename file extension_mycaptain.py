#!/usr/bin/env python
# coding: utf-8

# In[ ]:


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

