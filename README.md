# Paybag

Create metasploit payload easily using Paybag

![sce](https://user-images.githubusercontent.com/32305505/57907003-995f4d80-7899-11e9-9c02-38436cf1701a.png)

# Installation
1) git clone https://github.com/Deadpool2000/Paybag.git
2) cd Paybag
3) python3 paybag.py

---------------------------------------------------------------------------------------------------------------

# Usage
**1) Create a payload**
- Create a payload by just giving LHOST and LPORT and send it to victim.

**2) Start Handler**
- After creating payload,send it to victim & execute it on victim machine.
- After execution,Select **'Start Handler'**,give LHOST and LPORT which used while creating payload.
- Now wait until a successfull connection.

**3) Launch Metasploit**
- Start Metasploit using **Launch Metasploit** option.

-----------------------------------------------------------------------------------------------------------------

# Note 
### (Only for Termux users) -

**'msfconsole' and 'msfvenom' files must be present in '/data/data/com.termux/files/usr/bin/' folder.**

**If not,follow this steps to install Metasploit properly:**

**A] Remove old Metasploit (If present)**

**B] Then run following commands in termux:-**
- apt install unstable-repo
- apt update && apt upgrade
- apt install metasploit

------------------------------------------------------------------------------------------------------------------

### All payloads are stored in 'payload' folder.

------------------------------------------------------------------------------------------------------------------

### If you have any issue regarding this,Report an issue [Here](https://github.com/Deadpool2000/portkali/issues)
