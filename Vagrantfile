# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 7474, host: 7474

  config.vm.provision "shell" do |s|
    s.path = "provisioning/root_script.sh"
  end

  config.vm.provision "shell" do |s|
    s.privileged = false
    s.path = "provisioning/vagrant_script.sh"
  end
end
