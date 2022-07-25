
# Online Python - IDE, Editor, Compiler, Interpreter

username = input('user - ')
terminal='standardTerminal'
password='none'
echo='none'
filescreatedtotal=0
filescreated=0
fileseditedtotal=0
filesedited=0

while True:
    path = (terminal+'/'+username+' - ')
    cmd = input(path)
    if cmd=='helpcmd':
        print('commands are - \n- helpcmd \n- settings \n- file \n- calculator \n- openecho \n- end')


#calculator
    elif cmd == 'calculator':
        print('calculator - \n- calc \n- calc.classic')

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



#calc.classic
    elif cmd == 'calc.classic':
        print('calc.classic - \n- calc.totaliser \n- calc.multiplyer \n- calc.divider')

    elif cmd == 'calc.totaliser':
        anumber1=input('- number 1 - ')
        anumber2=input('- number 2 - ')
        print('- total -' , int(anumber1)+int(anumber2))


    elif cmd == 'calc.multiplyer':
        mnumber1=input('- number 1 - ')
        mnumber2=input('- number 2 - ')
        print('- total -' , int(mnumber1)*int(mnumber2))

    elif cmd == 'calc.divider':
        dnumber1=input('- number 1 - ')
        dnumber2=input('- number 2 - ')
        print('- total -' , int(dnumber1)/int(dnumber2))

#settings
    elif cmd == 'settings':
        print('settings - \n- set.terminal \n- set.username \n- set.password \n- info \n- set.data')

    elif cmd == 'info':
        print('info - \n- path -',path,'\n- terminal -',terminal,'\n- username -',username,'\n- password -',password)
    
    elif cmd == 'set.terminal':
        terminal=input('set new terminal - ')
        print('set new terminal -',terminal)

    elif cmd == 'set.username':
        username=input('set new username - ')
        print('set new username -',username)

    elif cmd == 'set.password':
        confirmpassword1=input('set new password - ')
        confirmpassword2=input('confirm new password - ')
        if confirmpassword1 == confirmpassword2:
            password=confirmpassword1
            print('set new password -',password)
        else:
            print('wrong confirmation')
            

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
                    print('====================full system reset complete====================')
                else:
                    print('ended process')
            else:
                print('access denied')

#openecho
    elif cmd == 'openecho':
        print('openecho - \n- openecho.start \n- openecho.keeptalk \n- openecho.last \n- openecho.sayhi')

    elif cmd == 'openecho.sayhi':
        print('Hello, World!')

    elif cmd == 'openecho.start':
        echo=input('- echo - ')
        print('- ' + username + ' - ' + echo)

    elif cmd == 'openecho.last':
        if echo == 'none':
            print('no record of last openecho use')
        else:
            print('- ' + username + ' - ' + echo)
            pass

    elif cmd == 'openecho.keeptalk':
        openechorange=int(input('range - '))
        for i in range (openechorange):
            echo=input('- echo -')
            print('- ' + username + ' - ' + echo)
            if echo == 'openecho.stop':
                print('openecho stopped')
                break

    elif cmd == 'echo':
        print('echo')

#file
    elif cmd == 'file':
        print('file - \n- file.open \n- file.create \n- file.write \n- file.append \n- file.delete \n- file.helloworld')

    elif cmd == 'file.helloworld':
        helloworldfile=open('Hello, World!.txt' , 'x')
        helloworldfile.write('Hello, World!')
        helloworldfile.close()
    
    elif cmd == 'file.open':
        openfile=open(input('name file - '))
        print('file -' , openfile)
        print(openfile.read())
        openfile.close()

    elif cmd == 'file.create':
        createfile=open(input('name file - ')+'.'+input('extension - '), 'x')
        createfile.close()
        filescreatedtotal=filescreated+int(1)

    elif cmd == 'file.write':
        writefile=open(input('name file - ') , 'w')
        print(writefile.write(input('edit file - ')))
        writefile.close()
        fileseditedtotal=filesedited+int(1)

    elif cmd == 'file.append':
        appendfile=open(input('name file - ') , 'a')
        print(appendfile.write(input('append file - ')))
        appendfile.close()
        fileseditedtotal=filesedited+int(1)

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
                    else:
                        print("file not found")
                else:
                    print('ended process')
            else:
                print('access denied')

        
#end
    elif cmd == 'end':
        confirmStatsFile=input('request info? doing so will overwrite your current stats.txt. y/n - ')
        if confirmStatsFile == 'y':
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
        print('syntax error - \n- ' + cmd + ' is not a command')
