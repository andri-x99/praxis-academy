sudo apt install samba
mkdir /home/a/zamba
nano /etc/samba/smb.conf

#last line
[zamba]
   comment = UBUNTU DRIVERS 
   path = /home/a/zamba          
   browseable = yes
   read only = yes
   guest ok = yes

sudo service smbd restart
sudo smbpasswd -a a(user saya) pass 1

check di windows
