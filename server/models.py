from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin  #

db = SQLAlchemy()


# came without migrations filled out
# do they even tell thenm how to run these migrations

#has_many baked goods
# name is string
# price is integer
#created at
# updated at
class Bakery(db.Model, SerializerMixin): ##
    __tablename__ = 'bakeries'

    serialize_rules = ('-baked_good.bakery',)# needs the comma because tuple

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    baked_goods = db.relationship('BakedGood', backref='bakery')

    def __repr__(self):
        return f'<Bakery is {self.name} with {self.id}>'

#belogs_to bakery
# name, created at, udpated at
class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialize_rules = ('-bakery.baked_goods',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

    def __repr__(self):
        return f'<BakedGood ({self.id}) of {self.bakery}/10>'
