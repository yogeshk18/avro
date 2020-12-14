#AVRO - CSV FILE CONVERSION USING PYTHON:


#import required modules
from fastavro import reader
import csv
# coding part
head = True
fo = csv.writer(open("test.csv", "w+"))
with open('abc.avro', 'rb') as fi:
    avro_reader = reader(fi)
    for data in avro_reader:
        if head == True:
            header = data.keys()
            fo.writerow(header)
            head = False
        fo.writerow(data.values())
