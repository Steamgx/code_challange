from app import app, db
from models import Hero, Power, HeroPower
from faker import Faker
import random

# Initialize Faker
faker = Faker()

# Function to Seed Database with Fake Data
def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(HeroPower).delete()
        db.session.query(Hero).delete()
        db.session.query(Power).delete()
        
        # Create Fake Heroes
        heroes = [
            Hero(name=faker.name(), super_name=faker.first_name() + " " + faker.word().capitalize())
            for _ in range(10)  # Generate 10 random heroes
        ]

        # Create Fake Powers
        powers = [
            Power(name=faker.word().capitalize() + " Power", description=faker.sentence())
            for _ in range(6)  # Generate 6 random powers
        ]

        # Add Heroes and Powers to DB
        db.session.add_all(heroes)
        db.session.add_all(powers)
        db.session.commit()  # Commit to get generated IDs

        # Assign Random Powers to Heroes
        hero_powers = [
            HeroPower(
                strength=random.choice(["Weak", "Average", "Strong"]),
                hero_id=random.choice(heroes).id,
                power_id=random.choice(powers).id
            )
            for _ in range(15)  # Assign 15 random hero-power relationships
        ]

        db.session.add_all(hero_powers)
        db.session.commit()

        print("✅ Database Seeded with Fake Data Successfully!")

# Run the Seeding Function
if __name__ == "__main__":
    seed_data()
