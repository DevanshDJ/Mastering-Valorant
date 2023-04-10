#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


raw_csv_data = pd.read_csv('valo_agents_stat.csv')


# In[55]:


df = raw_csv_data.copy()


# In[56]:


df


# In[163]:


pd.options.display.max_rows = None


# In[7]:


df


# In[6]:


df.info()


# In[9]:


df['KDA'][0]


# In[10]:


K_D_A = df['KDA'][0].split('/')
K_D_A[0] = K_D_A[0].strip()
K_D_A[1] = K_D_A[1].strip()
K_D_A[2] = K_D_A[2].strip()
K_D_A


# In[57]:


K_D_A = []
K = []
D = []
A = []
for i in range(df.shape[0]):
    K_D_A.append(df['KDA'][i].split('/'))
    K.append(K_D_A[i][0].strip())
    D.append(K_D_A[i][1].strip())
    A.append(K_D_A[i][2].strip())

K = pd.Series(K)
D = pd.Series(D)
A = pd.Series(A)


# In[58]:


print('No. of rows of data = ', df.shape[0])
print('Length of K_D_A[]   = ', len(K_D_A))
print('Length of K[]       = ', len(K))
print('Length of D[]       = ', len(D))
print('Length of A[]       = ', len(A))


# In[59]:


df = pd.concat([df, K, D, A], axis = 1)


# In[10]:


df


# In[60]:


df.columns.values


# In[61]:


rename_cols = ['Rank', 'Name', 'Role', 'Game Type', 'Map', 'Game Rank', 'KD',
       'KDA', 'Win %', 'Pick %', 'Avg. Score', 'First Blood %', 'Matches',
       'K', 'D', 'A']


# In[62]:


df.columns = rename_cols


# In[14]:


df


# In[63]:


reorder_cols = ['Rank', 'Name', 'Role', 'Game Type', 'Map', 'Game Rank', 'KD',
       'KDA','K', 'D', 'A', 'Win %', 'Pick %', 'Avg. Score', 'First Blood %', 'Matches']


# In[64]:


df = df[reorder_cols]


# In[65]:


df


# In[66]:


df = df.drop(['KDA'], axis =1)


# In[67]:


df = df.drop(['Rank'], axis = 1)


# In[68]:


df.head(30)


# In[70]:


winxx = []
pickxx = []
fb = []
for i in range(df.shape[0]):
    winxx.append(float(df['Win %'][i][:-1]))
    pickxx.append(float(df['Pick %'][i][:-1]))
    fb.append(float(df['First Blood %'][i][:-1]))

winxx = pd.Series(winxx)
pickxx = pd.Series(pickxx)
fb = pd.Series(fb)


# In[21]:


pickxx


# In[71]:


df1 = df.copy()


# In[45]:


df = df1.copy()


# In[72]:


df = pd.concat([df, winxx, pickxx, fb], axis = 1)


# In[73]:


df = df.drop(['Win %'], axis = 1)


# In[74]:


df = df.drop(['Pick %'], axis = 1)


# In[75]:


df = df.drop(['First Blood %'], axis = 1)


# In[76]:


df.columns.values


# In[77]:


col_rename = ['Name', 'Role', 'Game Type', 'Map', 'Game Rank', 'KD', 'K', 'D',
       'A', 'Avg. Score', 'Matches',
       'Win %', 'Pick %', 'First Blood %']


# In[78]:


df.columns = col_rename


# In[79]:


col_reorder = ['Name', 'Role', 'Game Type', 'Map', 'Game Rank', 'KD', 'K', 'D',
       'A', 'Win %', 'Pick %', 'Avg. Score', 'First Blood %', 'Matches',]


# In[80]:


df = df[col_reorder]


# In[94]:


df


# In[97]:


type(df['Matches'][0])


# In[103]:


x = df['Matches'][0].replace(",",'')
x


# In[147]:


matchesxx = []
mapxx = []
for i in range(df.shape[0]):
    x = df['Matches'][i].replace(",",'')
    y = df['Map'][i].replace("All Maps","AllMaps")
    matchesxx.append(x)
    mapxx.append(y)
matchesxx = pd.Series(matchesxx)
mapxx = pd.Series(mapxx)


# In[149]:


mapxx


# In[150]:


df = pd.concat([df, mapxx], axis = 1)


# In[151]:


df = df.drop(['Map'], axis = 1)


# In[152]:


