#!/usr/bin/python3
"""
This is the ``task_02_csv`` module
"""
import csv
import json 


def convert_csv_to_json(csvFile):
    """
    This function convert csv file to json file
    """
    data = {}
    try:
        with open(csvFile) as file:
            csvReader = csv.DictReader(file)
            for rows in csvReader:
                key = rows['name']
                data[key] = rows
        with open('data.json', "w") as dataf:
            json.dump(data, dataf, indent=4)
        return True
    except Exception:
        return False
