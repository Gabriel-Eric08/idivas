from flask import Blueprint, render_template

isnap_bp = Blueprint('isnap', __name__, url_prefix='/isnap')

@isnap_bp.route('/')
def isnap():
    return render_template('pages/isnap/isnap.html')
