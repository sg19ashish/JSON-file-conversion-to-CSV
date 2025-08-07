import json
import csv
import sys

def json_to_csv(json_file, csv_file):
    # Read the JSON data from the file
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    
    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['host', 'name', 'proxy', 'templates'])
        
        # Write the data rows
        for entry in json_data:
            host = entry['host']
            name = entry['name']
            proxy = entry['proxy']['name']
            templates = "\n".join([template['name'] for template in entry['templates']])
            
            writer.writerow([host, name, proxy, templates])

    print(f"Data has been written to {csv_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_json_file> <output_csv_file>")
        sys.exit(1)
    
    input_json_file = sys.argv[1]
    output_csv_file = sys.argv[2]
    
    json_to_csv(input_json_file, output_csv_file)
