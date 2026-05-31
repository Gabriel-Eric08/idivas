from flask import Blueprint, render_template

isong_bp = Blueprint('isongs', __name__, url_prefix='/isongs')

@isong_bp.route('/')
def isong():
    return render_template('pages/isongs/index.html')
