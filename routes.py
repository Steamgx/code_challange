from flask import Flask, jsonify, request
from app import app, db
from models import Hero, Power, HeroPower

# ✅ Route: Get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{ "id": hero.id, "name": hero.name, "super_name": hero.super_name } for hero in heroes]), 200

# ✅ Route: Get a single hero by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        powers = [{"id": hp.power.id, "name": hp.power.name, "description": hp.power.description} for hp in hero.hero_powers]
        return jsonify({
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": powers
        }), 200
    return jsonify({"error": "Hero not found"}), 404

# ✅ Route: Delete a hero
@app.route('/heroes/<int:id>', methods=['DELETE'])
def delete_hero(id):
    hero = Hero.query.get(id)
    if hero:
        db.session.delete(hero)
        db.session.commit()
        return jsonify({"message": "Hero deleted successfully"}), 200
    return jsonify({"error": "Hero not found"}), 404

# ✅ Route: Get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{ "id": power.id, "name": power.name, "description": power.description } for power in powers]), 200

# ✅ Route: Get a single power by ID
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify({ "id": power.id, "name": power.name, "description": power.description }), 200
    return jsonify({"error": "Power not found"}), 404

# ✅ Route: Delete a power
@app.route('/powers/<int:id>', methods=['DELETE'])
def delete_power(id):
    power = Power.query.get(id)
    if power:
        db.session.delete(power)
        db.session.commit()
        return jsonify({"message": "Power deleted successfully"}), 200
    return jsonify({"error": "Power not found"}), 404

# ✅ Route: Update a power (PATCH)
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    if "description" in data:
        power.description = data["description"]
        db.session.commit()
        return jsonify({ "id": power.id, "name": power.name, "description": power.description }), 200

    return jsonify({"error": "Invalid data"}), 400

# ✅ Route: Assign a power to a hero (POST)
@app.route('/hero_powers', methods=['POST'])
def assign_power():
    data = request.get_json()
    
    hero = Hero.query.get(data.get("hero_id"))
    power = Power.query.get(data.get("power_id"))
    
    if not hero or not power:
        return jsonify({"error": "Invalid hero or power ID"}), 400

    if "strength" not in data or data["strength"] not in ['Strong', 'Weak', 'Average']:
        return jsonify({"errors": ["strength must be 'Strong', 'Weak', or 'Average'"]}), 400

    new_hero_power = HeroPower(
        strength=data.get("strength", "Average"),
        hero_id=data["hero_id"],
        power_id=data["power_id"]
    )
    
    db.session.add(new_hero_power)
    db.session.commit()

    return jsonify({ "id": new_hero_power.id, "strength": new_hero_power.strength, "hero_id": new_hero_power.hero_id, "power_id": new_hero_power.power_id }), 201

# ✅ Route: Delete a hero power
@app.route('/hero_powers/<int:id>', methods=['DELETE'])
def delete_hero_power(id):
    hero_power = HeroPower.query.get(id)
    if hero_power:
        db.session.delete(hero_power)
        db.session.commit()
        return jsonify({"message": "Hero power deleted successfully"}), 200
    return jsonify({"error": "Hero power not found"}), 404
