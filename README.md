django_test
===========

Small project to play a little bit with **Django** and **Tastypie** with **neo4j** as a db using **neomodel**.

It implements some demo models, and offers interaction with them through a **restful API**


How to use it
-------------

::
  
    $ git clone git@github.com:lpmayos/django_test.git
    $ cd django_test/
    $ vagrant up --provision
    $ vagrant ssh
    vagrant@precise64:/etc/neo4j$ sudo vim neo4j-server.properties
        // uncomment l.16: org.neo4j.server.webserver.address=0.0.0.0
    vagrant@precise64:/etc/neo4j$ sudo service neo4j-service start
    vagrant@precise64:~$ cd /vagrant/
    vagrant@precise64:/vagrant$ source /home/vagrant/4dlife-env/bin/activate
    (4dlife-env)vagrant@precise64:/vagrant$ cd src/
    (4dlife-env)vagrant@precise64:/vagrant/src$ python manage.py runserver 0.0.0.0:8000
    
    Go to you browser and open http://localhost:8000
