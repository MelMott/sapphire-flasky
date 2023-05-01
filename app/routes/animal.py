from flask import Blueprint, jsonify, abort, make_response

class Animal():
    def __init__(self, id, species, name, habitat):
        self.id = id
        self.species = species
        self.name = name
        self.habitat = habitat

# sapphire_animals = [
#     Animal(1, "Anaconda", "Nikki Minaj", "Jungle"),
#     Animal(2, "Elephant", "Dumbo", "Our childhood!!!"),
#     Animal(3, "Unicorn", "Not Charlie", "Youtube")
# ]

def validate_animal(animal_id):
    try:
        animal_id = int(animal_id)
    except:
        abort(make_response({'msg': f"Invalid id '{animal_id}'"}, 400))

    animal = Animal.query.get(animal_id)

    return animal if animal else abort(make_response({'msg': f"No animal with id {animal_id}"}, 404))



# All routes defined with animals_bp start with url_prefix (/animals)
animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

@animals_bp.route("", methods=['GET'])
def handle_animals():
    # all_animals is a list of Animal instances! We should use them as Animal instances, and access their values via .
    all_animals = Animal.query.all()
    animals_response = []
    for animal in all_animals:
        animals_response.append(animal.to_dict())
    return jsonify(animals_response), 200

@animals_bp.route("/<animal_id>", methods=["GET"])
def handle_animal(animal_id):
    animal = validate_animal(animal_id)
    return {
        "id": animal.id,
        "name": animal.name
    }, 200

@animals_bp.route("", methods=['POST'])
def create_animal():
    # Get the data from the request body
    request_body = request.get_json()

    # Use it to make an Animal
    new_animal = Animal(name=request_body["name"])

    # Persist (save, commit) it in the database
    db.session.add(new_animal)
    db.session.commit()

    # Give back our response
    return {
        "id": new_animal.id,
        "name": new_animal.name,
        "msg": "Successfully created"
    }, 201
