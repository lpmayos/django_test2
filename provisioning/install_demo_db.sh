sudo service neo4j-service stop
sudo rm -rf /var/lib/neo4j/data/graph.db/
sudo cp /vagrant/provisioning/horadeaventuras.tar.gz /var/lib/neo4j/data/
cd /var/lib/neo4j/data/
sudo tar zxvf horadeaventuras.tar.gz
sudo rm -f horadeaventuras.tar.gz
sudo service neo4j-service start
