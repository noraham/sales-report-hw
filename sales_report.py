"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []  # creates 2 empty lists we will use in the loop
melons_sold = []

f = open("sales-report.txt")  # opens the input file
for line in f:  # iterates through each line of sales-report.txt
    line = line.rstrip()  # strip whitespace (/n character) from end of line
    entries = line.split("|")  # converts line to list of strings, separator is |
    salesperson = entries[0]  # grabs first string in list and saves as variable
    melons = int(entries[2])  # grabs this string from the list and saves as variable 

# adds these variables to the 2 lists we initialized earlier
    if salesperson in salespeople:  # checks if they're already in the list
        position = salespeople.index(salesperson)  # gathers index of this person in the salespeople list
        melons_sold[position] += melons  # uses the index gathered above to edit the melon value in the melon list
    else:  # if they're not in the list yet
        salespeople.append(salesperson)  # add this person to people list
        melons_sold.append(melons)  # add their melons sold to melon list


for i in range(len(salespeople)):  # iterate through the indices of salespeople list
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])  # print values from each list at same index
    # if the parallel lists were successfully set up, it should correctly match person name with total melons sold

# ideas for improvement:
# - convert sales-report.txt to dictionary
# close the input file (or convert to sys.argv[1])
# stop with the parallel lists
# track/print entries[1]
# convert these loops into a function