from app import db
import enum

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
        }

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    def to_dict(self):
        return {
            "number": self.number,
            "street": self.street,
            "city": self.city,
            "state": self.state
        }