#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bigml')


# In[14]:


from bigml.api import BigML


# In[15]:


api = BigML('SIGRID1992', 'f0908db801439c9b805feb6d020bdbf51aafa706')


# In[16]:


mi_source = api.create_source('https://cleverdata.io/csv/diabetes.csv')


# In[17]:


api.ok(mi_source)


# In[19]:


mi_dataset = api.create_dataset(mi_source)
api.ok(mi_dataset)


# In[23]:


train_dataset = api.create_dataset(

           mi_dataset, {"name": "Dataset Name | Training 80%",

           "sample_rate": 0.8, "seed": "my seed"})











test_dataset = api.create_dataset(

           mi_dataset, {"name": "Dataset Name | Test",

           "sample_rate": 0.8, "seed": "my seed",

           "out_of_bag": True})


# mi_modelo = api.create_model(train_dataset)

# In[24]:


mi_modelo = api.create_model(train_dataset)


# In[32]:


evaluation = api.create_evaluation(mi_modelo, mi_dataset)


# In[33]:


mi_evaluacion = api.create_evaluation(mi_modelo, test_dataset)


# In[34]:


prediction = api.create_prediction(mi_modelo, {'pregnancies':4, 'insulin':4 })


# In[35]:


api.pprint(prediction)


# In[ ]:




