# Readme
- This is a implementation of Image Recognition Application for BU CS655 GENI Project. The user is able to submit an image query from the web interface and the service will use image recognition technique, which classifies the image and returns the answer to the user.
- We implement this project using python, here ```client.py```, ```server.py```, ```classifier.py``` and ```index.html``` are all the code files. ```client.sh``` and ```server.sh``` are automated scripts to set up the dependencies on the server and client nodes. ```rspec.xml``` is the Rspec files to reserve resources on GENI. And folder ```data``` includes files needed for the classifier model.
## Instructions
### Setup
1. Setup the Topology:

   Reserve it from ```rspec.xml```:[rspec.xml](https://raw.githubusercontent.com/lux1997/CS655_grp/main/rspec.xml)

   Or manually create the nodes: add one VM named server, then add one or multiple VM named client (our Rspec uses 5 client nodes), connect each client node with the server node. Then enable public routable ip for the nodes and set any InstaGENI.

2. Server Node:

   Login to the server node, run ```server.sh```, the script will install pip on python3, pytorch, torchvision numpy and PIL and download the server codes from this github repo.

   Then run the server:
   ```
   python3 server.py
   ```
   To run it in background:
   ```
   nohup python3 server.py &
   ```
3. Client Node:

   Login to the client node, run ```client.sh```, the script will install pip on python3, PIL and apache2. You need to run it on each client node.
### How to Run
- If all the setups have finished, visit the address for any client node on your browser to view the web interface. 

- If you use our Rspec, the addresses would be ```http://204.102.244.59/```, ```http://204.102.244.60/```, ```http://204.102.244.62/```, ```http://204.102.244.55/```, ```http://204.102.244.54/```
## Team Members
Xiao Lu, Tianqi Tan, Hao Yu, Zixiang Wei
