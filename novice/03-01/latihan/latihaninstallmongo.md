#INSTALL MONGO
```
apt-get install gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
apt-get update
apt-get install -y mongodb-org 
```
#Before Start Mongo
root@aa:~# mkdir /data/db -p (biar ada penampungan databasenya)
root@aa:~# mongo

#Start Mongo with 2 Terminal
terminal 1 : mongod 
terminal 2 : mongo --port 27017
