from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort
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
        numero_suivi = accesForm.numero_suivi.data
        Signalement.query.filter_by(numero_suivi=numero_suivi)
        return
    return render_template('signalement/suivi.html', form=accesForm)
