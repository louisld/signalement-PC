activate_this = "venv/bin/activate.py"
with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))


import sys
import os

from signalement import create_app

project = "signalement"

BASE_DIR = os.path.join(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

application = create_app()
