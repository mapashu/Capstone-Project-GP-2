import pandas as pd

centers=pd.read_csv("distribution_centers.csv")
events=pd.read_csv("events.csv")
inventory_items=pd.read_csv("inventory_items.csv")
order_items=pd.read_csv("order_items.csv")
orders=pd.read_csv("orders.csv")
products=pd.read_csv("products.csv")
users=pd.read_csv("users.csv")

print(events.shape[0])
print(events["user_id"].unique().shape[0])