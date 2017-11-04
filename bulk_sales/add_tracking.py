# Takes two csv files
# 
# tracking_file (csv): needs blank row with title "Tracking" number and filled row "Buyer Name"
# tracking_info (csv): exported from Stamps.com

import csv
import os

tf = os.listdir('tracking_info')
of = os.listdir('order_info')

if (len(tf) != 1):
	print("Too many or not enough files in the tracking_info directory, exiting.")
	exit()
if (len(of) != 1):
	print("Too many or not enough files in the order_info directory, exiting.")
	exit()

tf_reader = csv.reader(open('tracking_info/'+tf[0]), delimiter=",")
tracking_dict = {}

for line in tf_reader:
	tracking_num = line[5][2:-1]
	if (len(tracking_num) == 22):
		tracking_dict[line[3]] = tracking_num

output_arr = []
of_reader = csv.reader(open('order_info/'+of[0]), delimiter=",")

count = 0
first_line = True
for line in of_reader:
	if (first_line):
		ol = line
		first_line = False
	else:
		ol = line
		for tracking in tracking_dict.keys():
			if (line[22] in tracking):
				count += 1
				ol[1] = 'USPS First Class'
				ol[2] = tracking_dict[tracking]
	output_arr.append(ol)

with open("output.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerows(output_arr)