from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

# Replace the following with your MySQL database connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:deviPravu26@localhost/devi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model for internship registration
class User_Details(db.Model):
    User_Id = db.Column(db.Integer, primary_key=True)
    Full_name = db.Column(db.String(100), nullable=False)
    Date_Of_Birth = db.Column(db.Date, nullable=False)
    Email_Id = db.Column(db.String(255), unique=True, nullable=False)
    Phone_number = db.Column(db.String(10), unique=True, nullable=False)
    Mode_Of_Internship = db.Column(db.String(100), nullable=False)
    Skills = db.Column(db.String(300), nullable=False)
    Duration_Period = db.Column(db.String(200), nullable=False)
    Domain = db.Column(db.String(200), nullable=False)
    Department = db.Column(db.String(200), nullable=False)
    College_Name = db.Column(db.String(250), nullable=False)

# Route for internship registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['name']
        Date_of_birth = request.form['dob']
        Emailid = request.form['email']
        Phoneno = request.form['phone']
        Mode = request.form['mode']
        skills = request.form['skills']
        duration = request.form['duration']
        domain = request.form['domain']
        depart = request.form['depart']
        college = request.form['clg']

        # Create a new registration entry
        registration = User_Details(
            Full_name=fullname,
            Date_Of_Birth=Date_of_birth,
            Email_Id=Emailid,
            Phone_number=Phoneno,
            Mode_Of_Internship=Mode,
            Skills=skills,
            Duration_Period=duration,
            Domain=domain,
            Department=depart,
            College_Name=college,
        )

        db.session.add(registration)
        db.session.commit()

        return redirect(url_for('registration_success'))

    return render_template('mainhtml.html')

# Route for displaying registration success
@app.route('/success')
def registration_success():
    return "Registration Successful!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0')
