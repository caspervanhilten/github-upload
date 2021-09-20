#!/usr/bin/env python
# coding: utf-8

# In[7]:


#libraries
import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt
from collections import namedtuple


# In[8]:


#loan characteristics
original_balance = 500000
coupon = 0.08
term = 120

#payments
periods = range(1, term+1)
interest_payment = npf.ipmt(
    rate = coupon /12, per=periods, nper=term, pv=-original_balance)
principal_payment = npf.ppmt(
    rate = coupon / 12, per=periods, nper=term, pv=-original_balance)


# In[9]:


plt.stackplot(periods, interest_payment, principal_payment,
                 labels=["interest","principal"])
plt.legend(loc="upper left")
plt.xlabel("Period")
plt.ylabel("Payment")
plt.margins(0,0)


# In[15]:


#pandas float formatting
pd.options.display.float_format = "{:,.2f}".format

#cash flow table
cf_data = {"interest": interest_payment, "principal": principal_payment}
cf_table = pd.DataFrame(data=cf_data,index=periods)
cf_table["Payment"] = cf_table["interest"] + cf_table["principal"]
cf_table["Ending Balance"] = original_balance -                 cf_table["principal"].cumsum()
cf_table["Beginning Balance"] = [original_balance] +                 list(cf_table["Ending Balance"])[:-1]
cf_table = cf_table[["Beginning Balance", "Payment", "interest", "principal", "Ending Balance"]]
cf_table.head(10)


# In[17]:


[original_balance] + list(cf_table["Ending Balance"])[:-1]


# In[ ]:




