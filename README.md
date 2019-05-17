# Paybag

Create metasploit payload easily using Paybag


![Screenshot at 2019-05-17 10-47-49](https://user-images.githubusercontent.com/32305505/57904787-dfb0ae80-7891-11e9-8301-34571fcf7dac.png)

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

**'msfconsole' and 'msfvenom' files must be present in '/data/data/com.termux/files/usr/bin' folder.**

------------------------------------------------------------------------------------------------------------------

### All payloads are stored in 'payload' folder.

------------------------------------------------------------------------------------------------------------------

### If you have any issue regarding this,Report an issue [Here](https://github.com/Deadpool2000/portkali/issues)
