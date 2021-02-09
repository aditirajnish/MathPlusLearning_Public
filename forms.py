from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Regexp, Optional, NumberRange


class ContactForm(FlaskForm):

    email_expression = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    phone_expression = "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"

    first_name = StringField(label=None, validators=[InputRequired()],
                             render_kw={"placeholder": "First Name",
                                        "class": "form-control form-control-lg",
                                        "id": "first_name"})

    last_name = StringField(label=None, validators=[InputRequired()],
                            render_kw={"placeholder": "Last Name",
                                       "class": "form-control form-control-lg",
                                       "id": "last_name"})

    email = StringField(label=None, validators=[InputRequired(),
                                                Regexp(email_expression,
                                                       message="Please provide a valid email address")],
                        render_kw={"placeholder": "Email",
                                   "class": "form-control form-control-lg",
                                   "id": "email"})

    phone = StringField(label=None, validators=[InputRequired(),
                                          Regexp(phone_expression,
                                                 message="Please provide a valid phone number")],
                        render_kw={"placeholder": "Phone Number",
                                   "class": "form-control form-control-lg",
                                   "id": "phone"})

    question = TextAreaField(label=None, validators=[InputRequired()],
                             render_kw={"placeholder": "Tell us about your question",
                                        "class": "form-control form-control-lg",
                                        "id": "textarea",
                                        "style": "height: 100px;"})

    submit = SubmitField(label="Click Me",
                         render_kw={"class": "btn btn-outline-dark"})


class EnrollForm(FlaskForm):

    parent_first_name = StringField(label=None, validators=[InputRequired()],
                                    render_kw={"placeholder": "Parent's First Name",
                                               "class": "form-control form-control-lg",
                                               "id": "parent_first_name"})

    parent_last_name = StringField(label=None, validators=[InputRequired()],
                                    render_kw={"placeholder": "Parent's Last Name",
                                               "class": "form-control form-control-lg",
                                               "id": "parent_last_name"})

    parent_email = StringField(label=None, validators=[InputRequired(),
                                                       Regexp(ContactForm.email_expression,
                                                              message="Please provide a valid email address")],
                               render_kw={"placeholder": "Email",
                                          "class": "form-control form-control-lg",
                                          "id": "email"})

    parent_phone = StringField(label=None, validators=[InputRequired(),
                                                       Regexp(ContactForm.phone_expression,
                                                              message="Please provide a valid phone number")],
                               render_kw={"placeholder": "Phone Number",
                                          "class": "form-control form-control-lg",
                                          "id": "phone"})

    find_us = TextAreaField(label=None, validators=[Optional()],
                             render_kw={"placeholder": "How did you find us (ex. referral)?",
                                        "class": "form-control form-control-lg",
                                        "id": "find",
                                        "style": "height: 100px;"})

    student_name = StringField(label=None, validators=[InputRequired()],
                               render_kw={"placeholder": "Student's Name",
                                          "class": "form-control form-control-lg",
                                          "id": "student_name"})

    student_grade = IntegerField(label=None, validators=[InputRequired(),
                                                         NumberRange(7, 12, "Please provide a valid grade (7-12)")],
                                 render_kw={"placeholder": "Student's Grade",
                                          "class": "form-control form-control-lg",
                                          "id": "grade"})

    comments = TextAreaField(label=None, validators=[Optional()],
                                render_kw={"placeholder": "Any additional information",
                                          "class": "form-control form-control-lg",
                                          "id": "comments",
                                          "style": "height: 100px;"})

    submit = SubmitField("Click Me",
                         render_kw={"class": "btn btn-outline-dark"})
