#
# Author: Derek Gorthy
# Date: 4/17/2017
# Description: General analysis script for preprocessed data.
#			   This script will be replaced with a database, using for preliminary results.
#
# Notes: Run with Python3 
#

import csv
import os
import sys

PROCESSED_DATA = "../data_output/raw.csv"


def display_menu():
	print("1. Display list of all devices")
	print("9. Exit/Quit")
	return


def read_file_into_dict():
	transactions = {}

	f = open(PROCESSED_DATA)
	csv_f = csv.reader(f)

	for row in csv_f:
		print (row[9])

	return transactions


processed_transactions = {}



ans = True
while ans:
	display_menu()
	ans=input("What would you like to do? ")

	if (ans == "1"):
		read_file_into_dict()

	elif (ans == "9"):
		print ("Goodbye!")
		ans = None

	else:
		print ("Invalid input, try again.")
		ans = True