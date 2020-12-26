import csv
from typing import List

with open("C:\covid_impact_on_airport_traffic.csv") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    lst = []

    for line in csv_reader:
        lst.append(line[3])
        leest = []

        leest = set(lst)

        for x in leest:
            leest.add(x)
print(leest)