from flask import Blueprint, render_template

isong_bp = Blueprint('isong', __name__, url_prefix='/isong')

@isong_bp.route('/')
def isong():
    return render_template('isongs.html')
