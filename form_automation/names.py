import csv

# Open the CSV file
with open('names.csv', newline='') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    form_data = []
    
    for row in reader:
        name = row[0]
        email = row[1]
        form_data.append([name, email])