df.columns.values


# In[153]:


col_rename = ['Name', 'Role', 'Game Type', 'Game Rank', 'KD', 'K', 'D', 'A',
       'Win %', 'Pick %', 'Avg. Score', 'First Blood %', 'Matches', 'Map']


# In[154]:


df.columns = col_rename


# In[155]:


col_reorder = ['Name', 'Role', 'Game Type', 'Map', 'Game Rank', 'KD', 'K', 'D',
       'A', 'Win %', 'Pick %', 'Avg. Score', 'First Blood %', 'Matches']


# In[156]:


df = df[col_reorder]


# In[157]:


df


# In[110]:


df.columns


# In[112]:


df = df.drop([0], axis = 1)


# In[139]:


df


# In[171]:


Rankxx = []
for i in range(df.shape[0]):
    x = str(df['Game Rank'][i]).replace(" ","_")
    Rankxx.append(x)
Rankxx = pd.Series(Rankxx)


# In[168]:


type(df['Game Rank'][5400])


# In[170]:


df


# In[172]:


df = df.drop(['Game Rank'], axis = 1)


# In[175]:


df = pd.concat([df, Rankxx], axis = 1)


# In[176]:


df.columns


# In[177]:


col_rename = ['Name',          'Role',     'Game Type',           'Map',
                  'KD',             'K',             'D',             'A',
               'Win %',        'Pick %',    'Avg. Score', 'First Blood %',
             'Matches',               'Game Rank']


# In[178]:


df.columns = col_rename


# In[179]:


col_reorder = ['Name', 'Role', 'Game Type', 'Map', 'Game Rank', 'KD', 'K', 'D',
       'A', 'Win %', 'Pick %', 'Avg. Score', 'First Blood %', 'Matches']


# In[180]:


df = df[col_reorder]


# In[181]:


df


# In[205]:


avgxx = []
for i in range(df.shape[0]):
    x = df['Avg. Score'][i].replace(",",'')
    avgxx.append(x)
avgxx = pd.Series(avgxx)


# In[207]:


df


# In[208]:


df = pd.concat([df, avgxx], axis = 1)


# In[211]:


df = df.drop(['Avg. Score'], axis = 1)
df.columns


# In[212]:


col_rename = [         'Name',          'Role',     'Game Type',           'Map',
           'Game Rank',            'KD',             'K',             'D',
                   'A',         'Win %',        'Pick %', 'First Blood %',
             'Matches',               'Avg. Score']


# In[213]:


df.columns = col_rename


# In[218]:


col_reorder = [         'Name',          'Role',     'Game Type',           'Map',
           'Game Rank',            'KD',             'K',             'D',
                   'A',         'Win %',        'Pick %', 
             'Avg. Score', 'First Blood %', 'Matches']


# In[219]:


df = df[col_reorder]


# In[220]:


df


# In[221]:


agent_stats = df.copy()


# In[115]:


import pymysql


# In[116]:


conn = pymysql.connect(database = 'Valorant_V1', user = 'root', password = '365Pass')


# In[117]:


cursor = conn.cursor()


# In[118]:


cursor.execute("select * from agent_stats;")


# # Query Creation

# In[158]:


df.columns.values


# In[120]:


df.columns


# In[121]:


df_columns = ['Name', 'Role', 'Game Type', 'Map', 'Game Rank', 'KD', 'K', 'D', 'A',
       'Win %', 'Pick %', 'Avg. Score', 'First Blood %', 'Matches']


# In[222]:


insert_part_of_query = 'Insert into agent_stats (Agent_Name, Agent_Role, Game_Type, Map, Game_Rank, KD, K, D, A, Win_Percent, Pick_Percent, Avg_Score, First_Blood_Percent, Matches) values '
for i in range(df.shape[0]):
    main_query = "("
    for j in df_columns:
        main_query = main_query + '\'' + str(df[j][i]) + '\',' 
    main_query = main_query[:-1]
    main_query = main_query + "), "
    insert_part_of_query = insert_part_of_query + main_query
insert_part_of_query = insert_part_of_query[:-2]
insert_part_of_query = insert_part_of_query + ";"


# In[223]:


insert_part_of_query


# In[224]:


cursor.execute(insert_part_of_query)


# In[204]:


df


# In[226]:


cursor.execute("select Agent_Name from agent_stats;")


# In[227]:


conn.commit()


# In[ ]:




