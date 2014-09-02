from neomodel import StructuredNode, StringProperty, IntegerProperty, DateTimeProperty, RelationshipTo, RelationshipFrom, StructuredRel, One
from datetime import datetime
import pytz


class FriendRel(StructuredRel):
    since = DateTimeProperty(default=lambda: datetime.now(pytz.utc))
    met = StringProperty()


class World(StructuredNode):
    name = StringProperty(unique_index=True)

    # traverse incoming IS_FROM relation, inflate to Person objects
    inhabitant = RelationshipFrom('Character', 'LIVES_IN')


class Character(StructuredNode):
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    friends = RelationshipTo('Character', 'FRIEND', model=FriendRel)
    enemies = RelationshipTo('Character', 'ENEMY', model=FriendRel)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    world = RelationshipTo(World, 'LIVES_IN', cardinality=One)
