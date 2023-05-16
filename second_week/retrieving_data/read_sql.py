## example of reading from sql database 

import sqlite3 as sq3
import pandas as ps 


path = "data/classic_rock.db"


# create a connection 
con = sq3.Connection(path)


# write a query 
# query = 'select * from rock_songs' 

# # Execute a query 
# data = ps.read_sql(query, con)
 
query = '''SELECT Artist, Release_Year, COUNT(*) AS num_songs, AVG(PlayCount) AS avg_plays  
    FROM rock_songs
    GROUP BY Artist, Release_Year
    ORDER BY num_songs desc'''
 


observations_generator = ps.read_sql(query,con,coerce_float=True,parse_dates=['Release_Year'],chunksize=5)


for index, observations in enumerate(observations_generator):
    
    if index < 5:
        print(f'Observations index: {index}'.format(index))
        print(observations)
        
        
