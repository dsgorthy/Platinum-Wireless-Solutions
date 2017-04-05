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


def file_exists(input_file):
	if not (os.path.isfile(input_file)):
		print (" ")
		print ("ERROR: Input file:", input_file) 
		print ("not found in the raw_data directory.")
		return 0
	return 1


def display_menu():
	print("1. Remove a column")
	print("2. Remove a items of certain category")
	print("9. Exit/Quit")
	return


def add_line_to_file(line,output_file_name):
	with open(output_file_name, "a") as f:
		f.write(line)
	return


def parsed_row_to_string(row):
	init_str = ""

	for item in row:
		init_str = init_str + item + ","
	return init_str[:-1] + "\n"


def get_column_number(file_name, column):

	f = open(file_name)
	csv_f = csv.reader(f)
	column_number = 0
	column_int = -1

	for row in csv_f:	
		for header in row:
			if (column == header):
				column_int = column_number
			column_number += 1

	if (column_int == -1):
		print (" ")
		print ("ERROR: The column:", column)
		print ("does not exist.")

	return column_int


def remove_column(file_name, column_int, new_file_name):

	if(os.path.isfile(new_file_name)):
		os.remove(new_file_name)

	first_line = 1
	f = open(file_name)
	csv_f = csv.reader(f)

	for row in csv_f:
		del row[column_int]
		add_line_to_file(parsed_row_to_string(row), new_file_name)

	return


def remove_rows_with_element(file_name, remove_string, category_int, new_file_name):

	f = open(file_name)
	csv_f = csv.reader(f)

	for row in csv_f:
		if (row[category_int] != remove_string):
			add_line_to_file(parsed_row_to_string(row), new_file_name)	

	return



ans = True
while ans:
	display_menu()
	ans=input("What would you like to do? ")

	if (ans == "1"):
		input_file = "../raw_data/"+input("What is the name of the input file? ")
		if (file_exists(input_file)):
			column_name = input("What column would you like to remove? ")
			column_int = get_column_number(input_file, column_name)
			if (column_int != -1):
				output_file = "../data_output/"+input("What would you like the output file to be named? ")
				remove_column(input_file,column_int,output_file)	

	elif (ans == "2"):
		input_file = "../raw_data/"+input("What is the name of the input file? ")
		if (file_exists(input_file)):
			column_name = input("What column would you like to look at? ")
			column_int = get_column_number(input_file, column_name)
			if (column_int != -1):
				data_val = input("What data value do you want to remove? ")
				output_file = "../data_output/"+input("What would you like the output file to be named? ")
				remove_rows_with_element(input_file, data_val, column_int, output_file)

	elif (ans == "9"):
		print ("Goodbye!")
		ans = None

	else:
		print ("Invalid input, try again.")
		ans = True