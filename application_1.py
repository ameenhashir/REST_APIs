from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return str({'id': self.id, 'username': self.username, 'email': self.email})


@app.route("/")
def index():
    return {'Data': 'Drinks Data'}


@app.route("/Users")
def get_users():
    output = []
    for user in User.query.all():
        output.append({'id': user.id, 'username': user.username, 'email': user.email})
    return {'Users': output}


@app.route("/Users/<id>")
def get_user(id):
    user = User.query.get_or_404(id)
    return {'id': user.id, 'username': user.username, 'email': user.email}


@app.route("/Users", methods=['POST'])
def post_user():
    user = User(username=request.json['username'], email=request.json['email'])
    db.session.add(user)
    db.session.commit()
    return {'id': user.id}


@app.route("/Users/<id>", methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return {'id': user.id, 'username': user.username, 'email': user.email}


if __name__ == '__main__':
    app.run(debug=True, port=3001)
