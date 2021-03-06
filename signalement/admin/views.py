import datetime

from flask import Blueprint, render_template, flash, \
        url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user
from flask_babel import lazy_gettext as _

from signalement.extensions import login_manager, db
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
    signalements_new = Signalement.query.filter_by(statut=SignalementStatut.new).order_by(Signalement.date_updated.desc()).all()
    signalements_opened = Signalement.query.filter_by(statut=SignalementStatut.opened).order_by(Signalement.date_updated.desc()).all()
    signalements_closed = Signalement.query.filter_by(statut=SignalementStatut.closed).order_by(Signalement.date_updated.desc()).all()
    return render_template('admin/dashboard.html',
                           signalements_new=signalements_new,
                           signalements_opened=signalements_opened,
                           signalements_closed=signalements_closed)


@admin.route('/signalement/<int:id>')
@login_required
def signalement(id):
    signalement = Signalement.query.get(id)
    if not signalement:
        flash(_("signalement-not-found"))
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/signalement.html', signalement=signalement)


@admin.route('/signalement/set_new/<int:id>')
@login_required
def signalement_set_new(id):
    signalement = Signalement.query.get(id)
    if not signalement:
        flash(_("signalement-not-found"))
        return redirect(url_for('admin.dashboard'))
    signalement.statut = SignalementStatut.new
    db.session.commit()
    flash(_("signalement-set-new"))
    return redirect(url_for('admin.signalement', id=id))


@admin.route('/signalement/set_opened/<int:id>')
@login_required
def signalement_set_opened(id):
    signalement = Signalement.query.get(id)
    if not signalement:
        flash(_("signalement-not-found"))
        return redirect(url_for('admin.dashboard'))
    signalement.statut = SignalementStatut.opened
    db.session.commit()
    flash(_("signalement-set-opened"))
    return redirect(url_for('admin.signalement', id=id))


@admin.route('/signalement/set_closed/<int:id>')
@login_required
def signalement_set_closed(id):
    signalement = Signalement.query.get(id)
    if not signalement:
        flash(_("signalement-not-found"))
        return redirect(url_for('admin.dashboard'))
    signalement.statut = SignalementStatut.closed
    db.session.commit()
    flash(_("signalement-set-closed"))
    return redirect(url_for('admin.signalement', id=id))


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('frontend.home'))
