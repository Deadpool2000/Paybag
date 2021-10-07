# Paybag

Create metasploit payload easily using Paybag

![Screenshot](https://user-images.githubusercontent.com/32305505/99352267-56d06400-28c8-11eb-8aa3-a7da8e85e337.jpg)


# Installation

### For Linux users -
    sudo apt-get install python3 python3-pip
    
    git clone https://github.com/Deadpool2000/Paybag.git
    
    cd Paybag
    
    sudo pip3 install -r requirements.txt
    
    python3 paybag.py
    
### For Termux users -
    apt install python
    
    git clone https://github.com/Deadpool2000/Paybag.git
    
    cd Paybag
    
    pip3 install -r requirements.txt
    
    python3 paybag.py



# What's New in v1.2?

1) Bugs Fixed
2) If metasploit is not installed on your system, it will install automatically on your system (Only works on Debian-based distro and Termux)


# Usage

**1) Create a payload**
- Create a payload by just giving LHOST and LPORT and send it to victim.

**2) Start Listner**
- After creating payload,send it to victim & execute it on victim machine.
- After execution,Select **'Start Listner'**,select LHOST from table and enter LPORT which used while creating payload.
- Now wait until a successfull connection.

**3) Launch Metasploit**
- Start Metasploit using **Launch Metasploit** option.

-----------------------------------------------------------------------------------------------------

### All payloads are stored in 'payload' folder.

-----------------------------------------------------------------------------------------------------

### Tested on - Ubuntu 20.04, Kali linux & Termux

-----------------------------------------------------------------------------------------------------

### If you have any issue regarding this,report an issue [here](https://github.com/Deadpool2000/Paybag/issues)


-----------------------------------------------------------------------------------------------------


# Show your support


Don't buy me a coffee.I HATE COFFEE!

Just show your support here -

[![Bitcoin Donate Button](https://deadpool2000.github.io/bitcoin-395-920580(1).png)](https://deadpool2000.github.io/btc.html)

[![Ethereum Donate Button](https://deadpool2000.github.io/New%20Project(1).png)](https://deadpool2000.github.io/eth.html)
