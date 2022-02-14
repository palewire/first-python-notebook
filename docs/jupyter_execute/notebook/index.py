#!/usr/bin/env python
# coding: utf-8

# # Chapter 2: Hello notebook
# 
# Now you are all setup and ready to start writing Python code.
# 
# Do not stress. There is nothing too fancy about it. You can start by just doing a little simple math.
# 
# Type the following into the first box, then hit the play button in the toolbar above the notebook (or hit `SHIFT+ENTER` on your keyboard).

# In[1]:


2+2


# There. You have just written your first Python code. You have entered two integers and added them together using the plus sign operator.
# 
# Not so bad, right?
# 
# ```{note}
# If you get an error after you run a cell, look carefully at your code and see that it exactly matches what's been written in the example. Don't worry.
# 
# Code crashes are a normal part of life for computer programmers. They're usually caused by small typos that can be quickly corrected.
# ```
# 
# This to-and-fro of writing Python code in a notebook cell and then running it with the play button is the rhythm of working in a notebook. Over time you will gradually stack cells to organize an analysis that runs from top to bottom.
# 
# The cells can contain variables, functions and other Python tools.
# 
# A simple example would be storing your number in a variable in one cell ...

# In[2]:


number = 2


# ... then adding it to another number in the next.

# In[3]:


number + 3


# Run those two cells in succession and the notebook should output the number five. Change the number value to 3 and run both cells again and it should output six.
# 
# ```{note}
# If you've never written Python before, we recommend [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) and subsequent sections of python.org's tutorial.
# ```
# 
# Once you've got the hang of making the notebook run, you're ready to introduce pandas, the powerful Python analysis library that can do a whole lot more than add a few numbers together.
