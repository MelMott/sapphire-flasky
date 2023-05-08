from app import db

class Sanctuary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    animals = db.relationship("Animal", back_populates="Sanctuary")

    # no animal_id stored here because it's not many to many relationship

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name
        }
    
    @classmethod
    def from_dict(cls, sanctuary_details):
        new_sanctuary = cls(
            name=sanctuary_details["name"],
            species=sanctuary_details["species"],
            age=sanctuary_details["age"]
        )
        return new_sanctuary