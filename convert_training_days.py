import csv
import json
from datetime import datetime

# Define the header names so we can specify them when reading the CSV
fieldnames = (
    "Date","DayoftheWeek","Activity","DaysTrained"

)

# Open both files so we can interact with them
# Using the `with` keyword lets us close the files automatically after these
# with blocks end and we're done writing and reading the files

with open('./days.csv', 'r') as csvfile:
    with open('./days.json', 'w') as jsonfile:
            # `next` will simply skip over the header row in the csvfile
        next(csvfile)
            # We use the csv library to create a 'reader' of the file
            # This reader parses through the csvfile and the headers
            # and allows us to interact with it as a Python object
        reader = csv.DictReader(csvfile, fieldnames)
            # This creates an empty dictionary to hold the final set of
            # data that we'll eventually dump into the JSON file
        final_data = {}
            # Now we use the reader to iterate over all the rows of the CSV
            # (except for the header) and then keep the values we want
        final = []
        for row in reader:
                # We also restructure the data so that it exists as
                # a set of date keys with the value as a dictionary of
                # different data elements from the CSV.
                # "Date","Open","High","Low","Close","Volume","Adj Close"
            final_data = {
                    "Date": row["Date"],
                    "DayWeek": row["DayoftheWeek"],
                    "Activity": row["Activity"],
                    "DaysTrained": row["DaysTrained"]
                }
            final.append(final_data)
        sorted_date = sorted(final, key=lambda x: datetime.strptime(x['Date'], '%m-%d-%Y'))

        fin = sorted_date
            # Finally, we use the json library to output the final_data
            # dictionary to the jsonfile we opened earlier
        json.dump(fin, jsonfile)
            # And then we write a final newline to the end of the file
            # (this is just a best practice)
        jsonfile.write('\n')
