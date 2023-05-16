import pandas as ps 

# file with commas
file_path = 'data/file.csv'
#file with delimit whitespaces
file2_path = 'data/file2.csv'

# data = ps.read_csv(file_path)
# data = ps.read_csv(file2_path, delim_whitespace=True)


# count the first row
# data = ps.read_csv(file_path, header=None)

# name the columns
# data = ps.read_csv(file_path, names=['first', 'second', 'third'])


# read na_values as null values 
# data = ps.read_csv(file_path, na_values=[20,'mohamed'])


data = ps.read_csv(file_path)
print(data)


