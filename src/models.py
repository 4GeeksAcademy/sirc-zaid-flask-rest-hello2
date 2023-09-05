from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(80), unique=False, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.password,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            # do not serialize the password, its a security breach
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "passengers": self.passengers,
            # do not serialize the password, its a security breach
        }

class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Starships %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "passengers": self.passengers,
            # do not serialize the password, its a security breach
        }
    
class Favorites(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))

    usuario = db.relationship(User)
    planets = db.relationship(Planets)
    people = db.relationship(People)
    vehicles = db.relationship(Vehicles)
    starships = db.relationship(Starships)

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        planetaInfo = Planets.query.filter_by(id= self.planet_id).first()
        charactersInfo = People.query.filter_by(id= self.people_id).first()
        vehiclesInfo = Vehicles.query.filter_by(id= self.vehicle_id).first()
        starshipsInfo = Starships.query.filter_by(id= self.starships_id).first()

        return {
            "id": self.id,
            "user_id": self.user_id,
            "planeta": None if planetaInfo is None else planetaInfo.serialize(),
            "characters": None if charactersInfo is None else charactersInfo.serialize(),
            "vehicles": None if vehiclesInfo is None else vehiclesInfo.serialize(),
            "starships": None if starshipsInfo is None else starshipsInfo.serialize(),
            # do not serialize the password, its a security breach
        }
