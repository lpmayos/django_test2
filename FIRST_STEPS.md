# Scrapbook for neo4jmodel, Neo4j and CYPHER

Meant to be used from the python shell:

```
$ cd /vagrant/src
$ ./manage.py shell_plus
```

## neomodel

** imports **

```python
from adventure_time.models import World, Location, User
from adventure_time.serializers import WorldSerializer, LocationSerializer, UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
```

** listing objects **

```python
world_category = World.category()
worlds = world_category.instance.all()

location_category = Location.category()
locations = location_category.instance.all()

user_category = User.category()
users = user_category.instance.all()
```

** creating objects **

```python
w1 = World(id='1', name='world B', world_type='type B', surface=7652, creation_date='2014-08-12T00:00')
w1.save()

l1 = Location(location_id='1', name='location A', coordinates='-1,3')
l1.save()

u1 = User(user_id='1', name='user 1')
u1.save()
```

** relating objects **

```python
loc1.world.connect(w1)

w1.location.connect(l1)
```

** getting objects info **

```python
users[0].world.all()
    --> [<adventure_time.models.World object at 0x35e9f50>]

serializer = WorldSerializer(world1)
```

** clear db **

Execute 
```
$ dropneo4jdb.sh
```


## NEO4J FIRST STEPS

** clear database **
```
vagrant@precise64:~$ dropneo4jdb.sh
```

Open your favorite browser (it's Chrome, isn't it?) and point it to http://localhost:7474/

** create nodes **
```
CREATE (n:Person { name : 'Andrés', surname: 'Canta Raro', title : 'artist' })
CREATE (n:Person { name : 'Jesús', title : 'Developer' })
```

** create relationships **
```
MATCH (a:Person {name: 'Andrés'}),(b:Person {name: 'Jesús'})
CREATE (a)-[r:RELTYPE]->(b)
RETURN r
```

** set properties **
```
MATCH (n { name: 'Jesús' })
SET n.surname = 'Tomás Dado'
RETURN n
```
