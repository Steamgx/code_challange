from database import db
from sqlalchemy.orm import validates

# Hero Model
class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Hero {self.name} - {self.super_name}>'

# Power Model
class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return description

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Power {self.name}>'

# HeroPower (Join Table)
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    __table_args__ = (
        db.CheckConstraint("strength IN ('Strong', 'Weak', 'Average')", name="check_strength"),
    )

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    def __repr__(self):
        return f'<HeroPower Hero: {self.hero_id}, Power: {self.power_id}, Strength: {self.strength}>'
