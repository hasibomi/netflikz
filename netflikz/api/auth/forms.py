from wtforms import fields
from wtforms import validators
from wtforms.fields import html5
from wtforms.form import Form


class FormSignUp(Form):
    email = html5.EmailField(validators=[
        validators.InputRequired(),
        validators.Email(message="Email is required")
    ])
    password = fields.PasswordField(
        validators=[
            validators.InputRequired(message="Password is required"),
            validators.EqualTo("password_confirmation", message="Passwords must match")
        ]
    )
    password_confirmation = fields.PasswordField(
        validators=[
            validators.InputRequired(message="Password confirmation is required")
        ]
    )


class FormSignIn(Form):
    email = html5.EmailField(
        validators=[
            validators.InputRequired(),
            validators.Email(message="Email is required")
        ]
    )
    password = fields.PasswordField(
        validators=[
            validators.InputRequired(
                message="Password is required"
            )
        ]
    )
