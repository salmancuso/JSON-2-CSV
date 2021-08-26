# Data Flattening JSON to CSV

## About the Project
The project, albeit simple in concept, takes a few JSON files and flatten them into CSV.  The curveball came when several items within the JSON files were nested arrays, which means I must reshape the files into their own results files.

## About the Data
The data is comprised of several JSON files that were riddled with nested arrays. Unfortunately, nested arrays in JSON are rather cumbersome to flatten into CSV files, and I had to deploy a few techniques to flatten the files. For example, if a JSON file contained nested arrays, I used the unique ID to create a separate file with only the ID and the array data that became resembled more of a time series dataset. 


## Platform & Libraries
* Python3
* JSON
* csv
* tqdm
* re

## Contact
This code developed by Sal Mancuso, Senior Data Engineer at Stanford University, is used by Sanford Faculty, Students, Staff, and Affiliates. 
- Creator: Sal Mancuso