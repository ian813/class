#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import numpy as np
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window() # 창 최대화

driver.get('https://finance.naver.com/item/sise_day.nhn?code=005930&page=1')  # 크롤링할 사이트 호출
date_data_list = list()
cost_data_list = list()
trade_amount_data_list = list()

num=1
for i in range(4) :
    for j in range(2,11) :
        date_data=driver.find_elements_by_xpath('//html/body/table[1]/tbody/tr[*]/td[1]/span')
        cost_data=driver.find_elements_by_xpath('//html/body/table[1]/tbody/tr[*]/td[2]/span')
        trade_amount_data=driver.find_elements_by_xpath('//html/body/table[1]/tbody/tr[*]/td[7]/span')
        for k in date_data :
            date_data_list.append(k.text)
        for k in cost_data :
            cost_data_list.append(k.text)
        for k in trade_amount_data :
            trade_amount_data_list.append(k.text)
        num+=1
        btn = driver.find_element_by_link_text(str(num))
        btn.click()
    date_data=driver.find_elements_by_xpath('//html/body/table[1]/tbody/tr[*]/td[1]/span')
    cost_data=driver.find_elements_by_xpath('//html/body/table[1]/tbody/tr[*]/td[2]/span')
    trade_amount_data=driver.find_elements_by_xpath('//html/body/table[1]/tbody/tr[*]/td[7]/span')
    for k in date_data :
        date_data_list.append(k.text)
    for k in cost_data :
        cost_data_list.append(k.text)
    for k in trade_amount_data :
        trade_amount_data_list.append(k.text)
    btn = driver.find_element_by_partial_link_text('다음')
    btn.click()
    num+=1
df = pd.DataFrame(list(zip(date_data_list, cost_data_list, trade_amount_data_list)) ,columns=['data','cost','trade_amount'])
df.to_csv('C:/Users/User/Desktop/project/samsung.csv')

driver.quit()

df


# In[2]:


labels = pd.read_csv('samsung.csv')
                     #dtype = {"cost" : float, "trade_amount" : float})
    
df1 = labels.head(200)
df1['cost'] = df1["cost"].str.replace(pat=r'[^\w]', repl=r'', regex=True)
df1['trade_amount'] = df1["trade_amount"].str.replace(pat=r'[^\w]', repl=r'', regex=True)
df1


# In[3]:


df1["cost"] = df1.cost.astype(float)
df1["trade_amount"] = df1.trade_amount.astype(float)


# In[4]:


#training data 설정
x = df1.cost[:-100]
y = df1.trade_amount[:-100]


# In[5]:


#test data 설정
x1 = df1.cost[-100:] # test feature data
y1 = df1.trade_amount[-100:] # test feature data


# In[6]:


x_train = x.values.reshape(1, -1)
y_train = y.values.reshape(1, -1)


# In[7]:


x_test = x1.values.reshape(1, -1)
y_test = y1.values.reshape(1, -1)


# In[8]:


from sklearn.ensemble import RandomForestClassifier

#tree의 개수 Random Forest 분류 모듈 생성
rfc = RandomForestClassifier(n_estimators=10)
print(rfc)


# In[9]:


# rfc.fit()에 training data를 입력해 Random Forest 모듈을 학습
rfc.fit(x_train, y_train)

#Test data를 입력해 target data를 예측
prediction = rfc.predict(x_test)

#예측 결과 precision과 실제 test data의 target을 비교
print(prediction==y_test)


# In[ ]:




