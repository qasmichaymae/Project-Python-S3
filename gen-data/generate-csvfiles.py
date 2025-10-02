
import pandas as pd
import numpy as np
from faker import Faker 
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# --- 1. Users ---
num_users = 1000
users = []

for i in range(1, num_users + 1):
    users.append({
        'user_id': i,
        'name': fake.name(),
        'email': fake.email(),
        'signup_date': fake.date_between(start_date='-2y', end_date='today')
    })

df_users = pd.DataFrame(users)
df_users.to_csv('users.csv', index=False)

# --- 2. Products ---
num_products = 100
categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys', 'Sports']
products = []

for i in range(1, num_products + 1):
    products.append({
        'product_id': i,
        'name': fake.word().capitalize(),
        'category': random.choice(categories),
        'price': round(random.uniform(5, 500), 2)
    })

df_products = pd.DataFrame(products)
df_products.to_csv('products.csv', index=False)

# --- 3. Orders ---
num_orders = 5000
orders = []

for i in range(1, num_orders + 1):
    user = random.choice(df_users['user_id'])
    product = random.choice(df_products['product_id'])
    quantity = random.randint(1, 5)
    order_date = fake.date_between(start_date='-1y', end_date='today')
    
    orders.append({
        'order_id': i,
        'user_id': user,
        'product_id': product,
        'quantity': quantity,
        'order_date': order_date
    })

df_orders = pd.DataFrame(orders)
df_orders.to_csv('orders.csv', index=False)

# --- 4. Order Summary (daily aggregation) ---
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
order_summary = df_orders.groupby(['order_date']).agg(
    total_orders=('order_id', 'count'),
    total_quantity=('quantity', 'sum')
).reset_index()

df_order_summary = order_summary
df_order_summary.to_csv('order_summary.csv', index=False)

print("✅ Fichiers CSV générés : users.csv, products.csv, orders.csv, order_summary.csv")
