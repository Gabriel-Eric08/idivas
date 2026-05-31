from flask import Flask, render_template
from routes import iblog_bp, inews_bp, isong_bp

app = Flask(__name__)

app.register_blueprint(iblog_bp)
app.register_blueprint(inews_bp)
app.register_blueprint(isong_bp)

@app.route('/')
def home():
    return render_template('pages/home.html')

if __name__ == '__main__':
    app.run(debug=True)