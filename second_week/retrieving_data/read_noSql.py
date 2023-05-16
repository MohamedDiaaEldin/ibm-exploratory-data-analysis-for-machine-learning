#  connecting to no sql database 

from pymongo import MongoClient 
import pandas as pd

con = MongoClient()

## will display all avaliable database 
## database_name => database name
db = con.database_name 

query = 'select * form students'

# collection_name => table name 
cursor = db.collection_name.find(query)

df = pd.DataFrame(list(cursor))



