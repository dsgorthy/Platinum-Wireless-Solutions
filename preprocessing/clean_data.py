#
# Author: Derek Gorthy
# Date: 4/4/2017
# Description: General preprocessing script for sales and ledger files. Intended
#			   to be interactive from command line with possible entension. 
#
# Notes: Run with Python3 
#

import csv
import os
import sys


def displayMenu():
	print("""
		1. Remove a column
		9. Exit/Quit
		""")



def add_line_to_file(line,output_file_name):
	with open(output_file_name, "a") as f:
		f.write(line)
	return


def remove_column(file_name, column, new_file_name):

	if(os.path.isfile(new_file_name)):
		os.remove(new_file_name)

	first_line = 1

	f = open(file_name)
	csv_f = csv.reader(f)
	delete_column = -1

	for row in csv_f:
		if (first_line):
			first_line = 0
			column_number = 0
			
			for header in row:
				if (column == header):
					delete_column = column_number
				column_number += 1
			if (delete_column == -1):
				print ("The column header --", column , "-- does not exist! Exiting.")

		del row[delete_column]

		init_str = ""

		for item in row:
			init_str = init_str + item + ","
		init_str = init_str[:-1] + "\n"

		add_line_to_file(init_str, new_file_name)

	return



ans = True
while ans:
	displayMenu()
	ans=input("What would you like to do? ")

	if (ans == "1"):
		column = input("What column would you like to remove? ")
		input_file = "../raw_data/"+input("What is the name of the input file? ")
		output_file = "../data_output/"+input("What would you like the output file to be named? ")

		if(os.path.isfile(input_file)):
			remove_column(input_file,column,output_file)
		else:
			print (" ")
			print ("ERROR: Input file:", input_file) 
			print ("found in the raw_data directory.")	

	elif (ans == "9"):
		print ("Goodbye!")
		ans = None

	else:
		print ("Invalid input, try again.")
		ans = True