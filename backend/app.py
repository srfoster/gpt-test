import os
import json
from flask import Flask, send_from_directory, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from datetime import date, datetime

app = Flask(__name__, static_folder='../frontend/hello-world-angular/dist/hello-world-angular')

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # This sets up a one-to-many relationship between User and Adventure.
    # When you query a user object, you can access its adventures with user.adventures attribute
    adventures = relationship('Adventure', back_populates='user')

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

    def __repr__(self):
        return self.username + " - " + self.email

class Adventure(db.Model):
    __tablename__ = 'adventures'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    mileage = db.Column(db.Float)
    estimated_calories = db.Column(db.Float)

    # Foreign key for the user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # This sets up a many-to-one relationship between Adventure and User.
    # When you query an adventure object, you can access its user with adventure.user attribute
    user = relationship('User', back_populates='adventures')

@app.route('/add_user/<username>/<email>')
def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return "User {username} added!"

@app.route('/list_users')
def list_users():
    print("Listing users")
    users = User.query.all()
    print(users)
    users_json = json.dumps([user.to_dict() for user in users])
    return users_json

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
SessionLocal = sessionmaker(bind=engine)

@app.route("/add_adventure", methods=["POST"])
def add_adventure():
    session = SessionLocal()

    try:
        data = request.json

        user_id = 1 #data['user_id']
        user = session.query(User).filter(User.id == user_id).first()
        
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        # Parse the date string into a date object
        date_object = datetime.strptime(data['date'], '%Y-%m-%d').date()

        adventure = Adventure(
            date = date_object,
            category = data['category'],
            mileage = data['mileage'],
            estimated_calories = data['estimated_calories'],
            user = user
        )

        session.add(adventure)
        session.commit()
        return jsonify({"message": "Adventure added successfully", "adventure_id": adventure.id}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

@app.route("/list_adventures/<int:user_id>", methods=["GET"])
def list_adventures(user_id):
    session = SessionLocal()

    try:
        user = session.query(User).filter(User.id == user_id).first()
        
        if not user:
            return jsonify({"error": "User not found"}), 404

        adventures = session.query(Adventure).filter(Adventure.user_id == user_id).all()

        # Convert the list of adventures to a list of dictionaries to be JSON serialized
        adventures_list = [{
            "id": adventure.id,
            "date": adventure.date.strftime('%Y-%m-%d'),  # Format the date for output
            "category": adventure.category,
            "mileage": adventure.mileage,
            "estimated_calories": adventure.estimated_calories
        } for adventure in adventures]

        return jsonify(adventures_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
  if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
    return send_from_directory(app.static_folder, path)
  else:
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()