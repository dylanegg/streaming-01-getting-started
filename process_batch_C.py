"""
Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.

"""

import csv

#Name Files
input_file_name = "batchfile_2_kelvin.csv"
output_file_name = "batchfile_3_farenheit.csv"

#Open both Files
input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w", newline='')

#create reader for input file and writer for output file
reader = csv.reader(input_file, delimiter=",")
writer = csv.writer(output_file, delimiter=",")

#Considr header row and write header row to output file
header = next(reader)
header_list = ["Year","Month","Day","Time","TempF"]
writer.writerow(header_list)

# Convert Kelvin Temp to Fahrenheit Temp
# Kelvin to Fahrenheit conversion sourced from https://www.thoughtco.com/convert-kelvin-to-fahrenheit-609234
for row in reader:
    Year, Month, Day, Time, TempK = row
    TempF = round(1.8*(float(TempK)-273) + 32, 2)
    writer.writerow([Year, Month, Day, Time, TempF])

#close files
output_file.close()
input_file.close()

