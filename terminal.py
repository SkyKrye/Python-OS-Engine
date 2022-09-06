
# Online Python - IDE, Editor, Compiler, Interpreter

username = input('user - ')
terminal='standardTerminal'
password='none'
echo='none'
filescreatedtotal=1
filescreated=1
fileseditedtotal=1
filesedited=1
errorVariable=0
oneVariablePlaceHolder=1
errorVariableTotal=0
commandsExecuted=0
rawprint='none'

#startup
print('- pyTerminal -')
print('- Welcome to pyTerminal -')
print('- do "helpcmd" for a list of available commands')


while True:
    path = (terminal+'/'+username+' - ')
    cmd = input(path)
    if cmd=='helpcmd':
        print('commands are - \n- helpcmd \n- settings \n- file \n- calculator \n- openecho \n- printTools \n- infofetch \n- docs \n- end')
        commandsExecuted+=1


#calculator
    elif cmd == 'calculator':
        print('calculator - \n- calc \n- calc.classic')
        commandsExecuted+=1

#calculator
    elif cmd == 'calc':
        #input
        problem = input("Insert a problem: ")
        #variables
        problem = problem.replace(" ","")
        selectnum = True
        num1 = ""
        num2 = ""
        
        for i in range(len(problem)):
            if problem[i] == "+" or problem[i] == "-" or problem[i] == "*" or problem[i] == "/":
                if selectnum == True:
                    operator = problem[i]
                else:
                    print("Can only conjoin 2 numbers.. adding the first 2")
                    break
                selectnum = False
                continue
            if selectnum == True:
                num1 += problem[i]
            else:
                num2 += problem[i]
        try:
            num1 = int(num1)
            num2 = int(num2)
        except:
            print("Didn't use integers")   
        if operator == "+":
            finalanswer = num1 + num2
        elif operator == "-":
            finalanswer = num1 - num2
        elif operator == "*":
            finalanswer = num1 * num2
        elif operator == "/":
            finalanswer = num1 / num2
        else:
            print("Invalid syntax")
            continue
        print(finalanswer)
        commandsExecuted+=1



#calc.classic
    elif cmd == 'calc.classic':
        print('calc.classic - \n- calc.totaliser \n- calc.multiplyer \n- calc.divider')

    elif cmd == 'calc.totaliser':
        anumber1=input('- number 1 - ')
        anumber2=input('- number 2 - ')
        print('- total -' , int(anumber1)+int(anumber2))
        commandsExecuted+=1

    elif cmd == 'calc.multiplyer':
        mnumber1=input('- number 1 - ')
        mnumber2=input('- number 2 - ')
        print('- total -' , int(mnumber1)*int(mnumber2))
        commandsExecuted+=1

    elif cmd == 'calc.divider':
        dnumber1=input('- number 1 - ')
        dnumber2=input('- number 2 - ')
        print('- total -' , int(dnumber1)/int(dnumber2))
        commandsExecuted+=1

#settings
    elif cmd == 'settings':
        print('settings - \n- set.terminal \n- set.username \n- set.password \n- info \n- set.data')

    elif cmd == 'info':
        print('info - \n- path -',path,'\n- terminal -',terminal,'\n- username -',username,'\n- password -',password)
        commandsExecuted+=1
    
    elif cmd == 'set.terminal':
        terminal=input('set new terminal - ')
        print('set new terminal -',terminal)
        commandsExecuted+=1

    elif cmd == 'set.username':
        username=input('set new username - ')
        print('set new username -',username)
        commandsExecuted+=1

    elif cmd == 'set.password':
        confirmpassword1=input('set new password - ')
        confirmpassword2=input('confirm new password - ')
        if confirmpassword1 == confirmpassword2:
            password=confirmpassword1
            print('set new password -',password)
            commandsExecuted+=1
        else:
            print('wrong confirmation')
            
    elif cmd == 'set.cmdmode':
        cmdselector=input('what mode do you want to replace your cmd with? - \n- cmd \n- rawprint \n- func \n'+path)
        if cmdselector == 'rawprint':
            print('your cmd has been set to rawprint')
            rpTitle=input('rawprint/title - ')
            rpSubject=input('rawprint/subject - ')
            rpBody=input('rawprint/body - ')
            rpLeave=input('rawprint/sign - ')
            print("""
            ————————————————————————————————————————————————————————————————————————————————
            """+rpTitle+"""                                                                 
            ————————————————————————————————————————————————————————————————————————————————
            """+rpSubject+"""                                                               
            ————————————————————————————————————————————————————————————————————————————————
                                                                                            
            """+rpBody+"""                                                                  
                                                                                            
            ————————————————————————————————————————————————————————————————————————————————
                                                        """+rpLeave+"""                     
            ————————————————————————————————————————————————————————————————————————————————
                """)
            

        elif cmdselector == 'func':
            print('your cmd has been set to func')
            for i in range(10):
                func=input('func/')
                if func == 'cmd':
                    print(cmd)
                if func == 'user':
                    print(username)
                if func == 'terminal':
                    print(terminal)
                if func == 'password':
                    print(password)
                if func == 'echo':
                    print(echo)
                if func == 'rawprint':
                    print(rawprint)
                
        elif cmdselector == 'cmd':
            print('your cmd has been set to default')
        else:
            print('no such option')

    elif cmd == 'set.data':
        if password == 'none':
            print('cannot reset data')
        else:
            confirm=input('confirm password - ')
            if confirm == password:
                doubleconfirm=input('are you really sure you want to reset all information? y/n - ')
                if doubleconfirm == 'y':
                    print('reset started')
                    terminal='standardTerminal'
                    username='defaultUser'
                    password='none'
                    commandsExecuted=0
                    echo='none'
                    filescreatedtotal=1
                    filescreated=1
                    fileseditedtotal=1
                    filesedited=1
                    errorVariable=0
                    oneVariablePlaceHolder=1
                    errorVariableTotal=0
                    print('====================full system reset complete====================')
                else:
                    print('ended process')
            else:
                print('access denied')

