cd ~
virtualenv 4dlife-env
cd /vagrant/
source /home/vagrant/4dlife-env/bin/activate && pip install -r requirements.txt
mkdir -p /home/vagrant/bin/
cp /vagrant/provisioning/dropneo4jdb.sh /home/vagrant/bin/dropneo4jdb.sh
chmod 744 /home/vagrant/bin/dropneo4jdb.sh
cp /vagrant/provisioning/install_demo_db.sh /home/vagrant/bin/install_demo_db.sh
chmod 744 /home/vagrant/bin/install_demo_db.sh
cp /vagrant/provisioning/install_joc_proves.sh /home/vagrant/bin/install_joc_proves.sh
chmod 744 /home/vagrant/bin/install_joc_proves.sh
