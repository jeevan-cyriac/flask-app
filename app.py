from flask import Flask, redirect, url_for, request, render_template_string
import csv
import json

app = Flask(__name__)
csv_file = 'sample_data.csv'

## READ CSV and load the data 
data = []
with open(csv_file, encoding='utf-8-sig')as csvf: 
    csvReader = csv.DictReader(csvf) 
    for row in csvReader: 
        data.append(row)

"""
GET endpoint for /pathway/stats
The API endpoint accepts any of the column name as a query parameter.

- When query parameters are passed, the app will look for exact match based on the query parameters and returns the filtered data.
- When no query parameters are passed, the whole dataset is returned
"""
@app.route('/pathway/stats', methods=['GET'])
def get_pathway_status(
    age_range=None,count=None,dx_count=None,final_dx_code=None,
    final_dx_description=None,gender=None,itla_code=None,pathway_end=None,pathway_start=None,session_end_date=None):

    args = request.args.to_dict()
    result = data
    for arg in args:
        result = [a for a in result if a[arg] == args[arg]]
    
    return result 
    # return render_output(result)

"""
render_output will return a HTML table to output the data. This is useful to debuf the API endpoint response body.
"""
def render_output(result):
    return render_template_string('''
        <table>
                <tr>
                    <td> session_end_date </td> 
                    <td> age_range </td>
                    <td> itla_code </td>
                    <td> gender </td>
                    <td> pathway_start </td>
                    <td> pathway_end </td>
                    <td> dx_count </td>
                    <td> dx_count </td>
                    <td> final_dx_code </td>
                    <td> final_dx_description </td>
                    <td> count </td>
                </tr>
        {% for i in result %}
                <tr>
                    <td>{{ i.session_end_date }}</td> 
                    <td>{{ i.age_range }}</td>
                    <td>{{ i.itla_code }}</td>
                    <td>{{ i.gender }}</td>
                    <td>{{ i.pathway_start }}</td>
                    <td>{{ i.pathway_end }}</td>
                    <td>{{ i.dx_count }}</td>
                    <td>{{ i.dx_count }}</td>
                    <td>{{ i.final_dx_code }}</td>
                    <td>{{ i.final_dx_description }}</td>
                    <td>{{ i.count }}</td>
                </tr>
        {% endfor %}
        </table>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)