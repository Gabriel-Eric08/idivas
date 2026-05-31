from flask import Blueprint, render_template

iblog_bp = Blueprint('iblog', __name__, url_prefix='/iblog')

@iblog_bp.route('/beyonce')
def iblog_beyonce():
    return render_template('pages/iblog/beyonce.html')
