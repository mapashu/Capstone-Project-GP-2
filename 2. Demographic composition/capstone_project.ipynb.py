import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as w

w.filterwarnings("ignore")

### USER'S DATAFRAME ###
df1 = pd.read_csv("./datasets/users/not_china_users.csv")
df2 = pd.read_csv("./datasets/users/china_users.csv")

users = pd.concat([df1, df2])
#print(users.head(3))

### PRODUCTS-USER'S DATAFRAME ###

df1 = pd.read_csv("./datasets/products/user_order_item_prd-1--24999.csv")
df2 = pd.read_csv("./datasets/products/user_order_item_prd-25000--49999.csv")
df3 = pd.read_csv("./datasets/products/user_order_item_prd-50000--74999.csv")
df4 = pd.read_csv("./datasets/products/user_order_item_prd-75000--100000.csv")

products_users = pd.concat([df1, df2, df3, df4])
#print(products_users.head(3))

### ORDERS-USER'S DATAFRAME ###

df1 = pd.read_csv("./datasets/orders/orders_1--74999.csv")
df2 = pd.read_csv("./datasets/orders/orders_75000+.csv")

orders_users = pd.concat([df1, df2])
#print(orders_users.head(3))

### EVENTS-USER'S DATAFRAME ###

df1 = pd.read_csv("./datasets/events/events_1--4999.csv")
df2 = pd.read_csv("./datasets/events/events_5000--9999.csv")
df3 = pd.read_csv("./datasets/events/events_10000--14999.csv")
df4 = pd.read_csv("./datasets/events/events_15000--19999.csv")
df5 = pd.read_csv("./datasets/events/events_20000--24999.csv")
df6 = pd.read_csv("./datasets/events/events_25000--29999.csv")
df7 = pd.read_csv("./datasets/events/events_30000--34999.csv")
df8 = pd.read_csv("./datasets/events/events_35000--39999.csv")
df9 = pd.read_csv("./datasets/events/events_40000--44999.csv")
df10 = pd.read_csv("./datasets/events/events_45000--49999.csv")
df11 = pd.read_csv("./datasets/events/events_50000--54999.csv")
df12 = pd.read_csv("./datasets/events/events_55000--59999.csv")
df13 = pd.read_csv("./datasets/events/events_60000--64999.csv")
df14 = pd.read_csv("./datasets/events/events_65000--69999.csv")
df15 = pd.read_csv("./datasets/events/events_70000--74999.csv")
df16 = pd.read_csv("./datasets/events/events_75000--79999.csv")
df17 = pd.read_csv("./datasets/events/events_80000--84999.csv")
df18 = pd.read_csv("./datasets/events/events_85000--89999.csv")
df19 = pd.read_csv("./datasets/events/events_90000--94999.csv")
df20 = pd.read_csv("./datasets/events/events_95000--100000.csv")

events = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20])

### EVENTS-USER'S DATAFRAME ###

df1 = pd.read_csv("./datasets/events/events_user-null_1298099--1418098.csv")
df2 = pd.read_csv("./datasets/events/events_user-null_1418099--1538098.csv")
df3 = pd.read_csv("./datasets/events/events_user-null_1538099--1658098.csv")
df4 = pd.read_csv("./datasets/events/events_user-null_1658099--1778098.csv")
df5 = pd.read_csv("./datasets/events/events_user-null_1778099--1898098.csv")
df6 = pd.read_csv("./datasets/events/events_user-null_1898099--2018098.csv")
df7 = pd.read_csv("./datasets/events/events_user-null_2018099--2138098.csv")
df8 = pd.read_csv("./datasets/events/events_user-null_2138099--2258098.csv")
df9 = pd.read_csv("./datasets/events/events_user-null_2258099--2378098.csv")
df10 = pd.read_csv("./datasets/events/events_user-null_2378099--2498098.csv")

events_null_users = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10])

conditions = [users["age"]<20, ((users["age"]>=20) & (users["age"]<=29)) , ((users["age"]>29) & (users["age"]<=39)), ((users["age"]>39) & (users["age"]<=49)) , ((users["age"]>49) & (users["age"]<=59)), users["age"]>59 ]
age_group = ["1-Teens", "2-Twenties", "3-Thirties", "4-Forties", "5-Fifties", "6-Elders"]

users["age_group"] = np.select(conditions, age_group)
users["created_at"] = pd.to_datetime(users["created_at"])
users["created_at"] = pd.to_datetime(users["created_at"].dt.strftime('%m/%d/%Y'))
users["costumer_time"] = ((pd.to_datetime('today').normalize()- users["created_at"])/(24*3600*1000000000)).astype('int64')

#print(users)

# 1. What is the distribution of age and gender among our customer base?
age_groups_count = users[["age_group","gender","user_id"]].groupby(["age_group","gender"]).count().sort_values(["age_group"], ascending=True)
age_groups_count["user_id"] = age_groups_count["user_id"]/1000

# IN GENERAL THE DISTRIBUTION AMONG AGE GROUPS AND GENDERS IS SIMILAR, HAVING A STRICLY BIGGER AMOUNT FOR PEOPLE ABOVE 60YO

#print(age_groups_count)

age_countries_count = users[["age_group","country","user_id"]].groupby(["country","age_group"], as_index=False).count().sort_values(["country","age_group"], ascending=True)
age_countries_count["user_id"] = age_countries_count["user_id"]/1000

#print(age_countries_count)

# LIKE IT HAPPENED IN GENERAL TERMS, IF WE DIVIDE THE DATASET BY COUNTRY THE DISTRIBUTION IS SIMILAR IF WE TALK ABOUT AGE GROUP

gender_countries_count = users[["country","gender","user_id"]].groupby(["country","gender"], as_index=False).count().sort_values(["country","gender"], ascending=True)
gender_countries_count["user_id"] = gender_countries_count["user_id"]/1000

print(gender_countries_count)

# LIKE IT HAPPENED IN GENERAL TERMS, IF WE DIVIDE THE DATASET BY COUNTRY THE DISTRIBUTION IS SIMILAR IF WE TALK ABOUT GENDERS

countries_count = users[["country","user_id"]].groupby(["country"]).count().sort_values(["user_id"], ascending=False)
countries_count["user_id"] = countries_count["user_id"]/1000

#print(countries_count)

# Study the 3 main countries
americans=users[users.country=="United States"]
chineses=users[users.country=="China"]
brazilians=users[users.country=="Brasil"]

age_groups_us_count = americans[["age_group","gender","user_id"]].groupby(["age_group","gender"], as_index=False).count().sort_values(["age_group"], ascending=True)
age_groups_us_count["user_id"] = age_groups_us_count["user_id"]/americans["user_id"].count()*100

print(age_groups_us_count)

female = age_groups_us_count[age_groups_us_count["gender"]=="F"]["user_id"]
male = age_groups_us_count[age_groups_us_count["gender"]=="M"]["user_id"]
index = age_groups_us_count["age_group"]

plt.figure(1)
sns.barplot(age_groups_us_count, x="age_group", y="user_id", hue="gender")



# Are there significant age or gender preferences for certain products or services?
# Which countries or cities have the highest concentration of our customer demographic?
# Are there location-based variations in customer behavior?
# Can we identify specific customer segments that exhibit strong loyalty through multiple purchases?
# What factors contribute to customer loyalty, and how can we leverage this information?
