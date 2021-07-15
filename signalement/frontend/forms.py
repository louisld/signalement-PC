from flask_babel import lazy_gettext as _
from wtforms_alchemy import model_form_factory
from wtforms import FileField, BooleanField
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from signalement.extensions import db

from signalement.frontend.models import Signalement

BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class SForm(ModelForm):

    class Meta:
        model = Signalement

    fichier = FileField(None)

    # Transmettre
    confirmation = BooleanField(_(" Je confirme vous transmettre mon signalement de manière désintéressée et de bonne foi.*"))

    def validate_fichier(form, field):
        if field.data:
            field.data = secure_filename(field.data)
