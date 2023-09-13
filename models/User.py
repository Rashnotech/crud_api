from models import db
from models import datetime

class User(db.Model):
    """
        A User Class that Inherit Inherits from the Base Class
        Args:
            id: unique identifier of the user
            name: string attribute of the user
            created_at: time user was created
            updated_at: time the user made an update
    """
    user_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name):
        self.name = name
        self.created_at = datetime.utcnow
        self.updated_at = self.created_at

    def __repr__(self):
        """ a magic method that return the dictionary
            representation of User class
        """
        return f'User {self.id}'
