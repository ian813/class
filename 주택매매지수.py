#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df_price = pd.read_csv("data/주택매매가격지수_시도_시_군_구__20220912074224.csv", encoding="cp949") #, nrows=3
df_price


# In[3]:


df = df_price.melt(id_vars="행정구역별")
df


# In[4]:


data_melt = pd.melt(df_price, id_vars="행정구역별", var_name='기간', value_name='주택매매가격지수')
data_melt


# In[5]:


data_melt["기간"].str.split(".", expand=True)[0]
data_melt["연도"] = data_melt["기간"].str.split(".", expand=True)[0]
data_melt["월"] = data_melt["기간"].str.split(".", expand=True)[1]
df1 = data_melt
df1


# In[6]:


df1["주택매매가격지수"] = df1["주택매매가격지수"].replace("0", np.nan)
df1["주택매매가격지수"] = df1["주택매매가격지수"].replace("-", np.nan)
df1["주택매매가격지수"] = pd.to_numeric(df1["주택매매가격지수"])


# In[7]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[8]:


df_nation = df1[data_melt["행정구역별"].isin(["전국"])]
df_nation.head()


# In[9]:


# 그래프 사이즈 변경하기 (가로, 세로)
plt.figure(figsize=(15, 4))

#  hue 인수에 카테고리 변수 이름을 지정하면, 카테고리 값에 따라 색상 변경
sns.pointplot(data=df_nation, x="연도", y="주택매매가격지수", hue="행정구역별")

# 레전드 "* 전국" 위치를 고정
plt.legend(bbox_to_anchor=(1, 1))


# In[ ]:




