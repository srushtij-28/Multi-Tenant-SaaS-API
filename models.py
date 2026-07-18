from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    tenant_id = db.Column(
        db.String(50),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )
