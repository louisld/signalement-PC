import os
from collections import OrderedDict
from flask import Markup

# Role levels

ADMIN = 0
MODO = 1
USER_ROLE = {
    ADMIN: 'Administrateur',
    MODO: 'Modérateur'
}
USER_ROLE = OrderedDict(sorted(USER_ROLE.items()))
