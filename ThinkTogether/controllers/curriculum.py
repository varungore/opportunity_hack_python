__author__ = 'dhara'

import os
from flask import Blueprint, Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

# Import module models (i.e. Curriculum)
from ThinkTogether.models.curriculum import Curriculum

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/curriculum_files')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in mod_auth.config['ALLOWED_EXTENSIONS']

# Set the route and accepted methods
@mod_auth.route('/', methods=['GET', 'POST'])
def curriculum_files():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(mod_auth.config['ALLOWED_EXTENSIONS'], filename))
            # TODO add in DB
            return filename
    return '''

