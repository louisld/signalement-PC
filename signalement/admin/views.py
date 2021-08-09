from flask import Blueprint, render_template, flash, \
        url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user
from flask_babel import lazy_gettext as _

from signalement.extensions import login_manager
from signalement.admin.forms import LoginForm
from signalement.admin.models import User
from signalement.frontend.models import Signalement, SignalementStatut

admin = Blueprint('admin', __name__, url_prefix="/admin")


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


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('frontend.home'))


@admin.route('/dashboard')
@login_required
def dashboard():
    signalements_new = Signalement.query.filter_by(statut=SignalementStatut.new).all()
    return render_template('admin/dashboard.html', signalements_new=signalements_new)


@admin.route('/signalement/<int:id>')
@login_required
def signalement(id):
    signalement = Signalement.query.get(id)
    if not signalement:
        print("PAs vu")
        flash(_("signalement-not-found"))
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/signalement.html', signalement=signalement)


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('frontend.home'))
