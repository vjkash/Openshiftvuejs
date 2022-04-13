#use this script to load some data into the database for testing
#make sure the stack is running (docker-compose up) before running this script
#the data is pulled from the csv and then sent to the database via the Django REST API
import csv
import requests


#baseball stat data
with open('2021_bball_stat.csv', mode='r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        
        
        print(f'\t{row["player_name"]} hit {row["home_runs"]} home runs in 2021.  Loading data....')
        response = requests.post('http://restapi:8000/api/bball-stats/', data = row)
        print(response)
        line_count += 1
    print(f'Processed {line_count} lines.')