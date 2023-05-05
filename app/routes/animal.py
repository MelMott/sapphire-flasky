from flask import Blueprint, jsonify, abort, make_response, request
from app.models.animal import Animal
from app import db

def get_valid_item_by_id(id):
    model = Animal
    try:
        id = int(id)
    except:
        abort(make_response({'msg': f"Invalid id '{id}'"}, 400))

    item = model.query.get(id)

    return item if item else abort(make_response({'msg': f"No {model.__name__} with id {id}"}, 404))


# All routes defined with animals_bp start with url_prefix (/animals)
animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

@animals_bp.route("", methods=['GET'])
def handle_animals():
    name_query = request.args.get("name")
    if name_query:
        animals = Animal.query.filter_by(name=name_query)
    else:
        animals = Animal.query.all()
    animals_response = []
    for animal in animals:
        animals_response.append(animal.to_dict())
    return jsonify(animals_response), 200

@animals_bp.route("", methods=['POST'])
def create_animal():
    # Get the data from the request body
    request_body = request.get_json()

    # Use it to make an Animal
    new_animal = Animal.from_dict(request_body)

    # Persist (save, commit) it in the database
    db.session.add(new_animal)
    db.session.commit()

    # Give back our response
    return {
        "id": new_animal.id,
        "name": new_animal.name,
        "msg": "Successfully created"
    }, 201


@animals_bp.route("/<animal_id>", methods=["GET"])
def handle_animal(animal_id):
    animal = get_valid_item_by_id(animal_id)
    return animal.to_dict(), 200

@animals_bp.route("/<animal_id>", methods=["PUT"])
def update_one_animal(animal_id):
    request_body = request.get_json()
    animal_to_update = get_valid_item_by_id(animal_id)
    
    animal_to_update.name = request_body["name"]
    animal_to_update.species = request_body["species"]
    animal_to_update.age = request_body["age"]

    db.session.commit()
    
    return animal_to_update.to_dict(), 200


@animals_bp.route("/<animal_id>", methods=["DELETE"])
def delete_one_animal(animal_id):
    animal_to_delete = get_valid_item_by_id(animal_id)

    db.session.delete(animal_to_delete)
    db.session.commit()

    return f"Animal {animal_to_delete.name} is deleted!", 200


