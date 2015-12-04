from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Oh no, not me, I never lost control"
