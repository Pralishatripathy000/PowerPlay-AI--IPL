#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import io
import ipywidgets as widgets
from IPython.display import display

upload_hist = widgets.FileUpload(
    accept='.csv',
    multiple=False,
    description='Upload IPL.csv'
)

upload_2026 = widgets.FileUpload(
    accept='.csv',
    multiple=False,
    description='Upload IPL2026'
)

display(upload_hist)
display(upload_2026)


# In[ ]:




