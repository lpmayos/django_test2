sudo service neo4j-service stop
sudo rm -rf /var/lib/neo4j/data/graph.db/
sudo cp /vagrant/provisioning/joc_proves.tar.gz /var/lib/neo4j/data/
cd /var/lib/neo4j/data/
sudo tar zxvf joc_proves.tar.gz
sudo rm -f joc_proves.tar.gz
sudo service neo4j-service start
