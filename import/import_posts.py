import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('Instagram_Posts.csv')

client = MongoClient('mongodb://localhost:27017/')
db     = client['mongoproject']
collection = db['posts']

data = df.to_dict(orient='records')

collection.insert_many(data)
