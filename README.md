Wrote this scrip to convert a large JSOn files to CSV so that data can be analysed. Here the entry values are hard coded. But this can be used a reference. 

Usage: python script.py <input_json_file> <output_csv_file>

It will read the json file and writes selected data into a CSV file with the following columns:
host
name
proxy (specifically proxy['name'])
templates (a newline-separated list of template['name'] values)

# JSON-file-conversion-to-CSV
This script will convert json files to CSV
