from flask import Flask, redirect, url_for, request
import csv
import json

app = Flask(__name__)
csv_file = 'sample_data.csv'

data = []
#read csv file
with open(csv_file, encoding='utf-8-sig')as csvf: 
    #load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf) 
    for row in csvReader: 
        data.append(row)

@app.route('/pathway/stats', methods=['GET'])
def get_pathway_status(
    age_range=None,count=None,dx_count=None,final_dx_code=None,
    final_dx_description=None,gender=None,itla_code=None,pathway_end=None,pathway_start=None,session_end_date=None):

    args = request.args.to_dict()
    result = data
    for arg in args:
        result = [a for a in result if a[arg] == args[arg]]
    return result 

if __name__ == '__main__':
    app.run(debug=True)