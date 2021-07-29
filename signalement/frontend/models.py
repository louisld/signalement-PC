import datetime

from sqlalchemy import Column
from flask_babel import lazy_gettext as _
from sqlalchemy_utils import EmailType, PhoneNumberType, ChoiceType

from signalement.extensions import db


class Signalement(db.Model):

    __tablename__ = "signalement"

    id = Column(db.Integer, primary_key=True)

    # Initialiser
    categorie_choices = [
        ("0", _("--Sélectionnez--")),
        ("1", _("1. Je souhaite faire un signalement")),
        ("2", _("2. Je souhaite prendre un rendez-vous avec la référente « écoute »"))
    ]
    categorie = Column(
        ChoiceType(categorie_choices),
        info={"label": _("Catégorie")}
    )
    # Identifier
    sous_categorie_choices = [
        ("1", _("1.1 Agression sexuelle")),
        ("2", _("Viol")),
        ("3", _("Harcèlement moral")),
        ("4", _("Harcèlement sexuel")),
        ("5", _("Cyber harcèlement")),
        ("6", _("Agissement sexiste")),
        ("7", _("Discriminations")),
        ("8", _("Violences"))
    ]
    sous_categorie = Column(
        ChoiceType(sous_categorie_choices),
        info={"label": _("Sous-catégorie")},
        nullable=True
    )
    # Identifier
    nom = Column(
        db.String(255),
        info={"label": _("Nom*")},
        nullable=False
    )
    prenom = Column(
        db.String(255),
        info={"label": _("Prénom*")},
        nullable=False
    )
    email = Column(
        EmailType,
        info={"label": _("Email*")},
        nullable=False
    )
    telephone = Column(
        PhoneNumberType,
        info={
            "label": _("Téléphone"),
            "render_kw": {
                "placeholder": "+00 0000000"
            }
        },
        nullable=True
    )
    anonyme = Column(
        db.Boolean(),
        info={"label": _("Je souhaite rester anonyme pour faire ce signalement")}
    )
    # Décrire
    preocupation = Column(
        db.String(255),
        info={"label": _("Quelle est votre préoccupation ?*")},
        nullable=False
    )
    date = Column(
        db.Date(),
        info={"label": _("À quelle date se sont déroulés les faits ?")},
        nullable=True
    )
    lieu = Column(
        db.String(255),
        info={"label": _("Où se sont déroulés les faits ?*")},
        nullable=False
    )
    description = Column(
        db.Text(),
        info={"label": _("Décrivez précisement la situation ou les faits.*")},
        nullable=False
    )
    temoin = Column(
        db.String(255),
        info={"label": _("Y a-t-il eu des témoins / d'autres témoins de la situation ? Si oui, précisez leur identité si vous la connaissez.")},
        nullable=True
    )
    premiere_choices = [
        ("1", "Oui"),
        ("2", "Je ne sais pas"),
        ("0", "Non")

    ]
    premiere = Column(
        ChoiceType(premiere_choices),
        info={"label": _("Est-ce la première fois que cette situation est observée ?*")}
    )
    fichier = Column(
        db.String(255),
        info={"label": _("Avez-vous des fichiers en lien avec votre signalement à nous transmettre ?")},
        nullable=True
    )
    recontact_choices = [
        ("0", "Non"),
        ("1", "Oui")
    ]
    recontact = Column(
        ChoiceType(recontact_choices),
        info={"label": _("Souhaitez-vous être recontacté par la référence écoute ?*")}
    )
    modalite = Column(
        db.Text(),
        info={"label": _("Si vous avez répondu « oui » à la question précédente n’hésitez pas à nous préciser les modalités de prise de contact privilégié et les horaires souhaités.")},
        nullable=True
    )
    numero_suivi = Column(
        db.String(36),
        unique=True
    )
    date_signalement = Column(
        db.DateTime(),
        default=datetime.datetime.utcnow
    )
