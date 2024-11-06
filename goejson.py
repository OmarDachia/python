import csv
import json

# Path to your CSV file
csv_file_path = 'C:\\Users\\PC\\Downloads\\Spreadsheet.csv'
geojson_file_path = 'C:\\Users\\PC\\Downloads\\geojson.geojson'

# Initialize the GeoJSON structure
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Read the CSV file and populate the GeoJSON structure
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    # Read the first line to check the headers
    reader = csv.DictReader(csvfile)
    
    # Print the headers as recognized by Python
    print("CSV Headers:", reader.fieldnames)
    
    # Iterate through each row in the CSV file
    for row in reader:
        try:
            # Attempt to read fields from each row
            meter_no = row['\ufeffmeter_no']
            feeder_name = row['feeder_name']
            substation = row['substation']
            feeder_type = row['feeder_type']
            longitude = row['longitude']
            latitude = row['Latitude']
            
            # Only add valid points with longitude and latitude
            if longitude and latitude:
                feature = {
                    "type": "Feature",
                    "properties": {
                        "meter_no": meter_no,
                        "feeder_name": feeder_name,
                        "substation": substation,
                        "feeder_type": feeder_type
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [float(longitude), float(latitude)]
                    }
                }
                geojson["features"].append(feature)
        except KeyError as e:
            print(f"KeyError: {e} - Check your CSV headers and data format.")
        except ValueError:
            print(f"ValueError: Invalid data for coordinates at meter_no {row.get('meter_no')}")
        
# Output the resulting GeoJSON to a file
with open("output.geojson", "w", encoding='utf-8') as geojsonfile:
    json.dump(geojson, geojsonfile, indent=4)

print("GeoJSON generated successfully.")
