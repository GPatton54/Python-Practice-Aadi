import csv

with open("C:\AH_Excess_Deaths_by_Sex__Age__and_Race.csv") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    male = []
    female = []
    for line in csv_reader:
        if str(line[6]) == "Male (M)":
            male.append(int(line[11]))
        elif str(line[6]) == "Female (F)":
            female.append(int(line[11]))
    print(sum(male))
    print(sum(female))