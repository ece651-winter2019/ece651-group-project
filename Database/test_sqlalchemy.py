#!/usr/bin/env python
# coding: utf-8

# make sure to install MySQL Connector/Python from the following website: https://dev.mysql.com/doc/connector-python/en/

# Metadata and Table are needed for the reflection. Reflection is the the process of reading database and building SQLalchemy table objects.
# 
# Create_engine provides the common interface to connect to the database

# In[65]:


from sqlalchemy import create_engine, MetaData, Table, select


# dialect+driver://username:password@host:port/database
# The dialect refers to the name of the database like mysql, postgresql, mssql, oracle and so on. The driver refers to the DBAPI you are using. The driver is optional, if not specified a default driver will be used (assuming it is already installed). The username and password are the credentials to login to the database server. The host is the location of the database server. The port refers to the optional database port and database is the name of the database you want to connect to. reference: https://overiq.com/sqlalchemy-101/installing-sqlalchemy-and-connecting-to-database/

# In[66]:


engine = create_engine('mysql+mysqldb://root:yourpassword@localhost/ece651')


# In[75]:


connection = engine.connect()
print(engine)


# In[76]:


print(engine.table_names())


# Now we need to read database and build SQLalchemy table objects.

# MetaData object is a catalog that stores database information such as tables. So to reflect the table we initalize a metadata object.
# Then we use SQLAlchemy Table object to provide the table name. We supply our metadata instance, and then instruct it to autoload the table using the engine 

# In[77]:


metadata = MetaData()


# In[78]:


patient = Table('Patient', metadata, autoload = True, autoload_with=engine)


# In[79]:


print(repr(patient))


# In[80]:


retrieve_stmt = select([patient])
print(retrieve_stmt)


# In[81]:


results = connection.execute(retrieve_stmt).fetchall() 


# In[83]:


print(connection.execute(retrieve_stmt).fetchall())


# In[ ]:





# In[ ]:




