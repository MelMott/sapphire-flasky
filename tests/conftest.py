import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.animal import animal

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    #CLOSE DATABASE SESSION
    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
        db.session.remove()
        
    # SET UP A DATABASE AKA ARRANGE PORTION OF TESTING
    # SET UP DATABASE
    with app.app_context():
        db.create_all()
        yield app 

    # CLEAR DATABASE
    with app.app_context():
        db.drop_all()

# CREATE A NEW CLIENT TO SEND OUR REQUESTS
@pytest.fixture
def client(app):
    return app.test_client()

    # POPULATE DATABASE
@pytest.fixture
def three_animals(app):
    animal_one = animal(id=1, name="Furby", species="Cat", age=17)
    animal_two = animal(id=2, name="Gouda", species="cheese monster", age=14)
    animal_three = animal(id=3, name="Foxy", species="flamingo", age=100)

    db.session.add(animal_one)
    db.session.add(animal_two)
    db.session.add(animal_three)

    db.session.commit()