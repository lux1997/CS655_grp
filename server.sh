sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install numpy
sudo pip3 install pillow

sudo pip3 install --no-cache-dir torch
sudo pip3 install --no-cache-dir torchvision

wget https://raw.githubusercontent.com/lux1997/CS655_grp/main/server.py
wget https://raw.githubusercontent.com/lux1997/CS655_grp/main/classifier.py

mkdir data
cd data
wget https://raw.githubusercontent.com/lux1997/CS655_grp/main/data/imagenet_classes.txt
wget https://raw.githubusercontent.com/lux1997/CS655_grp/main/data/imagenet_synsets.txt
cd ..
