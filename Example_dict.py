import csv

Prices = []
with open('Ipp.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for Ipp_dic in reader:
        Prices.append(Ipp_dic)
        print(Prices)