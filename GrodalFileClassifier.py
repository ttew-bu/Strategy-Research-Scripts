# Tristan Tew 8/1/2020
# GrodalFileClassifier
# This python file searches for, breaks down, scrubs, and categorizes file titles in a CSV file. 
# In theory, it should be adaptable to different users if you change the correct values. 

import os
import csv
# import the necessary packages to write a CSV and access the hard drive

#define the path as the folder you want to read the names from 
path = "C:/Users/trist/Dropbox/Wheelchairs/Research for Professor Grodal/Primary Sources/New Mobility Articles/New Mobility Advertisements/"

#define files as the objects within the destination folder
folders = os.listdir(path)

#use a list comprehension to go through ALL folders in the directory and only parse the PDFs since those are the only docs we want 
files = [os.path.join(root, name)
    for root, dirs, files in os.walk(path)
    for name in files 
    if name.endswith((".pdf"))]

#create a blank dictionary 
objects = []

#break each name into parts based on underscores and then add each component to the name/remove .pdf from the names
for f in files:
    names = f.replace(".pdf", "")
    namestwo = names.replace('C:/Users/trist/Dropbox/Wheelchairs/Research for Professor Grodal/Primary Sources/New Mobility Articles/New Mobility Advertisements/', "")
    objects += namestwo.split('_')

#define the years as every fourth object starting w position one
years = objects[0::4]
#print(years)

#same as above with months of the year (and for producers/products as this is the defined pattern)
months = objects[1::4]

producers = objects[2::4]

products = objects[3::4]


#define the fields so you have headers for the CSV
fields = ["Year", "Producer", "Producers", "Products"]

#Use ZIP to create a new list of tuples that matches the year to month to producers to products 
rows = zip(years, months, producers, products)

#define the name of the file that you want to send this CSV data to
filename = "TEST.csv"

#Open the file
with open(filename, "w") as f:

    #store csv writer in a variable 
    writer = csv.writer(f)

    #write in the field titles on the CSV 
    writer.writerow(fields)

    #Iterating through the list, write in the row data on the CSV
    for row in rows:
        writer.writerow(row)




