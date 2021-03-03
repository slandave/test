import csv
filename = input()
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    result = dict()
    for i in reader:
        for x in i:
            if x in result:
                result[x] = result[x] + 1
            else:
                result[x] = 1
    for a in list(result.keys()):
        print("{} {}".format(a, result[a]))