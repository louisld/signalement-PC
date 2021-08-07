from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional
 )
from flask_babel import lazy_gettext as _


class LoginForm(FlaskForm):
    email = StringField(
        _("Email"),
        validators=[
            DataRequired(),
            Email(message=_("Err_valid_email"))
        ]
    )
    password = PasswordField(_("Password"), validators=[DataRequired()])
    submit = SubmitField(_("log_in"))