#openecho
    elif cmd == 'openecho':
        print('openecho - \n- openecho.start \n- openecho.keeptalk \n- openecho.last \n- openecho.sayhi')
        commandsExecuted+=1

    elif cmd == 'openecho.sayhi':
        print('Hello, World!')
        commandsExecuted+=1

    elif cmd == 'openecho.start':
        echo=input('- echo - ')
        print('- ' + username + ' - ' + echo)
        commandsExecuted+=1

    elif cmd == 'openecho.last':
        if echo == 'none':
            print('no record of last openecho use')
            commandsExecuted+=1
        else:
            print('- ' + username + ' - ' + echo)
            pass

    elif cmd == 'openecho.keeptalk':
        openechorange=int(input('range - '))
        for i in range (openechorange):
            echo=input('- echo -')
            print('- ' + username + ' - ' + echo)
            commandsExecuted+=1
            if echo == 'openecho.stop':
                print('openecho stopped')
                break
                commandsExecuted+=1

    elif cmd == 'echo':
        print('echo')
        commandsExecuted+=1

#file
    elif cmd == 'file':
        print('file - \n- file.open \n- file.create \n- file.write \n- file.append \n- file.delete \n- file.helloworld')
        commandsExecuted+=1

    elif cmd == 'file.helloworld':
        helloworldfile=open('Hello, World!.txt' , 'x')
        helloworldfile.write('Hello, World!')
        helloworldfile.close()
        commandsExecuted+=1
    
    elif cmd == 'file.open':
        openfile=open(input('name file - '))
        print('file -' , openfile)
        print(openfile.read())
        openfile.close()
        commandsExecuted+=1

    elif cmd == 'file.create':
        createfile=open(input('name file - ')+'.'+input('extension - '), 'x')
        createfile.close()
        filescreatedtotal=filescreated+int(1)
        commandsExecuted+=1

    elif cmd == 'file.write':
        writefile=open(input('name file - ') , 'w')
        print(writefile.write(input('edit file - ')))
        writefile.close()
        fileseditedtotal=filesedited+int(1)
        commandsExecuted+=1

    elif cmd == 'file.append':
        appendfile=open(input('name file - ') , 'a')
        print(appendfile.write(input('append file - ')))
        appendfile.close()
        fileseditedtotal=filesedited+int(1)
        commandsExecuted+=1

    elif cmd == 'file.delete':
        if password == 'none':
            print('cannot delete file')
        else:
            confirm=input('confirm password - ')
            if confirm == password:
                doubleconfirm=input('are you really sure you want to delete file? y/n - ')
                if doubleconfirm == 'y':
                    import os
                    filedeleter=input('name file - ')
                    if os.path.exists(filedeleter):
                        os.remove(filedeleter)
                        filedeleter='none'
                        commandsExecuted+=1
                    else:
                        print("file not found")
                else:
                    print('ended process')
            else:
                print('access denied')


#trolled
    elif cmd == 'print(trolled)':
        print()
        print('a new window has been opened on your primary system monitor')
        print('close it to stop printTools ')
        import tkinter as tk
            
        
        def write_slogan():
            print(input('inputhere'))
        
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()
        
        slogan = tk.Button(frame,
                           text=input('here'),
                           command=write_slogan)
        slogan.pack(side=tk.LEFT)
            
        root.mainloop()
        commandsExecuted+=1


#print Tools
    elif cmd == 'printTools':
        print('a new window has been opened on your primary system monitor')
        print('close it to stop printTools ')
        commandsExecuted+=1
        import tkinter as tk
            
        
        def write_slogan():
            print("Tkinter is easy to use!")

        def write_helloworld():
            print('Hello, World!')

        def write_yes():
            print('yes')

        def input_help():
            definputhelp=input('')
            
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()
        
        slogan = tk.Button(frame,
                           text="Tkinter",
                           command=write_slogan)
        slogan.pack(side=tk.LEFT)

        slogan = tk.Button(frame,
                           text="Hello",
                           command=write_helloworld)
        slogan.pack(side=tk.RIGHT)

        slogan = tk.Button(frame,
                           text="yes",
                           command=write_yes)
        slogan.pack(side=tk.RIGHT)

        slogan = tk.Button(frame,
                           text="input",
                           command=input_help)
        slogan.pack(side=tk.RIGHT)
        
        root.mainloop()

#random
    elif cmd == 'random':
        import secrets
        names=["We","I","They","He","She","Jack","Jim"]
        verbs=["was","is","are","were"]
        nouns=["playing a game","watching television","talking","dancing","speaking"]
        while True:
           a=(secrets.choice(names))
           b=(secrets.choice(verbs))
           c=(secrets.choice(nouns))
           print(a+" ",b+" ",c)
           break

#random
    elif cmd == 'secret':
        import secrets
        firstSecretNames=["Nice","Found me!","Wowie","Real cool","Epic","Amazing","LOL","Bark-IT for life!","Great Mega32!"]
        while True:
           firstSecretPrint=(secrets.choice(firstSecretNames))
           print(a)
           break

#randomrate
    elif cmd == 'randomRate':
        import secrets
        randomRater=["1","2","3","4","5","6","7","8","9","10"]
        while True:
            randomRaterPrint=(secrets.choice(randomRater))
            print(randomRaterPrint)
            break

#documents
    elif cmd == 'docs':
        print('docs - Documents - \n- docs.main \n- docs.commands \n- docs.development')
        commandsExecuted+=1

#docs.main
    elif cmd == 'docs.main':
        commandsExecuted+=1
        print("""
    - Welcome to the pyTerminal documents -    
    - Main Page -    

    The pyTerminal is a basic terminal similar to that of operating systems like Windows(Microsoft) and Linux(UNIX, IBM, GNU)
    The similarities of it cannot be compared to MacOS(Apple) since the developer(SkyKrye) does not have any experience with using it.
    pyTerminal was a project that I decided to make simply out of boredom, one day I was sitting in my room in quarantine and decided
    to remake a failed HTML project(CLIos_https://skykrye.000webhostapp.com/clios/clios.html) - that had some functions which would
    allow you to use it like an operating system - but in actual CLI using a much easier to learn and read language(Python), now since
    I had already had some experience with Python I started to bang bang my keyboard and make a simple program that was built on
    [if/else] statements for commands and I keep updating it every now and then when I get ideas for commands.

    - 1: Commands -    
    pyTerminal uses text commands as it's main source of information for executing or doing process/tasks, processes such as a
    calculator[calc, calc.classic], a tool for creating and managing files[file], and text for fetching variable information about
    pyTerminal. These commands work through [if/else] statements that work on a simple variable(cmd), the variable(cmd) is an input,
    and lets say [`if- the input is "say.hello"`] then the program would give the output "hello", or [`else- if that command doesn't
    exist`] it outputs "syntax error". It's really simple.

    - 2: Intended Usage -    
     pyTerminal's intended usage is to serve as an engine that is currently in the making, and thus it doesn't have any major feature
     that can help the user enough that it is actually useful, other than the files[file] command, which can be used to create, write,
     append, and delete a file. This in my opinion is the best feature up till now since the deleting feature can be used to delete ANY
     file on your system(not guaranteed for deleting system32/system/hardware related files since it is not optimal and has not been
     tested). This helps a ton if you get into a situation where a buggy file cannot be terminated or deleted due to it being used as a
     seperate application or even if you don't have permissions for removing a corrupt file etc.

     - 3. Why? -    
     pyTerminal, as I said before, does not have any intended usage as of now, and so it is completely up to you if you wish to not keep
     it or not download it(this cannot be true since the only way you'd be reading this other than from an image or copied text is by
     installing pyTerminal) etc. I simply don't mind. BUT what I would mind is if you were to support me with this project simply by
     helping me out using Discord(Jason Citron), my user tag is "SkyKrye#5867" without quotes.

     |docs.main| - docs.commands - docs.secrets - docs.development

        """)

