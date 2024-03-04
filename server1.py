from flask import Flask,render_template,request
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

def write_to_csv(data):
    with open('Database.csv', mode='a', newline ='') as database3:
      name = data['name']
      email = data['email']
      subject = data['subject']
      message = data['message']

      csv_writer= csv.writer(database3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
      csv_writer.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'submitted successfully'
    else:
        return 'sorry somthing went wrong'
