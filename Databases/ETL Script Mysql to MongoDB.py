import mysql.connector as sql
import pymongo
from pymongo import MongoClient
import pandas as pd

#EXTRACT FROM MYSQL
db_connection = sql.connect(host='localhost', database='test', user='root', password='test')
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM users')
table_rows = db_cursor.fetchall()
df = pd.DataFrame(table_rows, columns = ["ID", "Name", "Department", "Location", "Pay"])
df['Pay'] = df['Pay'].astype(int)
#print(df)

#TRANSFORM DATA INTO AVERAGE PAY PER DEPARTMENT
tdf = df.groupby('Department')['Pay'].mean().reset_index(name ='Average Pay')
print(tdf)

#Connect to MONGODB
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/Test')
#select database
db = client['Test']
#select the collection within the database
testcollection = db.testcollection
#convert entire collection to Pandas dataframe

#LOAD DATA, two sets, one is original datavalues, other is transformed values
testcollection.insert_many(df.to_dict('records'))
testcollection.insert_many(tdf.to_dict('records'))