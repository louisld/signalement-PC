from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort

from signalement.extensions import db
from signalement.frontend.forms import SForm
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
        db.session.add(signalement)
        db.session.commit()
        return "Signalement enregistré."
    print(sForm.errors)
    return render_template('signalement.html', form=sForm)
