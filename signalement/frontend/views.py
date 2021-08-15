from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g
from flask_babel import lazy_gettext as _
from uuid import uuid4

from signalement.extensions import db
from signalement.frontend.forms import SForm, AccesForm
from signalement.frontend.models import Signalement

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def home():
    return render_template('index.html')


@frontend.route('/signalement', methods=["GET", "POST"])
def signalement():
    sForm = SForm()
    signalement = Signalement()
    if sForm.validate_on_submit():
        sForm.populate_obj(signalement)
        signalement.numero_suivi = str(uuid4())
        db.session.add(signalement)
        db.session.commit()
        return render_template('signalement/confirmation.html', numero_suivi=signalement.numero_suivi)
    print(sForm.errors)
    return render_template('signalement/signalement.html', form=sForm)

@frontend.route('/suivi', methods=["GET", "POST"])
def suivi():
    accesForm = AccesForm()
    if accesForm.validate_on_submit():
        numero_suivi = accesForm.numero_suivi.data.lstrip()
        signalement = Signalement.query.filter_by(numero_suivi=numero_suivi).first()
        if signalement is not None:
            return render_template('signalement/suivi_informations.html', signalement=signalement)
        flash(_("Ce signalement n'a pas été trouvé dans la base de donnée."))
        return render_template('signalement/suivi.html', form=accesForm)
    return render_template('signalement/suivi.html', form=accesForm)
