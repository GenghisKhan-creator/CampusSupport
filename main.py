from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, BLOB, LargeBinary
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,validators, TimeField, SelectField, PasswordField, EmailField, DateField
from wtforms.validators import DataRequired,Email


app = Flask(__name__)
app.config['SECRET_KEY'] = "transgender"
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus-support.db"


db.init_app(app)


class GeneralRequest(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    first_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    other_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    student_id: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    programme: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    level: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    date: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    department: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    faculty: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    request: Mapped[str] = mapped_column(String, unique=False, nullable=False)


class ComplaintForm(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    first_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    other_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    student_id: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    programme: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    level: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    date: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    department: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    faculty: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    course_code: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    course_title: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    lecturer_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    taken_year: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    semester_taken: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    session_taken: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    grade_awarded: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    complaint_nature: Mapped[str] = mapped_column(String, unique=False, nullable=False)


class SchoolFees(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    first_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    other_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    student_id: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    programme: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    level: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    date: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    department: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    faculty: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    school_feesc: Mapped[str] = mapped_column(String, unique=False, nullable=False)


class Deferment(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    first_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    other_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    student_id: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    programme: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    level: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    date: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    department: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    faculty: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    prefered_date: Mapped[str] = mapped_column(String, unique=False, nullable=False)

class Resit(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    first_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    other_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    student_id: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    programme: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    level: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    date: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    department: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    faculty: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    list_of_courses: Mapped[str] = mapped_column(String, unique=False, nullable=False)

class ChangeProgramme(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    first_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    other_name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    student_id: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    programme: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    level: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    date: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    department: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    faculty: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    prefered_programme: Mapped[str] = mapped_column(String, unique=False, nullable=False)

with app.app_context():
    db.create_all()


class LoginForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired(), validators.length(3, message='must be more than 3 characters')],
        render_kw={'placeholder': 'Admin@methodist'}
    )

    password = PasswordField(
        label='Password',
        validators = [DataRequired(), validators.length(8, message='password must be more than 8')],
        render_kw={'placeholder': 'Password'}
    )

    signin = SubmitField('Login')


class GetForms(FlaskForm):
    form_type = SelectField(
        label='Complaint Type:',
        validators=[DataRequired()],
        choices=['Complaint Form', 'School Fees', 'Resit', 'Deferment', 'Change Programme', 'Make a request']
    )

    submit_choice = SubmitField('Submit')


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/login')
def login():
    login_form = LoginForm()
    email = "admin@methodistuni.com"
    password = "admin1234"
    if login_form.validate_on_submit():
        if login_form.username.data != email and login_form.password.data != password:
            flash('Error!', 'error')
    return render_template('login.html', my_login = login_form)


@app.route('/forms', methods=['GET', 'POST'])
def get_started():
    form = GetForms()
    current_form = form.form_type.data
    print(current_form)
    action = request.form.get("Request")
    action1= request.form.get("submit_complaint")
    action2 = request.form.get("fees_submit")
    action3 = request.form.get('def_button')
    action4 = request.form.get('sit_submit')
    action5 = request.form.get('prog_submit')
    if action == "Request":
        if request.method == "POST":
            new_request = GeneralRequest(
                surname = request.form.get('request_surname'),
                first_name = request.form.get('request_firstname'),
                other_name = request.form.get('request_othername'),
                student_id = request.form.get('request_student_id'),
                programme = request.form.get('request_programme'),
                level = request.form.get('request_level'),
                date = request.form.get('request_date'),
                phone_number = request.form.get('request_phone'),
                department = request.form.get('request_department'),
                faculty = request.form.get('request_faculty'),
                request = request.form.get('request_make')
            )
            db.session.add(new_request)
            db.session.commit()
            flash('Sent!', 'success')
            return redirect(url_for('get_started'))

    if action1 == "submit_complaint":
        if request.method == "POST":
            new_complaint = ComplaintForm(
                surname = request.form.get('surname'),
                first_name=request.form.get('firstname'),
                other_name=request.form.get('othername'),
                student_id=request.form.get('student_id'),
                programme=request.form.get('programme'),
                level=request.form.get('level'),
                date=request.form.get('date'),
                phone_number=request.form.get('phone'),
                department=request.form.get('department'),
                faculty=request.form.get('faculty'),
                course_code= request.form.get('code'),
                course_title = request.form.get('course_title'),
                lecturer_name = request.form.get('lecturer'),
                taken_year = request.form.get('year_taken'),
                semester_taken= request.form.get('semester_taken'),
                session_taken= request.form.get('session_taken'),
                grade_awarded= request.form.get('grade'),
                complaint_nature= request.form.get('nature')
            )
            db.session.add(new_complaint)
            db.session.commit()
            flash('Sent!', 'success')
            return redirect(url_for('get_started'))

    if action2 == "fees_submit":
        if request.method == "POST":
            file = request.files.get('bank_receipt')
            new_fees = SchoolFees(
                surname=request.form.get('fees_surname'),
                first_name=request.form.get('fees_firstname'),
                other_name=request.form.get('fees_othername'),
                student_id=request.form.get('fees_studentid'),
                programme=request.form.get('fees_programme'),
                level=request.form.get('fees_level'),
                date=request.form.get('fees_date'),
                phone_number=request.form.get('fees_phone'),
                department=request.form.get('fees_department'),
                faculty=request.form.get('fees_faculty'),
                school_feesc=request.form.get('school_feesc')
            )

            db.session.add(new_fees)
            db.session.commit()
            flash('Sent!', 'success')
            return redirect(url_for('get_started'))

    if action3 == "def_button":
        if request.method == 'POST':
            new_deferment = Deferment(
                surname=request.form.get('def_surname'),
                first_name=request.form.get('def_firstname'),
                other_name=request.form.get('def_othername'),
                student_id=request.form.get('def_studentid'),
                programme=request.form.get('def_programme'),
                level=request.form.get('def_level'),
                date=request.form.get('def_date'),
                phone_number=request.form.get('def_phone'),
                department=request.form.get('def_department'),
                faculty=request.form.get('def_faculty'),
                prefered_date=request.form.get('def_datepref')
            )

            db.session.add(new_deferment)
            db.session.commit()
            flash('Sent!', 'success')
            return redirect(url_for('get_started'))

    if action4 == 'sit_submit':
        if request.method == 'POST':
            new_resit = Resit(
                surname=request.form.get('sit_surname'),
                first_name=request.form.get('sit_firstname'),
                other_name=request.form.get('sit_othername'),
                student_id=request.form.get('sit_studentid'),
                programme=request.form.get('sit_programme'),
                level=request.form.get('sit_level'),
                date=request.form.get('sit_date'),
                phone_number=request.form.get('sit_phone'),
                department=request.form.get('sit_department'),
                faculty=request.form.get('sit_faculty'),
                list_of_courses=request.form.get('sit_listcourse')
            )

            db.session.add(new_resit)
            db.session.commit()
            flash('Sent!', 'success')
            return redirect(url_for('get_started'))

    if action5 == "prog_submit":
        if request.method == 'POST':
            new_change_programme = ChangeProgramme(
                surname=request.form.get('prog_surname'),
                first_name=request.form.get('prog_firstname'),
                other_name=request.form.get('prog_othername'),
                student_id=request.form.get('prog_studentid'),
                programme=request.form.get('prog_programme'),
                level=request.form.get('prog_level'),
                date=request.form.get('prog_date'),
                phone_number=request.form.get('prog_phone'),
                department=request.form.get('prog_department'),
                faculty=request.form.get('prog_faculty'),
                prefered_programme=request.form.get('prog_prefered')
            )
            db.session.add(new_change_programme)
            db.session.commit()
            flash('Sent!', 'success')
            return redirect(url_for('get_started'))

    return render_template('getstarted.html', form=form, current_form=current_form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/complaint')
def complaint_dash():
    return render_template('complaint_dash.html')

@app.route('/change programme')
def change_programme():
    return render_template('change_programme.html')

@app.route('/deferment')
def deferment():
    return render_template('deferment.html')

@app.route('/resit')
def resit():
    return render_template('resit.html')

@app.route('/school fees')
def school_fees():
    return render_template('school_fees.html')

@app.route('/general requests')
def general_request():
    return render_template('general_request.html')


if __name__ == "__main__":
    app.run(debug=True)