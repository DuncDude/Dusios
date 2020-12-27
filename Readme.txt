Thank You for Using my Software
For more software and information vist my GitHub https://github.com/DuncDude

DUSIOS
------------------------------
From Wikipedia, the free encyclopedia
In the Gaulish language, Dusios was a divine being among the continental Celts who was identified 
with the god Pan of ancient Greek religion and with the gods Faunus, Inuus, Silvanus, and Incubus of 
ancient Roman religion. Like these deities, he[ might be seen as multiple in nature, and referred to
in the plural (dusioi), most commonly in Latin as dusii. Although the Celtic Dusios is not described
in late-antique sources independently of Greek and Roman deities, the common functionality of the
others lay in their ability to impregnate animals and women, often by surprise or force.
So your interested in hacking wifi (legally)? Then you've come to the right place. Dusios is a tool 
made to help automate the process. Dusisos is based off using other popular tools such as NMAP, HAshCat,
Reaver etc and allow use and customastion from a user friendly dashboard without typing lots of 
commands. HOwever you might want to have at least an entry level idea of wireless networks before 
configuring any options, but the process should be fairly user friendly regardless. 


FAQ
------------------------------
What is Dusios? Dusios is a menu driven program written in python2 to help automate and improve common
tactics of cracking Wifi network, along with basic network analysis, firewall settings, and a few other 
tricks.
Why/how did I make this? When I was beginning to have an interest in computer security a lot of my 
learing barriers manifested in my inability to type well or remember what commands I was supposed to be
typing, and as I learned how to do more with more tools I decided I wanted a way to get around the 
aforementioned barriers. That along with the start of covid and lots of newly found free time I automated 
in python the commands I would use a lot or a little (so I wouldn't have to remember them) MOst commands 
extensions established and respected programs such as NMAP or AirMOn etc (they are the real heros). This
became Dusios, the project became fun and a self test for my code writing abilities and involved more as 
I learn more.

What's this website? At some point I wanted to be able to access my notes and tutorials I wrote, from within 
the shell (incase thats all thats available) so I wrote a readme divided into chapters that could be read
from within Dusios. I've found DUsios quite useful as a tool for testing and learning. I hoped to share that 
with the world so I made this website. Originally I wrote a lot of these tutorials for the in Program 
accessible library as notes for myself, doing so I used a lot of info from other authors thinking only i'd be
reading it, to go back now and try to find what I used would be ALOT, but I do want to give credit to them if
they claim it.(NUllbyte.com was used and are amazing) Have Fun! 

Install
-------------------------------
Install
-------------------------------
In order to install Dusios you will need a computer running Linux, Debian distros such as KALI and Ubuntu 
have been tested on and work well.
You will also need to be running Python2 which you can install by opening a terminal session and typing
"sudo apt install python2" 
"sudo apt install python2"
"sudo apt install python3"

Anything else that needs to be downloaded is done by Dusios when you select the update option from the main screen.
Once you've downloaded the link unzip the file, and navigate to the folder Dusios is in via the Linux 
command line. launch Dusios using the command
"python Dusios.py"(note the .py file may be Dusios8.py or Dusios10.2.py etc just fill that in accordingly)

Dusios will then run and create the nesscary folder and diretories, when that is complete you should 
select option "6" from the top menu to update your computer, install necsarry libraries, and even
basic password lists!

if you run into any problems consider running Dusios as "sudo" (ie; sudo python Dusios.py)

Updating Your Computer!
-------------------------------
In order to use Dusios you will need to have the correct libraries installed. Choose the update 
option from the top menu for an automated update. If you run into problems try running Dusios as sudo
When you update through Dusios the first time it will install all the necessary software to run 
properly. If you're running Kali most of this software will already be preinstalled.
This update will also download various Password Lists and USername lists which may take a little while longer.

Choosing your Wifi Interface
-------------------------------
Dusios is designed as basic toolkit with wifi cracking in mind, because of this there is constant need 
for use of your wifi card, in order for Dusios to run proper we need to know which wifi interface it 
should run, chances are its not the default set by Dusios. However we can select the card to use by 
selecting the "[3]. Change Wifi interface" from the wifi Home menu, You will be shown a list of 
interfaces on your computer chances are its will be call "wlan0" or something of the like. in most cases
it will be whatever is next to the broadcast Enter the appropriate name for your setup. IN the example 
below "wlp5s0" is the name of my wireless card. 

Advance User Mode
------------------------------
Dusios is based off of using other programs and scripts and having the options and commands pre typed, 
this it what makes it ideal to new users. But what if you want to have a better understanding or use 
varitons of the same command? Well you could definintly go ahead and just use those programs without
Duisos, or if you want to theres is an Advance mode option built into almost all Dusios that allows you 
to modify and view each task it does. If you look at the top of the screen when you launch Duisos you 
will see 3 items.Interface, Monitor Mode, and Adv-Mode The interface shows which wireless interface 
Dusios is set to use, the Monitor mode will show weither or not that same wireless card is set to moniter
mode, and finally advance mode will show you if you've turned on adavance mode. 

To enable Advance mode got to the Home screen as seen above and select the "Advance Options" enter "1" 
on the next prompt and hit Enter. At the top of the screen you should see that Advance Mode is set to
"On". you can test this by going to the WIfi Home screen and selecting option 1 from the menu to put 
your wifi card into monitor mode, you should see a print out of what command will be used, which you 
can choose to retype and edit to your whim or leave blank and let the default command run.

Setting up your WiFi card
-------------------------------
You will need to have your Wifi card set up to listen and interact with other networks so go ahead 
and select the "Set wifi adapter to Monitor mode" option. If you receive an error than you may need 
to change the default option of which Wireless Interface is going to be used you can do this by 
selecting the Change Wifi interface" in the Wifi Home page, where you'll be shown a list of all 
interfaces on your computer (its most likely wlan0 or wlanp) 

View Networks around you
--------------------------------
In order to attack a network you're going to need to choose your target. Once your WiFi card is 
set to monitor networks around you select the "View active networks in the area" option from the menu.
You will be shown all local networks around you, it will look something like this: 
 BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH WPS     ESSID
                                                                                                                                                                                                           
 9C:DC:D4:5A:E1:28  -68        2        0    0  11  54e. OPN                      HP-Print-28-Officejet 4630                                                                                               
 C8:B4:28:F5:2A:E5  -62        2        0    0   5  54e. WPA2 CCMP   PSK          OurTarget                                                                                                      
 U0:22:03:86:6A:15  -47        9        3    0   8  54e  WEP  CCMP   PSK  Locked  ATT8b2UHT4                                                                                                               
 80:28:94:CC:PE:E8  -69        2        0    0   1  54e  WPA  CCMP   PSK  1.0     Meg                                                                                                                 
 34:6I:4V:5D:F7:62  -67        3        0    0   1  54e. WPA2 CCMP   PSK          AstonButts                                                                                                            
                                                                                                                                                                                                            
 BSSID              STATION            PWR   Rate    Lost    Frames  Probe                                                                                                                                  
                                                                                                                                                                                                            
 (not associated)   D8:31:34:4F:62:8C  -90    0 - 6      0        5  ATT523C7s2
 C8:B4:22:F5:2A:E5  P5:31:34:7F:62:3C  -88    0 - 6      0        5  TargetPC

We have a few things going on here let's break down each column starting backwards from right to left.

ESSID is the human readable name of networks around you or AP (Access Points) the names are a bit cut 
off here but they would be something akin to "grandmas Wifi, or the jonesConnect".

WPS (Wifi Protected Setup) is a network security standard to create a secure wireless network made in 
the mid 2000's. Now though it's viewed as a security risk and can be cracked on older routers. If "1.0"
appears under the WPS column, that ESSID router in the same row has a chance for a WPS attack using Reaver.

AUTH is the kind of authentication used to login a network. If the network is open this column will 
remain blank. You will likely see PSK or PRe-Shared Key(the password) is a client authentication 
method that uses a string of 64 hexadecimal digits, or as a passphrase of 8 to 63 printable ASCII 
characters, to generate unique encryption keys for each wireless client. PSK is one of two available
authentication methods used for WPA and WPA2 encryption on Juniper Networks wireless networks. PSK
is no longer the default authentication method when creating a WLAN Service profile because the 
other choice, 802.1X authentication, is the standard and is stronger.

CIPHER Standard security ciphers are part of both WPA and WPA2 encryption. You choose whether you 
want to apply either the newer CCMP, or TKIP (an upgrade of original WEP programming), or both for
each WLAN Service profile. Both cipher suites dynamically generate unique session keys for each 
session and periodically change the keys to reduce the likelihood of a network intruder intercepting 
enough frames to decode a key. This may be a bit much for beginner.

ENC short for encryption shows what kind of encryption the network uses, lets go over the basics 
of what kind of networks you'll probably see.

OPN = open, no encryption.

WEP was the original security algorithm for IEEE 802.11 wireless networks, introduced as part of the
original 802.11 standard.

WPA addressed the vulnerabilities of WEP, the original, less secure 40 or 104-bit encryption scheme
in the IEEE 802.11 standard. WPA also provides user authentication—WEP lacks any means of authentication.

WPA2 is the certified version of the full IEEE 802.11i specification. Like WPA, WPA2 supports either
IEEE 802.1X/EAP authentication or PSK technology. It also includes a new advanced encryption 
mechanism using the Counter-Mode/CBC-MAC Protocol (CCMP) called the Advanced Encryption Standard (AES).

MB or Maximum speed supported by the AP. If MB = 11, it's 802.11b, if MB = 22 it's 802.11b+ and up to
54 are 802.11g. Anything higher is 802.11n or 802.11ac. The dot (after 54 above) indicates a short 
preamble is supported. Displays “e” following the MB speed value if the network has QoS enabled.

CH is the channel number the networks operate on.

#/s Number of data packets per second measure over the last 10 seconds

#Data Number of captured data packets (if WEP, unique IV count), including data broadcast packets.

BEACONS Number of announcements packets sent by the AP. Each access point sends about ten beacons per 
second at the lowest rate (1M), so they can usually be picked up from very far.

PWR or power of signal. Signal level reported by the card. The '-' in front of the number does not 
imply a negative pwr, for example -58 is more powerful than -34. The closer you are to the source the 
higher the PWR is. Its signification depends on the driver, but as the signal gets higher as you get 
closer to the AP or the station. If the BSSID PWR is -1, then the driver doesn't support signal level 
reporting. If the PWR is -1 for a limited number of stations then this is for a packet which came from 
the AP to the client but the client transmissions are out of range for your card.

and finally BSSID MAC address of the access point. A MAC address is a world wide unique id number 
given to hardware. In the Client section, a BSSID of “(not associated)” means that the client is not 
associated with any AP. In this unassociated state, it is searching for an AP to connect with.


Now below the listing of Routers or AP's there is a list of Devices or Nodes, computers, phones, etc.
Let's go over those columns from right to left as well

PROBE is just the name of the Device.

RATE Station's receive rate, followed by transmit rate. Displays “e” following each rate if the network 
has QoS enabled.

STATION is the MAC address of the target device

BSSID is the MAC address of each associated station (that is which ROuter or AP its connected to) or 
stations searching for an AP to connect with. Clients not currently associated with an AP have a BSSID 
of “(not associated)”.

PWR is the same as for the Routers or AP's


Choosing a Target and an Attack
-------------------------------
Looking at all this information also called Intelligence Gathering, we're able to pick and choose the 
best targets. Of course you should only operate on networks you're allowed to use. A few things you 
should be using to judge which network you want to attack might be: PWR you're going to want to make sure
that you have a relatively good signal for any network you're attacking. ENC: This is important, if the 
encryption is WEP it may only take seconds to break it vs WPA and WPA2 which would be more difficult to hack.

Depending on what kind of attack you are going to use you should looks at what kind of PROBEs or Devices 
are around If you are using a HANDSHAKE capture then you will want at least one PROBE connected to the 
AP that you wish to attack.
In the example above and below the "TargetPC" is connected to the "OurTarget" network.

 BSSID              STATION            PWR   Rate    Lost    Frames  Probe                                                                                                                                  
                                                                                                                                                                                                            
 (not associated)   D8:36:34:4F:62:8C  -90    0 - 6      0        5  ATT523C7s2
 C8:B4:82:F5:2A:E5  Y8:39:34:4F:62:8C  -88    0 - 6      0        5  TargetPC
     ^
	 |
Same MAC or BSSID of the "OurTarget" network or AP. The "ATT523C7s2" is not connected to any network.

If the WPS column has "1.0" then you may want to consider using a WPS Reaver attack, which can either be 
quite quick or a couple hours long. These attacks are becoming less effective as router companies are 
making routers that resist this type of exploit.

WPA/WPA2 Capturing Handshakes to Crack
-------------------------------
The weakness in the WPA2-PSK system is that the encrypted password is shared in what is known as the 4-way
handshake. When a client authenticates to the access point (AP), the client and the AP go through a 4-step 
process to authenticate the user to the AP. If we can grab the password at that time, we can then attempt to 
crack it. In order to capture a HANDSHAKE we'll need a network with a NODE or device attached, both AP and Device
should have relatively high signal strength. This attack may not work unless you're within the house or business!
For this example we'll use the Router(AP) OurTarget with the attached Device C8:B4:22:F5:2A:E5. 

 BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH WPS     ESSID
                                                                                                                                                                                                           
 9C:DC:D4:5A:E1:28  -68        2        0    0  11  54e. OPN                      HP-Print-28-Officejet 4630                                                                                               
 C8:B4:28:F5:2A:E5  -62        2        0    0   5  54e. WPA2 CCMP   PSK          OurTarget                                                                                                      
 U0:22:03:86:6A:15  -47        9        3    0   8  54e  WEP  CCMP   PSK  Locked  ATT8b2UHT4                                                                                                               
 80:28:94:CL:PE:E8  -69        2        0    0   1  54e  WPA  CCMP   PSK  1.0     Meg                                                                                                                 
 34:6I:4V:5D:F7:62  -67        3        0    0   1  54e. WPA2 CCMP   PSK          AstonButts                                                                                                            
                                                                                                                                                                                                            
 BSSID              STATION            PWR   Rate    Lost    Frames  Probe                                                                                                                                  
                                                                                                                                                                                                            
 (not associated)   D8:31:34:4F:62:8C  -90    0 - 6      0        5  ATT523C7s2
 C8:B4:22:F5:2A:E5  P5:31:34:7F:62:3C  -88    0 - 6      0        5  TargetPC
 
So now that we have a target lets set up Dusios to listen for handshakes. In a new window or tab reopen DUSIOS 
and go back through the WiFi home page and set your card into monitoring mode., then go to the Capture Handshake
option for the menu and fill in the required fields(you should be getting the hang of this now:) ) 

But how are we going to capture a HandShake if the device is already connected? you ask. Well that's where we 
use a DEAUTH ATTACK. In a new window or tab reopen DUSIOS and go back through the WiFi home page and set your 
card into monitoring mode. Then select the "Deauth Attack" option from the menu and follow the prompts. It may 
take a few tries to properly boot a Device off a network, so up the amount of attacks and attempts till you get 
a result. While your attack is running switch to the other Dusios screen where you set it to listen for HandShakes.
You will know when the Device is kicked and and a HandShake is captured by an Alert, once you've captured a 
HandShake you can stop the Deauth attack. The captured handshake will be saved in a ".cp" file ex 2341.cp in the
handshakes folder, the larger the number the more recent the handshake captured.

to CRACK THE HANDSHAKE you will need to navigate to the "Crack Handshake" part of the menu. Before this In the 
folder where you are running DUSIOS there will be your .cp file but you will also need a list of passwords to 
check against the handshake. From there follow the prompts and in time if a Password matches you've cracked the
WIFI! Larger password list take longer but are more effective. Experiment with different lists! 

WPS/WPA Reaver AttacK
-------------------------------
A very easy attack to initiate but may take some time. Most networks will now be running the much more robust 
WiFi Protected Access (WPA), with WEP running mainly on the older systems that haven’t been updated or maintained
But while it’s not as trivial as breaking into a WEP network, WPA is not completely infallible. Here we will take 
a look at one of the methods used to crack into a WPA network, and some of the pitfalls you may encounter. On the 
surface, this is a very clever feature. It allows less savvy users to establish a secure connection between their 
devices quickly and easily, and as it requires physical access to the hardware, it would seem relatively secure. 
But a tool called Reaver has been designed to brute-force the WPA handshaking process remotely, even if the physical
button hasn’t been pressed on the access point. While some newer devices are building in protection against this 
specific attack, the Reaver WPS exploit remains useful on many networks in the field. GO ahead and run your card 
in Monitor mode to see and look for targets around you. 

BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH WPS     ESSID
80:28:94:CL:PE:E8  -69        2        0    0   1  54e  WPA2  CCMP   PSK  1.0     Meg 


To Start we'll use the "Meg" network from the top example. We can see it will have a chance of success on 
this target because it has WPS enabled "1.0" its signal strength is fairly high, and it uses WPA2 encryption which
is fairly weak. Select the "WPS Reaver attack" from the menu, it will prompt for the BSSID of the AP in this
example the BSSID of "Meg" is "80:28:94:CL:PE:E8". You'll then be asked "Would you like to conduct a Pixie 
Attack (a quick common pin check)? y/n:" that parts up to you. Reaver will then start its attack and within minutes
to hours you may have found the password. Press ctrl+c to stop the attack at any time.


WEP Cracking
--------------------------------
WEP, or Wired Equivalent Privacy, was implemented in 1995 to provide the same expectation of privacy as on 
wired networks for users of Wi-Fi but had security problems that came to light shortly after. It was 
deprecated in 2004, superseded by the WPA and WPA2 encryption that you see today. The reason for this was 
a series of increasingly devastating attacks against the encryption used in WEP, resulting in the ability 
to recover the password in a matter of minutes WEP is a stream cipher which relies on never using the same
key twice to provide security. Unfortunately, as demonstrated in several published attacks, an attacker 
is easily able to force the same key to be used twice by replaying network traffic in a way that forces 
a tremendous amount of packets to be generated. This allows an attacker to collect the data needed to 
determine the encryption key and crack the network password outright. With good range and a powerful 
network adapter, anyone can expect to crack WEP networks in only a few minutes. 

The power behind WEP hacking comes from two different parts of the attack: the ability to stimulate traffic even 
from a busy network and the ability to crack the network password when collecting a certain amount of that 
traffic. Remember that with WPA, hackers can't even capture a handshake from an empty network, but even an empty 
WEP network can be attacked with packet injection.

After finding the network you wish to attack which we find by looking at ENC column for WEP, for example 

BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH WPS     ESSID
U0:22:03:86:6A:15  -47        9        3    0   8  54e  WEP  CCMP   PSK  Locked  ATT8b2UHT4

Navigate to the "WEP cracking option and simply follow the prompts. The crack should be finished within 
20 mins Its that easy! !

Cloning MAC to bypass paywalls
--------------------------------
Lots of hotels airports and coffee shops have wifi that you can connect to but have to go through a paywall or 
an id check to use. Because these networks are open to connect to intaily we can spoof who the router thinks 
we are and act like a computer that's already logged in. But what Is A MAC Address?

The MAC address is usually assigned by the manufacturer of a Network Interface Controller (NIC), and it is 
stored in the hardware. The NIC is a computer circuit card that allows a computer to connect to a network. During
network communication the Address Resolution Protocol (ARP) for the Internet Protocol Version 4 (IPv4) or the 
Neighbor Discovery Protocol (NDP) for IPv6 translates the IP into a NIC.

The MAC address is formed in accordance to the rules of the three numbering name spaces, which are managed by the
Institute of Electrical and Electronic Engineers (IEEE). The format is six sets of two digits or characters, 
separated by hyphens. An example of a MAC address is 30-65-EC- 6F-C4-58.

Some manufacturers, such as Dell, place a unique identifier in the MAC address, which is called the 
Organizationally Unique Identifier (OUI), and identifies the manufacturer. The OUIs of some well-known firms are:

Dell: 00-14-22,
Cisco: 00-40-96,
Nortel: 00-04-DC.

Some firms may have more than one MAC address.
What Is A MAC Address Used For?

One of the applications of MAC addresses is in the filtering process on wireless networks. In order to prevent
strangers from accessing a network, the router is set to accept only specific MAC addresses. In this manner, 
if the IP address changes, as for example in the case of dynamic IP addresses, the MAC address can still identify 
the device.

Filtering can be used to track network users, and to limit their access. It can also have other uses, such as 
identifying when a stolen device connects to the network. For these reasons, many companies and institutions 
require the MAC addresses of their members’ devices. Therefore, it is important for device owners not to reveal
their MAC addresses to anyone, except to authorized personnel.

In order to choose a computer to mimic we must find a computer on the network you are using. SO go ahead and 
choose option one to set your wifi card to monitor mode, then select the option "2" from the wifi Home Menu. 
After awhile you should see some networks and presumably the one you were looking for. In the list of connected 
devices or nodes you should see some that are currently connected to the Network that you want to connect to, go 
ahead and copy one of those Devices MAC it should be a unique number on the screen. Once you've done that, you 
can go back to the wifi home page and select option "4" to return your wifi card to normal status. Once your wifi 
card is operating again select option "11" from the wifi home page to be prompted for a new MAC address, if you 
leave it blank it will generate a random address (this can be useful in hiding your tracks), 

enter the MAC address you want to clone and you should see a confirmation notice. NOw try logging into the wifi 
you wish to join and if all above worked successfully you should have bypassed the paywall or login. note : sometimes
this takes a few tries and you may want to try different MACs on the network to spoof. 

PMKID Cracking
--------------------------------
Cracking the password for WPA2 networks has been roughly the same for many years, but a newer attack requires 
less interaction and info than previous techniques and has the added advantage of being able to target access points
with no one connected. The latest attack against the PMKID uses Hashcat to crack WPA passwords and allows hackers 
to find networks with weak passwords more easily.

A New Method of Password Cracking
Rather than relying on intercepting two-way communications between Wi-Fi devices to try cracking the password, 
an attacker can communicate directly with a vulnerable access point using the new method. On Aug. 4, 2018, a post on 
the Hashcat forum detailed a new technique leveraging an attack against the RSN IE (Robust Security Network Information
Element) of a single EAPOL frame to capture the needed information to attempt a brute-force attack.Similar to the 
previous attacks against WPA, the attacker must be in proximity to the network they wish to attack.

As per usual we will need to put the wifi adapter into monitor mode, do this by selecting the "1" option from the wifi Home

Once in monitor mode select the option "12" to capture PMKID in you available range,

you should let this run for a few minutes to collect as many possible keys as possible, when you are done use ctrl + c
to end the capture, if there are networks in your area you should be notified that you have captured some PMKIDs.

Go ahead back to the wifi HOme and return you wifi card to normal mode, there is no need to be in monitor mode once we
have the hashes to be cracked

TO crack the hashes, select option '13' from the wifi HOme page, From there follow the prompts and in time if a 
Password matches you've cracked the WIFI! Larger password list take longer but are more effective. Experiment with 
different lists! 

Target Computer Recon and SUBNETS
--------------------------------
Target Computer Recon and SUBNETS
--------------------------------
So you've logged into a network! and now you want to know what other computers or NODES are on that same network 
NOTE:( you can also you this to scan websites or other IP's on the internet) Well in order to learn what we're doing
we should familiarize ourselves with a few concepts before starting anything.

Internet: you know what this is, but to make sure, the internet is a large world wide network of computers, 
servers , websites etc.

IP Address: or INTERNET PROTOCOL ADDRESS is a unique set of numbers used to identify computers on the internet

Subnet: THis is important. so before your computer connects to the internet it has to connect to the WiFi, 
Router, AP or local network (LAN). In example lets say you've connected your laptop to your home wifi, well 
its likely that there are other devices connected to that wifi network as well. This home network is called 
a SUBNET, like a small internet just for your house, and just like every computer on the internet has its own 
IP you have a SUBNET IP, which you can tie back to each device on your network. It we to make an example list 
of what we might see on a home network it might will look something like this 

Router IP 234.53.232.354 (what the internet sees)

NODE name           Subnet ip (what you see)
-----------------------------
Mom's comp          192.168.1.7
Dad's PC			192.168.1.10
Sisters Phone		192.168.1.23
Our HackBox			192.169.1.69

Now this is just an example I typed up so when you receive actual data it probably wont be formatted quite 
the same. Anyways you may have noticed that all the SUBNET IP's start with "192.168.1" without getting to 
involved This is how your WiFi Router organizes all devices. In a metaphor you can think if our computer is 
a apartment in an Apartment complex say Shady Acres, then each apartment has it has its own number, 192.168.1 
would be the The Shady Acres complex . and the last number for example "Our HackBox" would be 69 or our apartment 
number. some routers don't use the number 192.168. but not all Apartment Complexes are called shady acres. 
Even without 192.168 conventions it's still a Subnet. IMPORTANT! other people on the internet don't see your 
Subnet IP (unless they're connected to you network) They see your router's IP instead. As far as the internet 
sees Mom's comp, Dad's PC, Sister's Phone, and Our Hackbox's activity all comes from the routers IP.

To see your SUBNET ip go to the Device finding and Attacking option it will be shown as the item from the top of the menu! 


How to Scan your Network for Targets
--------------------------------
Now that you know what a SUBNET is you're ready to scan it to find other machines, Nodes, or devices. Select 
the "Scan your LAN or Subnet" option from the Device finding and Attacking menu. You will notice next to your 
subnet IP a /24 or /8 or /something similar, without getting in too deep, that /something shows what class network
you're on. A class C network would have a subnet mask of 255.255.255.0 which means that 24 bits are used for the 
network. In CIDR notation this is designated by a /24 (you can ignore that for now just know you will need to 
enter the /something later)

Now is later! Copy the SUBNET IP including the /something trailing it, and hit enter. YOu will be shown a list 
of all devices attached to your SUBNET. THis information will be saved in the "Scan.txt" file in DUSIOS's working 
directory.


Port Scanning and Find holes to Attack in Target MAchine
--------------------------------
Now that you have the IP of the computer or server you wish to target, you will need scan that particular 
machine for weaknesses. Computers use "PORTS" to communicate with other computers, by scanning a computers PORTS,
we may be able to find holes in that computer's security. PORTS are not physical and there are thousands of them,
and no one knows them all, but there are some commonly used ones, Here are some common ports

PORT# and Usage

20 File Transfer Protocol (FTP) Data Transfer

21 File Transfer Protocol (FTP) Command Control

22 Secure Shell (SSH)

23 Telnet - Remote login service, unencrypted text messages

25 Simple Mail Transfer Protocol (SMTP) E-mail Routing

53 Domain Name System (DNS) service

80 Hypertext Transfer Protocol (HTTP) used in World Wide Web

110 Post Office Protocol (POP3) used by e-mail clients to retrieve e-mail from a server

119 Network News Transfer Protocol (NNTP)

123 Network Time Protocol (NTP)

143 Internet Message Access Protocol (IMAP) Management of Digital Mail

161 Simple Network Management Protocol (SNMP)

194 Internet Relay Chat (IRC)

443 HTTP Secure (HTTPS) HTTP over TLS/SSL

If you are interested in using exploits over certain ports check out METASPLOIT. To scan a IP select the 
"Port Scan Target Machine" Option from the menu. It may take a minute but you should be returned 
information about the machine at your target IP and some information about its Operating system, This
is called BANNER GRABBING. KNowing what kind of operating system a computer uses can be very useful as
many OS's have known security flaws. 


BruteForcing Ports and Services
--------------------------------
Once you know the ports open on a target machine you can attempt to login to them. Not all ports can be 
logged on traditionally with a username and password. Some of the ports that can be are SSH, FTP, and TELENET. 
But what happens if you dont know the Username or Password!?! That's where BRUTEFORING comes in. BRUTEFORCING 
is the act of trying many different password or usernames against a system till one or more work. In order to 
do this you will need a list of User names or Passwords, lucky for you included in DUSIOS there are several 
different lists of each. To BRUTEFORCE with Dusios open the bruteforce option and follow the prompts. You can use 
this option to bruteforce systems that are not on your SUBNETT but on the INTERNET too!!



FIREWALL and Keeping yourself Safe
--------------------------------
A firewall is a system that provides network security by filtering incoming and outgoing network traffic 
based on a set of user-defined rules. In general, the purpose of a firewall is to reduce or eliminate the 
occurrence of unwanted network communications while allowing all legitimate communication to flow freely. 
DUSIOS has provided you an easy way to set firewall using UFW or UnComplicated FireWall which itself uses 
IPTABLES either of which you can lookup how to set up on google but for now well work with DUSIOS interface.
To setup your firewall select the "Anonymize, Secure, and Defend Home" form the top screen and then the 
"Enable/Disable FIreWall" from the next menu, and enter 'e' thats it you should see a list of processes 
start and thats it 

Obfuscate Your internet History with NOISY
--------------------------------
Since post 9/11 the patriot act has granted access for law enforcement to have access to your internet 
history without a warrant, this is troubling for any one who cares about their privacy. Noisy was developed 
to create random internet traffic from your computer. Using NOisy and a list of websites from nUllByte.com 
is easy from the Dusios interface. Navigate to the "[3]. Anonymize, Secure, and Defend" page from the main 
Dusios page, from there select the "[5]. Flood your ISP with Random Data to Protect Privacy" option, NOisy 
should start immediately, 

if you wish to use Dusios for other means you will either have to stop NOISEY from running or open a new 
terminal window while it launches. 

RootKits, what they are, and how to check for them
--------------------------------
What is a Rootkit?

Rootkits are the toolboxes of the malware world. They install themselves as part of some other download, 
backdoor, or worm. They then take steps to prevent the owner from detecting their presence on the system. 
Once installed, Rootkits provide a bad actor with everything they need to take control of your PC and use 
it for DDoS or as a zombie computer.

Rootkit scans are the best attempt to detect a rootkit infection, most likely initiated by your AV solution.
The challenge you face when a rootkit infects our PC is that your OS can’t necessarily be trusted to 
identify the rootkit. They are pretty sneaky and good at camouflage. If you suspect a rootkit virus, 
one of the better strategies to detect the infection is to power down the computer and execute the scan 
from a known clean system.

Rootkit scans also look for signatures, similar to how they detect viruses. Hackers and security 
developers play this cat and mouse game to see who can figure out the new signatures faster. A a surefire 
way to find a rootkit is with a memory dump analysis. You can always see the instructions a rootkit is 
executing in memory, and that is one place it can’t hide. 


To use the root kit checks built into Dusios navigate to the Anonymize, Secure, and Defend Home page 
and select either the "[8]. Scan Computer with chkrootkit" or "[9]. Advance Scan with rkhunter" either
option will then scan your system for rootkits. 


