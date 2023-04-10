#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


raw_csv_AbilityStats = pd.read_csv('agents_abilities_stat.csv')


# In[7]:


df = raw_csv_AbilityStats.copy()


# In[9]:


pd.options.display.max_rows = None


# In[10]:


df


# In[18]:


matchesxx = []
mapxx = []
Rankxx = []
for i in range(df.shape[0]):
    x = df['Matches'][i].replace(",",'')
    y = df['Map'][i].replace("all","AllMaps")
    z = str(df['Game Rank'][i]).replace(" ","_")
    Rankxx.append(z)
    matchesxx.append(x)
    mapxx.append(y)
matchesxx = pd.Series(matchesxx)
mapxx = pd.Series(mapxx)
Rankxx = pd.Series(Rankxx)


# In[15]:


df['Ultimate'].max()


# In[20]:


df = df.drop(['Map', 'Game Rank', 'Matches'], axis = 1)


# In[23]:


df = pd.concat([df, mapxx, Rankxx, matchesxx], axis = 1)


# In[25]:


df.columns.values


# In[26]:


df.head()


# In[27]:


col_rename = ['Rank', 'Name', 'Game Type', '1st Ability', '2nd Ability',
       '3rd Ability', 'Ultimate', 'Map', 'Game Rank', 'Matches']


# In[28]:


df.columns = col_rename


# In[31]:


df = df.drop(['Rank'], axis = 1)


# In[33]:


col_reorder = ['Name', 'Game Type', 'Map', 'Game Rank', '1st Ability', '2nd Ability',
       '3rd Ability', 'Ultimate', 'Matches']


# In[34]:


df = df[col_reorder]


# In[36]:


df.head()


# In[38]:


df.max()


# In[39]:


import pymysql


# In[41]:


conn = pymysql.connect(database = 'Valorant_V1', user = 'root', password = '365Pass')


# In[42]:


cursor = conn.cursor()


# In[44]:


insert_part_of_query = 'Insert into ability_stats (Agent_Name, Game_Type, Map, Game_Rank, 1st_Ability, 2nd_Ability, 3rd_Ability, Ultimate, Matches) values '
for i in range(df.shape[0]):
    main_query = "("
    for j in df.columns:
        main_query = main_query + '\'' + str(df[j][i]) + '\',' 
    main_query = main_query[:-1]
    main_query = main_query + "), "
    insert_part_of_query = insert_part_of_query + main_query
insert_part_of_query = insert_part_of_query[:-2]
insert_part_of_query = insert_part_of_query + ";"


# In[45]:


insert_part_of_query


# In[46]:


cursor.execute(insert_part_of_query)


# In[47]:


conn.commit()

