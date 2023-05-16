

import pandas as ps 

file_path = 'data/file.json'

csv_file = 'data/file.csv'

# read json file 
data = ps.read_json(file_path)



# read csv data
csv_data = ps.read_csv(csv_file)
# convert data into json file 
# csv_data.to_json('data/new.json')

print(data)