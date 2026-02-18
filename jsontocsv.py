import json
import csv
import sys

def json_to_csv(json_file, csv_file):
    """
    Convert JSON file to CSV file.
    Assumes JSON is an array of objects.
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print("Error: JSON file must contain an array of objects")
            return
        
        if not data:
            print("Error: JSON array is empty")
            return
        
        # Get fieldnames from the first object
        fieldnames = list(data[0].keys())
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Successfully converted {json_file} to {csv_file}")
    
    except FileNotFoundError:
        print(f"Error: File {json_file} not found")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {json_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    json_file = 'sample.json'
    csv_file = 'sample.csv'
    json_to_csv(json_file, csv_file)
