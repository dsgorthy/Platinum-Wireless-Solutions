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
		transactions[row[9]] = row[0:8]

	return transactions


def build_model_list(raw_dict):
	model_list = []

	for ItemID in raw_dict:
		if (raw_dict[ItemID][0] not in model_list):
			model_list.append(raw_dict[ItemID][0])

	return model_list


# Key: ItemID
# Value: [Device Model, Category, Purchase Date, Purchase Price, Sale Date, Sale Price, Shipping Fees, eBay Fees, Net Profit]
#
processed_transactions = read_file_into_dict()
model_list = []


ans = True
while ans:
	display_menu()
	ans=input("What would you like to do? ")

	if (ans == "1"):
		model_list = build_model_list(processed_transactions)
		print(model_list)

	elif (ans == "9"):
		print ("Goodbye!")
		ans = None

	else:
		print ("Invalid input, try again.")
		ans = True