from flask import Blueprint, render_template, current_app
import os

inews_bp = Blueprint('inews', __name__, url_prefix='/inews')

@inews_bp.route('/')
def inews():
    pasta_jornal = os.path.join(
        current_app.static_folder,
        'media',
        'jornal'
    )

    try:
        imagens_jornal = [
            img for img in os.listdir(pasta_jornal)
            if img.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]
    except FileNotFoundError:
        print("Erro: A pasta static/media/jornal não foi encontrada!")
        imagens_jornal = []

    return render_template(
        'pages/inews/index.html',
        imagens_jornal=imagens_jornal
    )