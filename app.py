from flask import Flask, render_template, request, redirect, url_for, flash
from db_connection import execute_query, execute_select_query

app = Flask(__name__)

# Set the secret key
app.secret_key = 'my_secret_key_12345'


@app.route("/")
def index():
    try:
        # Fetch employee data from the database
        query = "SELECT * FROM employee_detail"
        employees = execute_select_query(query)
        

        # Pass the data to the HTML template
        return render_template("index.html", employees=employees)

    except Exception as e:
        # Handle any exceptions, e.g., database connection errors
        flash("An error occurred: " + str(e))
        return render_template("index.html", employees=[])


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        query = "INSERT INTO employee_detail (NAME, EMAIL, CONTACT_NO) VALUES (?, ?, ?)"
        params = (name, email, phone)
        execute_query(query, params)
        flash("Employee Inserted Successfully")
        return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        query = "UPDATE employee_detail SET NAME=?, EMAIL=?, CONTACT_NO=? WHERE UID=?"
        params = (name, email, phone, id)
        execute_query(query, params)
        flash("Employee Updated Successfully")
        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods=['GET'])
def delete(id):
    query = "DELETE FROM employee_detail WHERE UID=?"
    execute_query(query, (id,))
    flash("Employee Deleted Successfully")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
