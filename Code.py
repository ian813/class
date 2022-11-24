#!/usr/bin/env python
# coding: utf-8

# In[1]:


# user가 이길 때까지 반복할 수 있는 카지노
import random

print("Welcome to Python Casino")

pc_choice = random.randint(1, 100)

playing = True

while playing:
    user_choice = int(input("Choose number (1-100):"))
    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower! Computer chose")
    elif user_choice < pc_choice:
        print("Higher! Computer chose")


# In[2]:


from requests import get

websites = ("google.com",
           "https://httpstat.us/502",
           "https://httpstat.us/404",
           "httpstat.us/300",
           "https://httpstat.us/200",
           "httpstat.us/101")

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code < 200:
        results[website] = "1xx/ informational response"
    elif response.status_code < 300:
        results[website] = "2xx/ successful"
    elif response.status_code < 400:
        results[website] = "3xx/ redirection"
    elif response.status_code < 500:
        results[website] = "4xx/ client error"
    else :
        results[website] = "5xx/ server error"
        
print(results)


# In[ ]:




