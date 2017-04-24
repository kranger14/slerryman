
# coding: utf-8

# In[2]:

f = open("births.csv", 'r')
text = f.read()
new_line = text.split("\n")
new_line


# In[4]:

for n in new_line:
    record = n.split(",")
    print (record)


# In[8]:

days_counts = {}
for n in new_line:
    record = n.split(",")
    day_of_week = record[3]
    births = record[4]
    if day_of_week in days_counts:
        days_counts[day_of_week] += births
    else:
        days_counts[day_of_week] = births
        
print (days_counts)


# ##Aggregating birth data
# 
# We have found the total number of births by day of the week from the data from the set.

# In[ ]:



