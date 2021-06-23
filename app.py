from flask import Flask, render_template, url_for
from forms import ContactForm, EnrollForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
app.config.from_json("config.json")

@app.route('/')
def home():
    return render_template("home.html")

def upload_information_to_google_sheet(information, sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open(sheet_name).sheet1
    sheet.append_row(information)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        information = [form.first_name.data,
                       form.last_name.data,
                       form.email.data,
                       form.phone.data,
                       form.question.data]
        upload_information_to_google_sheet(information, "Question Form")
        return render_template("contact.html", valid=True)
    return render_template("contact.html", form=form)

@app.route('/enroll', methods=["GET", "POST"])
def enroll():
    form = EnrollForm()
    if form.validate_on_submit():
        information = [form.parent_first_name.data,
                       form.parent_last_name.data,
                       form.parent_email.data,
                       form.parent_phone.data,
                       form.find_us.data,
                       form.comments.data,
                       form.student_name.data,
                       form.student_grade.data]
        upload_information_to_google_sheet(information, "Enrollment Form")
        return render_template("enroll.html", valid=True)
    return render_template("enroll.html", form=form)
