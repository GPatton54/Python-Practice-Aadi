import datetime
import csv
from typing import List

with open("C:\covid_impact_on_airport_traffic_date_formatted.csv") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    totalflights = 0
    for line in csv_reader:
        a = line[2]
        b = int(line[4])
        okay = datetime.datetime.strptime(a, "%Y-%m-%d")
        if okay.month == "03":
            totalflights = totalflights + b
        else:
            continue
print(totalflights)
