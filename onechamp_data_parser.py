import csv
import json

# Open the CSV
f = open( "data.csv", 'rU' )
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader( f, fieldnames = ( "Person Id","Floor Access DateTime","Floor Level","Building"))
next(reader)

# Parse the CSV into JSON
out = json.dumps( [ row for row in reader ],indent=2, sort_keys=False )
print("JSON parsed!")

# Save the JSON
f = open( 'parsed_data.json', 'w')
f.write(out)
print("Data Parsed and JSON File Created")