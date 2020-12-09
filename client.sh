sudo apt-get update
sudo apt install python3.7
sudo apt install python3-pip
sudo python3.7 -m pip install Pillow
sudo apt-get install apache2
cd /var/www/html
sudo rm index.html
sudo wget https://raw.githubusercontent.com/lux1997/CS655_grp/main/index.html
cd /usr/lib
sudo chmod 777 cgi-bin
cd cgi-bin
sudo wget https://raw.githubusercontent.com/lux1997/CS655_grp/main/client.py
sudo chmod 777 client.py
sudo ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/ 
sudo systemctl restart apache2
