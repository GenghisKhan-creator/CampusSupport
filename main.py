from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, session
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, BLOB, LargeBinary,Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,validators, TimeField, SelectField, PasswordField, EmailField, DateField
from wtforms.validators import DataRequired,Email
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_session import Session
import uuid as uuid
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = "transgender"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"  # Adjust as needed
Session(app)
Bootstrap5(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

users = {
    'admin@methodistuni.com': {
        'password': 'admin1234'
    }
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None


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
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    request: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


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
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


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
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    img: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    prefered_date: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    list_of_courses: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    prefered_programme: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()


class LoginForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired(),
                    validators.length(
                        3,
                        message='must be more than 3 characters'
                    )
                    ],
        render_kw={
            'placeholder': 'Admin@methodist'
        }
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        username = login_form.username.data
        password = login_form.password.data
        print(username)
        print(password)
        if login_form.validate_on_submit():
            if username in users and users[username]['password'] == password:
                user = User(username)
                login_user(user)
                return redirect('dashboard')
            else:
                flash('Invalid Username or Password', 'error')
    return render_template('login.html', my_login = login_form)

@app.route('/login')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

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
            pic = request.files.get('pic')
            img_filename = secure_filename(pic.filename)
            pic_name = str(uuid.uuid1()) + "_" + img_filename
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            print(pic_name)
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
                img = pic_name,
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


@app.route('/mark_complaint_as_read', methods=['POST'])
def mark_complaint_as_read():
    data = request.json
    complaint_id = data.get('complaint_id')

    if complaint_id:
        complaint = ComplaintForm.query.get(complaint_id)
        if complaint:
            complaint.is_read = True
            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400

@app.route('/mark_change_programme_as_read', methods=['POST'])
def mark_change_programme_as_read():
    data = request.json
    programme_id = data.get('programme_id')

    if programme_id:
        programme = ChangeProgramme.query.get(programme_id)
        if programme:
            programme.is_read = True
            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400

@app.route('/mark_deferment_as_read', methods=['POST'])
def mark_deferment_as_read():
    data = request.json
    deferment_id = data.get('deferment_id')

    if deferment_id:
        deferments = Deferment.query.get(deferment_id)
        if deferments:
            deferments.is_read = True
            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400

@app.route('/mark_resit_as_read', methods=['POST'])
def mark_resit_as_read():
    data = request.json
    resit_id = data.get('resit_id')

    if resit_id:
        resits = Resit.query.get(resit_id)
        if resits:
            resits.is_read = True
            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400

@app.route('/mark_schoolfees_as_read', methods=['POST'])
def mark_schoolfees_as_read():
    data = request.json
    schoolfees_id = data.get('schoolfees_id')

    if schoolfees_id:
        school = SchoolFees.query.get(schoolfees_id)
        if school:
            school.is_read = True
            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400

@app.route('/mark_general_request_as_read', methods=['POST'])
def mark_general_request_as_read():
    data = request.json
    general_id = data.get('general_id')

    if general_id:
        general = GeneralRequest.query.get(general_id)
        if general:
            general.is_read = True
            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400


@app.route('/dashboard')
@login_required
def dashboard():
    recent_complaint = db.session.execute(db.select(ComplaintForm).order_by(ComplaintForm.created_at.desc())).scalars().first()
    recent_change = db.session.execute(db.select(ChangeProgramme).order_by(ChangeProgramme.created_at.desc())).scalars().first()
    recent_deferment = db.session.execute(db.select(Deferment).order_by(Deferment.created_at.desc())).scalars().first()
    recent_resit = db.session.execute(db.select(Resit).order_by(Resit.created_at.desc())).scalars().first()
    latest_schoolfees = db.session.execute(db.select(SchoolFees).order_by(SchoolFees.created_at.desc())).scalars()
    first_name2 = latest_schoolfees.first()
    recent_general = db.session.execute(db.select(GeneralRequest).order_by(GeneralRequest.created_at.desc())).scalars().first()
    return render_template('dashboard.html',
                           recent_complaint=recent_complaint,
                           recent_change=recent_change,
                           recent_deferment=recent_deferment,
                           recent_resit=recent_resit,
                           latest_schoolfees=first_name2,
                           recent_general=recent_general
    )

@app.route('/complaint')
@login_required
def complaint_dash():
    show_complaint = db.session.execute(db.select(ComplaintForm).order_by(ComplaintForm.created_at.desc())).scalars()
    clicked = session.get('button_clicked', False)
    return render_template('complaint_dash.html', complaint=show_complaint, clicked=clicked)


@app.route('/change programme')
@login_required
def change_programme():
    show_change = db.session.execute(db.select(ChangeProgramme).order_by(ChangeProgramme.created_at.desc())).scalars()
    return render_template('change_programme.html', program=show_change)

@app.route('/deferment')
@login_required
def deferment():
    show_deferment = db.session.execute(db.select(Deferment).order_by(Deferment.created_at.desc())).scalars()
    return render_template('deferment.html', deferments=show_deferment)

@app.route('/resit')
@login_required
def resit():
    show_resit = db.session.execute(db.select(Resit).order_by(Resit.created_at.desc())).scalars()
    return render_template('resit.html', resits=show_resit)

@app.route('/school fees')
@login_required
def school_fees():
    show_schoolfees = db.session.execute(db.select(SchoolFees).order_by(SchoolFees.created_at.desc())).scalars()
    return render_template('school_fees.html', all_fees=show_schoolfees)

@app.route('/general requests')
@login_required
def general_request():
    general_requests = db.session.execute(db.select(GeneralRequest).order_by(GeneralRequest.created_at.desc())).scalars()
    return render_template('general_request.html', general_requests=general_requests)


if __name__ == "__main__":
    app.run(debug=True)