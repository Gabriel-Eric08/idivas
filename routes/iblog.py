from flask import Blueprint, render_template

iblog_bp = Blueprint('iblog', __name__, url_prefix='/iblog')

@iblog_bp.route('/beyonce')
def iblog_beyonce():
    return render_template('pages/iblog/beyonce.html')

@iblog_bp.route('/lady_gaga')
def iblog_ladygaga():
    return render_template('pages/iblog/lady_gaga.html')

@iblog_bp.route('/rihanna')
def iblog_rihanna():
    return render_template('pages/iblog/rihanna.html')
