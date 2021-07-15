import string
import random
import os

from datetime import datetime

def get_current_time():
    return datetime.utcnow()

def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except:
        raise e
