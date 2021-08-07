from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort
from flask_login import login_required, logout_user, current_user, login_user
from flask_babel import lazy_gettext as _

from signalement.extensions import db, login_manager
from signalement.admin.forms import LoginForm
from signalement.admin.models import User

admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash(_("invalid_username_or_password"))
        return redirect(url_for('admin.login'))

    return render_template('admin/login.html', form=form)

@admin.route('/dashboard')
def dashboard():
    return "\\o/"