#docs.commands
    elif cmd == 'docs.commands':
        commandsExecuted+=1
        print("""
    - Welcome to the pyTerminal documents -    
    - Commands -    

    The pyTerminal is a basic terminal similar to that of operating systems like Windows(Microsoft) and Linux(UNIX, IBM, GNU)
    pyTerminal, as said in the main document page[docs.main] relies on commands for functions and usage etc. and for further
    explaining them and their usages you can always refer to this page[docs.commands].
    
    - 1: Here is an explanation of a structure of a file:(example: set.terminal) -    
    set.terminal
    [set].terminal - set, short for setting, is the main command.
    set[.]terminal - . , filters the command/divides it to a root, set.terminal allows modification of the terminal.
    set.[terminal] - terminal, in our case is the parameter/usage of the setting command, it changes the username,
                     it can be changed to something else.
    set.[username] - username, this is an example of another parameter/usage of the settings command, it changes
                     the username in our case.
    
    - 2: Some of the commands(simple) can be used simply by typing them, they have no extra contents -    

    - helpcmd - This is the first command, it shows other stable available commands that you can use in pyTerminal.
    - usage - [helpcmd]

    - settings - This is the settings command, it is used to modify and change default settings/variables used to control the
                 system(pyTerminal) and is used to set the password.
    - usage - [set.{parameter}]

    - file - This is the command used to manage files, it can make, write, append and delete files of your choice.
    - usage - [file.{parameter}]

    - calculator - This command shows a simple calculator for +,-,*,/ operations, there are two versions, a direct problem
                   solving one[calc] and another one that has 2 inputs for 2 numbers[calc.classic].
    - usage - [calc.{parameter}]

    - openecho - This command opens a input for echo, it has 3 versions, one that starts for only one echo message[openecho.start],
               - another one that replaces the terminal path["""+ str(path)+ """] which loops for a variable amount of time, you can
               - do [openecho.stop] to stop the loop and revert to the default terminal path"""+ str(path)+ """. Lastly, one version
               - echo's "Hello, World!"[openecho.sayhi]
    - usage - [openecho.{parameter}]

    - printTools - This command when executed opens a new window on your computer that shows buttons to print out in the terminal.
    - usage - [printTools]

    - infofetch - A command based off the Linux(UNIX, IBM, GNU) neofetch command, it generates a large print of a ascii character with
                - important variables and information about pyTerminal and how it is being used.
    - usage - [infofetch]

    - docs - A command for displaying multiple documents that might help you out with using pyTerminal and command information
    - usage - [docs.{parameter}]

     docs.main - |docs.commands| - docs.secrets - docs.development

        """)

#docs.secrets
    elif cmd == 'docs.secrets':
        commandsExecuted+=1
        print("""
    - Welcome to the pyTerminal documents -    
    - Main Page -    

    The pyTerminal is a basic terminal similar to that of operating systems like Windows(Microsoft) and Linux(UNIX, IBM, GNU)
    pyTerminal, does have some sneaky peaky secret commands like printTools

    - 1: These are the secrets, no longer secrets now that I spoiled it I guess -

    - random - Outputs a random sentence string.

    - secret - Outputs a random sentence/word.

     docs.main - docs.commands - |docs.secrets| - docs.development

        """)

#docs.development
    elif cmd == 'docs. development':
        commandsExecuted+=1
        print("""
    - Welcome to the pyTerminal documents -    
    - Main Page -    

    The pyTerminal, as you can see, is still currently in development and lacks many commands, this page highlights that since it's unfinished.
    YOU however can support the development with a variety of methods too, have a read.

    - 1: pyTerminal - 
    I started the pyTerminal with some simple commands and printTools being the most recent and stable one.

    - 2: Support me -
    You can support me with a variety of methods listed here:

    - Youtube - https://youtube.com/skykrye

    - Discord - https://discord.gg/keV6Bmc

     docs.main - docs.commands - docs.secrets - |docs.development|

        """)

