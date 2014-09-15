from adventure_time.models import World, Character
import random
i = 1
for i in xrange(2):
    world = World(pk="w%d" % i, name="W%d" % i)
    world.save()
    for j in xrange(10):
        caracter = Character(pk="c-%d-%d" % (i, j), name="C-%d-%d" % (i, j), age=random.randint(5, 100))
        caracter.save()
        world.inhabitant.connect(caracter)
        if j > 1:
            for k in xrange(j):
                car = Character.nodes.get(pk="c-%d-%d" % (i, k))
                if random.randint(1, 10) < 5:
                    car.friends.connect(caracter)
                else:
                    car.enemies.connect(caracter)
