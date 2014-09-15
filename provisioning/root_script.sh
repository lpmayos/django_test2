apt-get update
apt-get -y install git python-virtualenv software-properties-common python-software-properties curl vim
add-apt-repository -y ppa:webupd8team/java
apt-get update

echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
apt-get -y install libxtst6 oracle-java7-installer
apt-get -q -y install oracle-java7-set-default


# neo4j installation (http://www.neo4j.org/download/linux)
# --------------------------------------------------------

# # start root shell
sudo -s
# Import our signing key
wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key add -
# Create an Apt sources.list file
echo 'deb http://debian.neo4j.org/repo stable/' > /etc/apt/sources.list.d/neo4j.list
# Find out about the files in our repository
apt-get update
# Install Neo4j, community edition
apt-get -y install neo4j

cp /vagrant/provisioning/neo4j-server.properties /etc/neo4j
chown neo4j.adm /etc/neo4j/neo4j-server.properties
