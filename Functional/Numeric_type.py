#!/usr/bin/env python
# coding: utf-8

# ### Coercing Floats to Integers

# #### Truncation
# 
# 
# truncating a float simply returns the integer portion of the number i.e. ignores everything after the decimal point

# In[1]:


from math import trunc


# In[2]:


help(trunc)


# In[3]:


trunc(10.3), trunc(10.5), trunc(10.6), trunc(10.9)


# In[4]:


trunc(-10.6), trunc(-10.5), trunc(-10.3)


# The **int** constructor uses truncation when a float is passed in:

# In[5]:


int(10.3), int(10.5), int(10.6)


# In[6]:


int(-10.5), int(-10.5), int(-10.4)


# #### Floor
# 
# 
# The floor of a number is the largest integer less than (or equal to) the number.
# 
# For positive numbers, floor and truncation are equivalent but not for negative numbers!

# <img src='1.png'/>

# In[7]:


from math import floor


# In[8]:


floor(10.4), floor(10.5), floor(10.6)


# In[9]:


floor(-10.4), floor(-10.5), floor(-10.6)


# #### Ceiling
# 
# 
# The ceiling of a number is the smallest integer greater than (or equal to) the number

# 

# In[12]:


from math import ceil


# In[13]:


ceil(10.4), ceil(10.5), ceil(10.6)


# In[14]:


ceil(-10.4), ceil(-10.5), ceil(-10.6)


# ## Rounding

# In[15]:


help(round)


# In[16]:


a = round(1.9)
a, type(a)


# In[17]:


a = round(1.9, 0)
a, type(a)


# In[19]:


round(1.8888888, 3), round(1.888888, 0)


# In[23]:


round(888.888, 1), round(888.888, 0), round(888.888, -1), round(888.888, -2),round(888.888, -4)  # it is closer to zero (which is muktiple of 10000) than 10,000
# rounding to the closest multiple 


# ### Ties 

# In[29]:


round(1.25), round(1.25, 1), round(1.35, 1)


# In[28]:


round(-1.25, 1), round(-1.35,1)


# **Rounding to closest, ties away from zero**
# 
# This is traditionally the type of rounding taught in school, which is different from the Banker's Rounding implemented in Python (and in many other programming languages)
# 
# 
# 1.5 --> 2 <br>
# 2.5 --> 3 <br>
# 
# -1.5 --> -2 <br>
# -2.5 --> -3 <br>
# 
# To do this type of rounding (to nearest 1) we can add (for positive numbers) or subtract (for negative numbers) 0.5 and then truncate the resulting number.

# In[30]:


def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))


# In[31]:


round(1.5), _round(1.5)


# In[32]:


round(2.5), _round(2.5)


# In[33]:


round(-2.5), _round(-2.5)


# ## Decimals
# 
# 
# Decimals have context, that can be used to specify rounding and precision (amongst other things)

# In[34]:


import decimal
from decimal import Decimal


# #### Global Context

# In[35]:


g_ctx  = decimal.getcontext()
g_ctx.prec


# In[36]:


g_ctx.rounding


# We can change settings in the global context:

# In[37]:


g_ctx.prec = 6
g_ctx.rounding = decimal.ROUND_HALF_UP


# And if we read this back directly from the global context:

# In[39]:


decimal.getcontext().prec


# In[40]:


decimal.getcontext().rounding


# #### Local Context

# The ``localcontext()`` function will return a context manager that we can use with a ``with`` statement:

# In[41]:


with decimal.localcontext() as ctx:
    print(ctx.prec)
    print(ctx.rounding)


# Since no argument was specified in the ``localcontext()`` call, it provides us a context manager that uses a copy of the global context.
# 
# 
# Modifying the local context has no effect on the global context

# In[42]:


with decimal.localcontext() as ctx:
    ctx.prec = 10
    print('local prec = {0}, global prec = {1}'.format(ctx.prec, g_ctx.prec))


# In[43]:


decimal.getcontext().rounding


# In[44]:


x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))


# In[45]:


decimal.getcontext().rounding = decimal.ROUND_HALF_UP


# In[46]:


x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))


# As you may have realized, changing the global context is a pain if you need to constantly switch between different precisions and rounding algorithms. Also, it could introduce bugs if you forget that you changed the global context somewhere further up in your module.
# 
# For this reason, it is usually better to use a local context manager instead:

# In[47]:


decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN


# In[48]:


x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1), round(y, 1))
with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))
print(round(x, 1), round(y, 1))


# ## Booleans

# In[71]:


# Boolean 
(True + True + True) % 2


# In[51]:


True * False


# In[53]:


issubclass(bool, int)


# In[55]:


type(True), id(True), int(True)


# In[57]:


3 < 10, id(3 < 10)


# In[61]:


(3 < 4) is True


# In[62]:


(1 == 2) == False


# In[65]:


1 == 2 == False 


# In[66]:


1 == 2 and 2 == False


# In[67]:


int(True), int(False)


# In[69]:


True > False


# In[74]:


id(bool(0)), bool(1), bool(0), bool(100), bool(-2)


# In[75]:


bool([])


# In[78]:


bool(100), 100!=0, (100).__bool__()


# In[80]:


#help(list)


# In[81]:


'a' or [1,2]


# In[82]:


'' or [1, 2]


# In[ ]:




