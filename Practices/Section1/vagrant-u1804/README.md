# Platforms
Windows, Linux, Intel Mac.

Arm MacOS - sorry, but not yet.

# Checkout the Repo

Please checkout this repo:
```
git clone git@github.com:ask4ua/DKN.git
```
and naviaget to the folder inside:
```
Practices/Section1/vagrant-u1804/
```

# Install Virtualbox
On Windows: install VBox 7.0: https://download.virtualbox.org/virtualbox/7.0.22/VirtualBox-7.0.22-165102-Win.exe

On Intel Mac: install VBox 7.0: https://download.virtualbox.org/virtualbox/7.0.22/VirtualBox-7.0.22-165102-OSX.dmg

On Linux: https://download.virtualbox.org/virtualbox/7.0.22/

Arm MacOS only 7.1+ https://www.virtualbox.org/wiki/Downloads

# Install Vagrant
Windows, Linux, Intel Mac : https://releases.hashicorp.com/vagrant/2.4.1/

Linux (ubuntu):
```
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vagrant
```

Arm MAC OS:
```
/opt/vagrant/embedded/gems/gems/vagrant-2.4.1/plugins/providers/virtualbox/driver/meta.rb

$ diff -u meta.rb.orig meta.rb
--- meta.rb.orig        2024-09-16 11:37:37.017440100 +0100
+++ meta.rb     2024-09-16 11:33:51.312254400 +0100
@@ -69,6 +69,7 @@
             "6.0" => Version_6_0,
             "6.1" => Version_6_1,
             "7.0" => Version_7_0,
+            "7.1" => Version_7_0,
           }

           if @@version.start_with?("4.2.14")

brew tap hashicorp/tap
brew install hashicorp/tap/hashicorp-vagrant
```

# 1 or 3 VMs
the count is selected by the NUM_VMs var. 1 by default.
Windows powershell
```
$env:NUM_VMS = 3;
```

Mac OS/linux:
```
export NUM_VMS=3
```

Don't forget to set one always before work (especially after reboot)!

# Start
```
vagrant up
```

# Status
```
vagrant status
```

# CLI Connect
```
vagrant ssh vm1
```
```
vagrant ssh vm2
```
```
vagrant ssh vm3
```

## Ports forwarded Out of The Box
Use on your local machine in browser/SQL addresses like:
```
http://127.0.0.1:8080 - for port 8080 of the VM1
http://127.0.0.1:8180 - for port 8080 of the VM3
```

Forwarding from the hoster:
```
For ex.:
127.0.0.1:8180 -> vm1:8080
127.0.0.1:8181 -> vm1:8081
127.0.0.1:8182 -> vm1:8082
127.0.0.1:5132 -> vm1:5432

127.0.0.1:8280 -> vm2:8080
127.0.0.1:8281 -> vm2:8081
127.0.0.1:8282 -> vm2:8082
127.0.0.1:5232 -> vm2:5432
etc.
```

Intercommunication:
vm1-3: 192.168.56.11-13

```
For ex.:
vm1 -> vm2 8080: 192.168.56.12:8080
vm1 -> vm2 8081: 192.168.56.12:8081
vm1 -> vm2 8082: 192.168.56.12:8082

vm1 -> vm3 5432: 192.168.56.13:5432
etc.
```

# Shutdown
```
vagrant halt
```

# Destroy
```
vagrant destroy
```

# Remove totally
Unix world
```
rm -rf .vagrant
```
Windows:
```
rm .vagrant -r -force
```
