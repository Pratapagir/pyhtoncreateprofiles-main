import csv
import json

csv_file = 'profiles1.csv'
json_file = 'data.json'

data = []

#Read the CSV file
with open(csv_file, 'r', encoding='utf-8-sig') as file:  # Specify encoding
    csv_data = csv.DictReader(file)
    for row in csv_data:
        data.append(row)

#Write the JSON file
with open(json_file, 'w', encoding='utf-8') as file:  # Specify encoding
    json.dump(data, file, indent=4, ensure_ascii=False)  # Ensure ASCII is False

print("CSV to JSON conversion completed!")