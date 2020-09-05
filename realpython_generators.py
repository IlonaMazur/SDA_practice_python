import csv

def csv_read():
    techcrunch = []

    file_name = "techcrunch.csv"
    lines = (line for line in open(file_name))