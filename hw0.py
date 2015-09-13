import csv
count = 0
iowa = open('iowa-liquor-sample.csv')
data = csv.reader(iowa)
for row in data:
	compare = str.lower(row[11]) # induce case insensitivity
	if compare == 'single malt scotch':
		count = count + 1
print 'number of single malt scotches: ' + str(count)
