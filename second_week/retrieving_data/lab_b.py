# Imports
import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd


path  = 'data/baseball.db'

con = sq3.Connection(path)

# query = 'select * from allstarfull'

# observations = pds.read_sql(query, con)
# print(observations[:10])



# Optional part 
# Pretend that you were interesting in creating a new baseball hall of fame. Join and analyze the tables to evaluate the top 3 all time best baseball players
best_query = """
SELECT playerID, sum(GP) AS num_games_played, AVG(startingPos) AS avg_starting_position
    FROM allstarfull
    GROUP BY playerID
    ORDER BY num_games_played DESC, avg_starting_position ASC
    LIMIT 3
"""
best = pd.read_sql(best_query, con)
print(best.head())


