from flask import Blueprint, render_template

inews_bp = Blueprint('inews', __name__, url_prefix='/inews')

@inews_bp.route('/beyonce')
def inews_beyonce():
    return render_template('inews/inews_beyonce.html')
