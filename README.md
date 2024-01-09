# IdracManager
This is a python class. That controls idracs. Allowing you to issue start/stop and fan control commands 
# required software

Ipmitool - in path 

# required modules:
os

subprocess

time

datetime

# how to use :3

import IdracManage

Idrac = IdracManage.IDracManager()

(make sure you create a file called idrac with username and password for your idrac)

# file format "idrac" 

ip address of Idrac controller

username

password

# fan speed changing

Idrac.changeFanSpeed(int: percentage) 

- must be a integer between 0 or 100 or you will be told off by it
- This disables automode 

Idrac.autoMODE() - This Reenables IDrac's automatic fan control

# Idrac.updatefile()

Allows you to update  old stored password and user and ip address with a current one running 

Idrac.changePasswd(Str: Pass) - changes password

Idrac.changeUser(Str: User) - changes user

Idrac.changeIP(str: ip) - changes ip of where commands are sent

# notes about startup and stopping

Idrac.powerON()

In my setup. I don't like how loud r710 can get on inital startup of server. So to fix this the script sets fan speed to 12% manually few seconds after startup.
To use automode after start up just Do 
- you can remove this by removing self.changeFanSpeed(12) in poweron

# feel free to raise any issues or pull request any additional features to be added.


this is used for my r710 Idrac 6 controller. So it may not work with other Idrac controllers if Ipmit isn't enabled.

Thank youuu :3



