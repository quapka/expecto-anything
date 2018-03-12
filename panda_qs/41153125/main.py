# very usefull Python module for working with table-like file formats
import pandas as pd

def split_address(address):
	# helper function which accepts address string
	# "123 Any Street, New York, NY 00010"
	# and returns the list of separated values
	# ['123 Any Street', 'New York', 'NY', '00010']
	values = address.split(',')
	# pop the last value and after splitting extend the original list
	values.extend(values.pop().split())
	# return the values but strip them from white chars first
	return (x.strip() for x in values)

def add_address_cols(df):
	# this function accepts a pd.Dataframe and 
	# creates new_cols from the col Address.
	new_cols = ['Street', 'City', 'State', 'Zipcode']
	# here is the magic, using apply to process the dataframe
	# row by row, calling the helper function on each row's Address
	# value, returning pd.Series from lambda so we can add more columns
	# to the dataframe at once.
	df[new_cols] = df.apply(lambda row: pd.Series(
		split_address(row['Address'])), axis=1)
	# delete the Address col, since we no longer need it
	df.drop('Address', inplace=True, axis=1)
	# set the correct order of the columns in the df
	correct_col_order = ['Name'] + new_cols + ['Phonenumber', 'ID']
	# return the newly created df with the columns in the right order
	return df[correct_col_order]


if __name__ == '__main__':

	# load the data with pandas
	df = pd.read_csv('data', header=0)
	# call the function
	df = add_address_cols(df)
	# print the results
	print(df)