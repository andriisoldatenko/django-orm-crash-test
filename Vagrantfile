# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "forwarded_port", guest: 80, host: 8018
  config.vm.network :forwarded_port, guest: 22, host: 2213, id: "ssh"
  config.vm.synced_folder ".", "/home/vagrant/pycon/", :nfs => true
  config.vm.synced_folder "./data", "/vagrant_data", :nfs => true
  config.vm.provision :shell, path: 'bootstrap.sh'
  config.vm.provision :shell, path: 'install_postgresql.sh'
  config.vm.provision :shell, path: 'user_install.sh', privileged: false
  config.ssh.forward_agent = true
  config.vm.provider "virtualbox" do |v|
     v.customize ["modifyvm", :id, "--memory", 1024*4]
     v.customize ["modifyvm", :id, "--cpus", 4]
  end
end
