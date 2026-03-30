#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


Books = pd.read_csv("Books.csv")
Ratings = pd.read_csv("Ratings.csv")
Users = pd.read_csv("Users.csv")


# In[3]:


print(Books.shape)
print(Ratings.shape)
print(Users.shape)


# In[4]:


Books.head()


# In[5]:


Ratings.head()


# In[6]:


Users.head()


# In[7]:


Books.isna().sum()


# In[8]:


Users.isna().sum()


# In[9]:


Ratings.isna().sum()


# In[10]:


Books.duplicated().sum()


# In[11]:


Users.duplicated().sum()


# In[12]:


Ratings.duplicated().sum()


# ## Popularity Based Recommender System

# In[13]:


rating_with_name = Ratings.merge(Books, on='ISBN')


# In[14]:


rating_with_name.head()


# In[15]:


num_rating_df = rating_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating':'num_rating'}, inplace=True)
num_rating_df


# In[16]:


num_rating_df


# In[17]:


rating_with_name['Book-Rating'] = pd.to_numeric(rating_with_name['Book-Rating'], errors='coerce')
avg_rating_df = rating_with_name.groupby('Book-Title').mean(numeric_only = True)['Book-Rating'].reset_index()
avg_rating_df.rename(columns={'Book-Rating':'avg_rating'},inplace=True)
avg_rating_df.head()


# In[18]:


rating_with_name.head()


# In[19]:


popular_df = num_rating_df.merge(avg_rating_df, on='Book-Title')


# In[20]:


popular_df.head()


# In[21]:


popular_df = popular_df[popular_df['num_rating'] >= 250].sort_values('avg_rating', ascending=False).head(50)


# In[22]:


popular_df


# In[23]:


popular_df = popular_df.merge(Books, on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M','num_rating','avg_rating']]


# In[24]:


popular_df


# In[25]:


popular_df['Image-URL-M'][0]


# # Collaborating Based Filterring Approach

# In[26]:


Books.head(1)


# In[27]:


Ratings.head(1)


# In[28]:


rating_with_name.head(1)


# In[29]:


x = rating_with_name.groupby('User-ID').count()['Book-Rating'] > 200
padhe_likhe_users = x[x].index


# In[30]:


padhe_likhe_users


# In[31]:


filtered_rating = rating_with_name[rating_with_name['User-ID'].isin(padhe_likhe_users)]


# In[32]:


y = filtered_rating.groupby('Book-Title').count()['Book-Rating'] >= 50
famous_books = y[y].index


# In[33]:


final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]


# In[34]:


final_ratings.head()


# In[35]:


pt = final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')


# In[36]:


pt.fillna(0, inplace=True)


# In[37]:


pt


# In[38]:


from sklearn.metrics.pairwise import cosine_similarity


# In[43]:


similarity_scores = cosine_similarity(pt)


# In[49]:


similarity_scores


# In[44]:


similarity_scores.shape


# In[81]:


def recommend(book_name):
  index = np.where(pt.index == book_name)[0][0]
  similar_books = sorted(list(enumerate(similarity_scores[index])), key=lambda x : x[1], reverse=True)[1:6]

  data = []

  for i in similar_books:
    item = []
    temp_df = Books[Books['Book-Title'] == pt.index[i[0]]]
    item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
    item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
    item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
    
    data.append(item)
  return data


# In[82]:


recommend('1984')


# In[66]:


Books[Books['Book-Title'] == pt.index[0]]


# In[83]:


Books.drop_duplicates('Book-Title')


# In[84]:


import pickle


# In[85]:


pickle.dump(popular_df, open("popular_df.pkl", "wb"))
pickle.dump(pt, open("pt.pkl", "wb"))
pickle.dump(Books, open("books.pkl", "wb"))
pickle.dump(similarity_scores, open("similarity_scores.pkl", "wb"))


# In[ ]:





# In[ ]:





# In[ ]:




