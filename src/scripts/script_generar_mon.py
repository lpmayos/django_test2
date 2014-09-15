from adventure_time.models import World, Character
import random
import datetime


def create_world(id_world):
    print "CREATING WORLD: %s" % id_world
    world = World(pk="w%d" % id_world, name="W%d" % id_world)
    world.save()
    return world


def create_character(world, id_char):
    print "CREATING CHARACTER: %s" % id_char
    caracter = Character(pk="c-%s-%d" % (world.pk, id_char), name="C-%s-%d" % (world.pk, id_char), age=random.randint(5, 100))
    caracter.save()
    world.inhabitant.connect(caracter)
    return caracter


def create_relationship(a_char, another_char):
    print "CREATING RELATIONSHIP: %s with %s" % (a_char.pk, another_char.pk)
    if random.randint(1, 10) < 5:
        a_char.friends.connect(another_char)
    else:
        a_char.enemies.connect(another_char)


def main():
    ini = datetime.datetime.now()
    NUM_MONS = 100
    NUM_HABITANTS = 1000
    NUM_RELACIONS = 50
    worlds = []
    for i in xrange(NUM_MONS):
        worlds.append(create_world(i))

    chars = []
    for j in xrange(NUM_HABITANTS):
        un_mon = worlds[random.randint(0, NUM_MONS - 1)]
        chars.append(create_character(un_mon, j))

    for k in xrange(NUM_HABITANTS):
        for l in range(NUM_RELACIONS):
            create_relationship(chars[k], chars[random.randint(0, NUM_HABITANTS - 1)])
    fi = datetime.datetime.now()

    print "Temps execució: %s" % ((fi - ini) / 1000)


main()
