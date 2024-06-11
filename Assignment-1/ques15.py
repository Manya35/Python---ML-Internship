# Write a program that reads data from a CSV file and prints it to the console.

import csv

filename = "D:\Python & ML Internship\Assignment-1\sample.csv"

with open(filename, mode = 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)