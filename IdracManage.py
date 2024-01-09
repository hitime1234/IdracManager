import os
import subprocess, time
import datetime

class IDracManager:
    def __init__(self):
        file = open("idrac","r")
        hold = file.readlines()
        self.ipaddress = hold[0].split("\n")[0]
        self.user = hold[1].split("\n")[0]
        self.passwd = hold[2].split("\n")[0]
        file.close()
    
    
    def powerON(self):
        output = subprocess.getoutput('ipmitool -I lanplus -H ' +  self.ipaddress + ' -U ' + self.user  + ' -P ' + self.passwd + ' chassis power on')
        self.autoMODE()
        time.sleep(10)
        self.changeFanSpeed(12)
        print(output + " : "+ str(datetime.datetime.now()))
        return output

    
    def powerOFF(self):
        output = subprocess.getoutput('ipmitool -I lanplus -H ' +  self.ipaddress + ' -U ' + self.user  + ' -P ' + self.passwd + ' chassis power off')
        print(output + " : "+ str(datetime.datetime.now()))
        return output

    
    def getFanSpeed(self):
        output = subprocess.getoutput('ipmitool -I lanplus -H ' +  self.ipaddress + ' -U ' + self.user  + ' -P ' + self.passwd + ' sensor reading "Ambient Temp" "FAN 1 RPM" "FAN 2 RPM" "FAN 3 RPM"')
        return output
        
            

    def changeFanSpeed(self,PERCENT):
        os.system('ipmitool -I lanplus -H ' +  self.ipaddress + ' -U ' + self.user  + ' -P ' + self.passwd + ' raw 0x30 0x30 0x01 0x00')
        speed =0 
        speed=int(PERCENT)
        if PERCENT > 100 or PERCENT < 1:
            return "THAT IS NOT A VALID RANGE YOU F***ing idiot"
        else:
            wanted_percentage_hex = "{0:#0{1}x}".format(speed, 4)
            os.system('ipmitool -I lanplus -H ' +  self.ipaddress + ' -U ' + self.user  + ' -P ' + self.passwd + ' raw 0x30 0x30 0x02 0xff ' + wanted_percentage_hex)
            return self.getFanSpeed()
        
    
    def autoMODE(self):
        os.system('ipmitool -I lanplus -H ' +  self.ipaddress + ' -U ' + self.user  + ' -P ' + self.passwd + ' raw 0x30 0x30 0x01 0x01')
        return self.getFanSpeed()
    
    def updatefile(self):
        file = open("Idrac","w")
        file.write(self.ipaddress+"\n")
        file.write(self.user+"\n")
        file.write(self.passwd+"\n")
        file.close()
        self.__init__()

    def changeUser(self,Newuser):
        self.user = Newuser
        self.updatefile()
        
    def changePasswd(self,Newpass):
        self.user = Newpass
        self.updatefile()

    def changeIP(self,NewIP):
        self.ipaddress = NewIP
        self.updatefile()
    
        


