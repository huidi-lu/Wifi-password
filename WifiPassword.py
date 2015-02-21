from subprocess import check_output
import re

name_pattern = re.compile("All User Profile     : (.*)\\r")
auth_pattern = re.compile("Authentication         : (.*)\\r")
pwd_pattern = re.compile("Key Content            : (.*)\\r")
known_networks = re.findall(name_pattern,
                 check_output("netsh wlan show profiles", shell = True))
for ssid in known_networks:
    try:
        temp = check_output("netsh wlan show profiles name= \"%s\" key=clear" % ssid, shell = True)
        print "SSID: "+ssid
        if re.findall(auth_pattern, temp)[0] == "Open":
            print "Open WiFi. No password stored."
        else:
            if re.findall(pwd_pattern, temp) == []:
                print "%s authentification not supported !" % re.findall(auth_pattern, temp)[0]
            else:
                print "Authentification: "+re.findall(auth_pattern, temp)[0]
                print "Password: "+re.findall(pwd_pattern, temp)[0]
        print '\n'
    except:
        print "Unknown error occured when analyzing %s.\n" % ssid

raw_input("Press any key to exit...")





