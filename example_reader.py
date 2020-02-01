import csv

with open('Ipp.csv', 'r') as csvfile:
    Prices = csv.reader(csvfile, delimiter=',', quotechar='"')
    for Ipp_list in Prices:
        print(', '.join(Ipp_list))