#infofetch
    elif cmd == 'infofetch':
        print(r"""
                                                                                                                                                                                                        
                                     ::::::                                                         
                                    ::======:                                                       
                                   ::===.=====                                                      
                                   :==......===:                                                    
                                  ::==.......====                                                   
                                  :===.........===                                                  
                                  :==...........===                                                 
                                  :==............===:                                               
                                  :==.............====                                              
                                  :==...............===                                             
                                  :==................===                                            
                                  :==.................===:                                          
                                 ::==..................====                                         
                                 :==.....................===                                        
                                 :==......................===:                                      
                                 :==.........:::...........====:                                    
                                 :==........::===:...........====:                                  
                                 :==........:======:..........=====:                                
                                 :==........:== =====:..........=====::                             
                                 :==........:==    ====...........======::                          
                                 :==........:==     ====:............======:::                      
                                 :==.........==       ====:.............=======                     User: """+ username+ """
                                  ==.........:==        ====...............=====                    
                                  :==........:==         ====:................===                   Main: pyTerminal
                                  :==.......::==           ====:...............===                  
                                  :==........:=              ====:..............===                 Language (Main): Python
                                  :==........::=              =====:...::........==                 
                                  :==........::=                =====:.:==.......:==                Path: """+ path+ """
                                  :==........::=                  =====:==.......:==                
                                  :==........::=                     ====.........===               Shell/CMD: input("""+ path+ """)
                                  :==.........::                    ::==.........::==               
                                  :==.........::=       :::::      ::===.........:==                
                                  :==.........::=     ::=====:::::::===.........::==                
                                  :==.........::= ::::================........:::==                 
                                  :==.........::::=======....========........::===                  
                                  :==.........:========....................:::===                   
                                  :==........:=====.........==...........:::====                    
                                  :==........:==............==.........:::====                      Files Created: """+ str(filescreatedtotal)+ """
                                   ==........:==...........::::......:::=====                       
                                   :==......:==........::::=====....::=====                         Files Edited: """+ str(fileseditedtotal)+ """
                                   :==......:=......:::====    .::..=====                           
                                   :==......:=..::::====        =:..=:                              Total Errors: """+ str(errorVariableTotal)+ """
                                   :==......:=::====           =:..:=:                              
                                   :==........===:=           =:..===:                              Total commands executed: """+ str(commandsExecuted)+ """
                                   :==..........::=         =::.:==::                               
                                   :==..........::=       ==:...==                                  
                                   :==..........::=     ==::.:===                                   
                                   :==..........::=   ==::..:===                                    
              =                    :==..........::= ==::....==                                      
              =                     ==...........::=::..:====                                       
             =:=                    :==..........::===:=====                                        
             =::=                   :==..........::======                                           
             =::=                   :==..........::=                                                
             =::=                   :==..........::=                                                
             =::=                   :==..........::=                                                
             =:::=                  :==..........::=                                                
             =:=:=                  :==..........::=                                                
             =:=:=                 ::==..........::=                                                
             =:=::=                ::==..........::=                                                
             =::=:=                ::==..........::=                                                
             =::=::=               ::=............:=                                                
             =::=.::               ::=............:=                                                
             =::=.:::              ::=............:=                                                
              =:=..:::             ::=............:=                                                
              =::=..:::            ::=...........::=                                                
              =::=...:::           ::=...........::=                                                
              =::=....::::         ::=...........::=                                                
               ::=.....=:::       ::==...........::=                                                
               =::=.....=:::::   :::=............::=                                                
                ::=......==::::::::==............::=                                                
                =::=.......===:::===.............::=                                                
                 :::=.........====...............::=                                                
                 =:::=...........................::=                                                
                  =:::..........................:::=                                                
                   =:::.........................::==                                                
                    =::::.......................::=                                                 
                     ==::::....................:::=                                                 
                        =:::::.................::==                                                 
                          =:::::..............:::=                                                  
                            =::::::..........:::==                                                  
                              ==::::::::..:::::==                                                   
                                 ==::::::::::===                                                    
                                    ===::::===                                                      
                                        ====                                                        
        
    """)

#end
    elif cmd == 'end':
        confirmStatsFile=input('request info? doing so will overwrite your current stats.txt. y/n - ')
        if confirmStatsFile == 'y':
            commandsExecuted+=1
            import os
            if os.path.exists('stats.txt'):
                os.remove('stats.txt')
            else:
                print('file not found, proceeding to end')
            statsfile=open('stats.txt' , 'x')
            statsfile=open('stats.txt' , 'w')
            statsfile.write('stats-info - \n- path -'+path+'\n- terminal -'+terminal+'\n- username -'+username+'\n- password -'+password)
            statsfile.close()
            print('saved stats to file - stats.txt')
            break
        else:
            print('ended process with stats - \n- username - ' + username +'\n- terminal - '+ terminal)
            break

    else:
        errorVariableTotal += 1
        print('syntax error - \n- ' + cmd + ' is not a command')
