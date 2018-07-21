import re
import validation as valid
import dis
import view
import datetime


def changePassword(empid, cur):#TESTED
    #CHANGE THE PASSOWRD OF THE EMPLOYEE/MANAGER/ADMIN
    cur.execute('select password from employees where empid=:1',(empid,))
    res = cur.fetchall()
    res = res [0]
    verify_pass = res[0]
    old_password = input("ENTER YOUR PASSWORD")
    verify = False
    for i in range(3):
        if verify_pass == old_password:
            print("VERIFIED")
            verify = True
            break
        else:
            print("WRONG PASSWORD, PLEASE ENTER AGAIN !!")
            old_password = input("ENTER YOUR PASSWORD")
    
    if verify == False:
        print("YOU HAVE TRIED YOUR MAXIMUM LIMIT FOR NOW !! CONTACT YOUR ADMIN OR COME BACK LATER !!")
        
    else:
        new_pass1 = input("ENTER YOUR NEW PASSWORD")
        chk = False
        while(not chk):
            chk = valid.validPassword(new_pass1)
            if chk:
                break
            print("ENTER YOUR PASSWORD AGAIN")
            new_pass1 = input()
        
        print("PASSWORD CHECKED")
        print("CONFIRM YOUR PASSWORD")
        new_pass2 = input()
        if new_pass1 == new_pass2:
            cur.execute('update employees set password = :1 where empid = :2',(new_pass2,empid))
            cur.execute('commit')
            print("PASSWORD SUCCESSFULLY CHANGED")
        else:
            print("YOUR PASSWORD CANNOT BE CHANGED, PLEASE TRY AGAIN !!")
        
def changeEmployeeDetailsByCashier(empid, cur):#TESTED
    #LET THE CASHIER CHANGE HIS DETAILS
    cur.execute('select designation from employees where empid=:1',(empid,))
    res = cur.fetchall()
    res = res[0][0]
    des = res
    if res == 'ADMIN':#PREVENTIVE MECHANISM BUT WON"T BE NEEDED
        print("YOUR NOT AUTHORIZED TO CHANGE THIS ACCOUNT")
        return "q"
        
    else:
        cur.execute('select name from employees where empid=:1',(empid,))
        res = cur.fetchall()
        res = res[0][0]
        print("NAME : ",res)
        print("EMPLOYEE ID : ",empid)
        print("DESIGNATION : ",des)
        print()
        msg = """
        ENTER :
        1 =======> CHANGE MOBILE NUMBER
        2 =======> CHANGE ADDRESS
        3 =======> CHANGE DATE OF BIRTH
        4 =======> CHANGE GENDER
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        """
        
        while(True):
            msgoption = """
            ENTER : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            """
            choice = input(msg)
            option = 'r'
            if choice in ['1','2','3','4','q','Q','m','M']:
                if choice == '1':
                    while(option == 'r'):#JUST BELOW CHOICE
                        mob = input("ENTER YOUR MOBILE NUMBER")
                        chk = valid.validMobile(mob)
                        if chk:
                            cur.execute('update employees set mobile = :1 where empid = :2',(mob,empid))
                            cur.execute('commit')
                            print("MOBILE NUMBER SUCCESSFULLY CHANGED TO : ",mob)
                        else:
                            print("PLEASE ENTER A VALID MOBILE NUMBER AND TRY AGAIN !!")
                        while(True):#WITHIN CHOICE LOOP
                            option = input(msgoption)
                            option = option.lower()
                            if option in  ['q','m','r']:
                                if option == 'q':
                                    break
                                elif option == 'm':
                                    return 'm'
                                elif option =='r':
                                    print("RELOADED ")
                                    break
                            else:
                                print("PLEASE ENTER A VALID OPTION")
                        
                elif choice == '2':
                    while(option == 'r'):#JUST BELOW CHOICE
                        add = input("ENTER ADDRESS")
                        cur.execute('update employees set address = :1 where empid = :2',(add,empid))
                        cur.execute('commit')
                        print("ADDRESS SUCCESSFULLY CHANGED TO : ",add)
                        while(True):#WITHIN CHOICE LOOP
                            option = input(msgoption)
                            option = option.lower()
                            if option in  ['q','m','r']:
                                if option == 'q':
                                        break
                                elif option == 'm':
                                    return 'm'
                                elif option =='r':
                                    print("RELOADED ")
                                    break
                            else:
                                print("PLEASE ENTER A VALID OPTION")
                elif choice == '3':
                    while(option == 'r'):#JUST BELOW CHOICE
                        dob = input("ENTER DATE OF BIRTH dd/mm/yyyy")
                        chk = valid.validDate(dob)
                        if chk:
                            mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                            a,b,c = re.split("[./-]",dob)
                            dob = a+"/"+mon[int(b)]+"/"+c
                            cur.execute('update employees set DOB = :1 where empid = :2',(dob,empid))
                            cur.execute('commit')
                            print("DATE OF BIRTH SUCCESSFULLY CHANGED TO : ",dob)
                        else:
                            print("DATE NOT VALID ! PLEASE TRY AGAIN !!")
                        while(True):#WITHIN CHOICE LOOP
                            option = input(msgoption)
                            option = option.lower()
                            if option in  ['q','m','r']:
                                if option == 'q':
                                        break
                                elif option == 'm':
                                    return 'm'
                                elif option =='r':
                                    print("RELOADED ")
                                    break
                            else:
                                print("PLEASE ENTER A VALID OPTION")
                elif choice == '4':
                    while(option == 'r'):#JUST BELOW CHOICE
                        gender = input("ENTER YOUR GENDER Male/Female/Other")
                        gender = gender.upper()
                        if gender in ['MALE','FEMALE','OTHER']:
                            cur.execute('update employees set GENDER = :1 where empid = :2',(gender,empid))
                            cur.execute('commit')
                            print("GENDER SUCCESSFULLY CHANGED TO : ",gender)
                        else:
                            print("PLEASE ENTER A VALID GENDER AND TRY AGAIN!!")
                        while(True):#WITHIN CHOICE LOOP
                            option = input(msgoption)
                            option = option.lower()
                            if option in  ['q','m','r']:
                                if option == 'q':
                                        break
                                elif option == 'm':
                                    return 'm'
                                elif option =='r':
                                    print("RELOADED ")
                                    break
                            else:
                                print("PLEASE ENTER A VALID OPTION")
                else:
                    break
            else:
                print("PLEASE ENTER A VALID OPTION AND TRY AGAIN !!")
        return  choice.lower()               
        
def changeEmployeeDetailsByManager(empid, cur):#TESTED
    #LET THE MANAGER CHANGE CASHIER DETAILS
    cur.execute('select designation from employees where empid=:1',(empid,))
    res = cur.fetchall()
    res = res[0][0]
    des = res
    if res != 'CASHIER':#MANAGER CANNOT CHANGE ADMIN ACCOUNT OR OTHER MANAGER ACCOUNT
        print("YOU ARE NOT AUTHORIZED TO CHANGE THIS ACCOUNT");
        return "q"
        
    else:
        cur.execute('select name from employees where empid=:1',(empid,))
        res = cur.fetchall()
        res = res[0][0]
        print("NAME : ",res)
        print("EMPLOYEE ID : ",empid)
        print("DESIGNATION : ",des)
        print()
        msg = """
        ENTER :
        1 =======> CHANGE NAME
        2 =======> CHANGE MOBILE NUMBER
        3 =======> CHANGE ADDRESS
        4 =======> CHANGE DATE OF BIRTH
        5 =======> CHANGE GENDER
        6 =======> CHANGE DATE OF JOINING
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        """
        
        while(True):
            msgoption = """
            ENTER : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            """
            option = 'r'
            choice = input(msg)
            if choice in ['1','2','3','4','5','6','q','Q','m','M']:
                if choice == '1':
                    while(option == 'r'):#JUST BELOW CHOICE
                        name = input("ENTER NEW NAME")
                        chk = valid.validName(name)
                        if chk:
                            cur.execute('update employees set name = :1 where empid = :2',(name,empid))
                            cur.execute('commit')
                            print("NAME SUCCESSFULLY CHANGED TO : ",name)
                        else:
                            print("INVALID NAME PLEASE TRY AGAIN !!")
                        while(True):#WITHIN CHOICE LOOP
                            option = input(msgoption)
                            option = option.lower()
                            if option in  ['q','m','r']:
                                if option == 'q':
                                        break
                                elif option == 'm':
                                    return 'm'
                                elif option =='r':
                                    print("RELOADED ")
                                    break
                            else:
                                print("PLEASE ENTER A VALID OPTION")
                        
                        
                elif choice == '2':
                    while(option == 'r'):#JUST BELOW CHOICE
                        mob = input("ENTER MOBILE NUMBER")
                        chk = valid.validMobile(mob)
                        if chk:
                            cur.execute('update employees set mobile = :1 where empid = :2',(mob,empid))
                            cur.execute('commit')
                            print("MOBILE NUMBER SUCCESSFULLY CHANGED TO : ",mob)
                        else:
                            print("PLEASE ENTER A VALID MOBILE NUMBER AND TRY AGAIN !!")
                        while(True):#WITHIN CHOICE LOOP
                            option = input(msgoption)
                            option = option.lower()
                            if option in  ['q','m','r']:
                                if option == 'q':
                                        break
                                elif option == 'm':
                                    return 'm'
                                elif option =='r':
                                    print("RELOADED ")
                                    break
                            else:
                                print("PLEASE ENTER A VALID OPTION")
                            
                elif choice == '3':
                    while(option == 'r'):#JUST BELOW CHOICE
                        add = input("ENTER ADDRESS")
                        cur.execute('update employees set address = :1 where empid = :2',(add,empid))
                        cur.execute('commit')
                        print("ADDRESS SUCCESSFULLY CHANGED TO : ",add)
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                elif choice == '4':
                    while(option == 'r'):#JUST BELOW CHOICE
                        dob = input("ENTER DATE OF BIRTH dd/mm/yyyy")
                        chk = valid.validDate(dob)
                        if chk:
                            mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                            a,b,c = re.split("[./-]",dob)
                            dob = a+"/"+mon[int(b)]+"/"+c
                            cur.execute('update employees set DOB = :1 where empid = :2',(dob,empid))
                            cur.execute('commit')
                            print("DATE OF BIRTH SUCCESSFULLY CHANGED TO : ",dob)
                        else:
                            print("DATE NOT VALID ! PLEASE TRY AGAIN !!")
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                elif choice == '5':
                    while(option == 'r'):#JUST BELOW CHOICE
                        gender = input("ENTER YOUR GENDER Male/Female/Other")
                        gender = gender.upper()
                        if gender in ['MALE','FEMALE','OTHER']:
                            cur.execute('update employees set GENDER = :1 where empid = :2',(gender,empid))
                            cur.execute('commit')
                            print("GENDER SUCCESSFULLY CHANGED TO : ",gender)
                        else:
                            print("PLEASE ENTER A VALID GENDER AND TRY AGAIN!!")
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                        
                        
                elif choice == '6':
                    while(option == 'r'):#JUST BELOW CHOICE
                        dob = input("ENTER DATE OF JOINING dd/mm/yyyy")
                        chk = valid.validDate(dob)
                        if chk:
                            mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                            a,b,c = re.split("[./-]",dob)
                            dob = a+"/"+mon[int(b)]+"/"+c
                            cur.execute('update employees set DOJ = :1 where empid = :2',(dob,empid))
                            cur.execute('commit')
                            print("DATE OF JOINING SUCCESSFULLY CHANGED TO : ",dob)
                        else:
                            print("DATE NOT VALID ! PLEASE TRY AGAIN !!")
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                else:
                    break
            else:
                print("PLEASE ENTER A VALID OPTION AND TRY AGAIN !!")
        return  choice.lower()                
        
def changeEmployeeDetailsByAdmin(empid, cur):#TESTED
    #LET THE ADMIN CHANGE CASHIER/MANAGER/ADMIN DETAILS
    cur.execute('select designation from employees where empid=:1',(empid,))
    res = cur.fetchall()
    res = res[0][0]
    des = res
    cur.execute('select name from employees where empid=:1',(empid,))
    res = cur.fetchall()
    res = res[0][0]
    print("NAME : ",res)
    print("EMPLOYEE ID : ",empid)
    print("DESIGNATION : ",des)
    print()
    msg = """
    ENTER :
    1 =======> CHANGE NAME
    2 =======> CHANGE MOBILE NUMBER
    3 =======> CHANGE ADDRESS
    4 =======> CHANGE DATE OF BIRTH
    5 =======> CHANGE GENDER
    6 =======> CHANGE DATE OF JOINING
    7 =======> CHANGE PASSWORD
    8 =======> CHANGE SALARY
    9 =======> CHANGE DESIGNATION
    
    q =======> GO BACK
    m =======> GO TO MAIN MENU
    """
    choice = ''
    while(True):
        msgoption = """
            ENTER : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            """
        option = 'r'
        choice = input(msg)
        if choice in ['1','2','3','4','5','6','7','8','9','q','Q','m','M']:
            if choice == '1':
                while(option == 'r'):#JUST BELOW CHOICE
                    name = input("ENTER NEW NAME")
                    chk = valid.validName(name)
                    if chk:
                        
                        cur.execute('update employees set name = :1 where empid = :2',(name,empid))
                        cur.execute('commit')
                        print("NAME SUCCESSFULLY CHANGED TO : ",name)
                    else:
                        print("INVALID NAME PLEASE TRY AGAIN !!")
                    while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                    
                    
            elif choice == '2':
                while(option == 'r'):#JUST BELOW CHOICE
                    mob = input("ENTER MOBILE NUMBER")
                    chk = valid.validMobile(mob)
                    if chk:
                        cur.execute('update employees set mobile = :1 where empid = :2',(mob,empid))
                        cur.execute('commit')
                        print("MOBILE NUMBER SUCCESSFULLY CHANGED TO : ",mob)
                    else:
                        print("PLEASE ENTER A VALID MOBILE NUMBER AND TRY AGAIN !!")
                    while(True):#WITHIN CHOICE LOOP
                                    option = input(msgoption)
                                    option = option.lower()
                                    if option in  ['q','m','r']:
                                        if option == 'q':
                                                break
                                        elif option == 'm':
                                            return 'm'
                                        elif option =='r':
                                            print("RELOADED ")
                                            break
                                    else:
                                        print("PLEASE ENTER A VALID OPTION")
            elif choice == '3':
                while(option == 'r'):#JUST BELOW CHOICE
                    add = input("ENTER ADDRESS")
                    cur.execute('update employees set address = :1 where empid = :2',(add,empid))
                    cur.execute('commit')
                    print("ADDRESS SUCCESSFULLY CHANGED TO : ",add)
                    while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
            elif choice == '4':
                while(option == 'r'):#JUST BELOW CHOICE
                    dob = input("ENTER DATE OF BIRTH dd/mm/yyyy")
                    chk = valid.validDate(dob)
                    if chk:
                        mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                        a,b,c = re.split("[./-]",dob)
                        dob = a+"/"+mon[int(b)]+"/"+c
                        cur.execute('update employees set DOB = :1 where empid = :2',(dob,empid))
                        cur.execute('commit')
                        print("DATE OF BIRTH SUCCESSFULLY CHANGED TO : ",dob)
                    else:
                        print("DATE NOT VALID ! PLEASE TRY AGAIN !!")
                    while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
            elif choice == '5':
                while(option == 'r'):#JUST BELOW CHOICE
                    gender = input("ENTER YOUR GENDER Male/Female/Other")
                    gender = gender.upper()
                    if gender in ['MALE','FEMALE','OTHER']:
                        cur.execute('update employees set GENDER = :1 where empid = :2',(gender,empid))
                        cur.execute('commit')
                        print("GENDER SUCCESSFULLY CHANGED TO : ",gender)
                    else:
                        print("PLEASE ENTER A VALID GENDER AND TRY AGAIN!!")
                    while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                    
            elif choice == '6':
                while(option == 'r'):#JUST BELOW CHOICE
                    dob = input("ENTER DATE OF JOINING dd/mm/yyyy")
                    chk = valid.validDate(dob)
                    if chk:
                        mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                        a,b,c = re.split("[./-]",dob)
                        dob = a+"/"+mon[int(b)]+"/"+c
                        cur.execute('update employees set DOJ = :1 where empid = :2',(dob,empid))
                        cur.execute('commit')
                        print("DATE OF JOINING SUCCESSFULLY CHANGED TO : ",dob)
                    else:
                        print("DATE NOT VALID ! PLEASE TRY AGAIN !!")
                    while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                    
            elif choice == '7':
                while(option == 'r'):#JUST BELOW CHOICE
                    new_pass1 = input("ENTER NEW PASSWORD")
                    chk = False
                    while(not chk):
                        chk = valid.validPassword(new_pass1)
                        if chk:
                            break
                        print("ENTER PASSWORD AGAIN")
                        new_pass1 = input()
                    
                    print("PASSWORD CHECKED")
                    print("CONFIRM YOUR PASSWORD")
                    new_pass2 = input()
                    if new_pass1 == new_pass2:
                        cur.execute('update employees set password = :1 where empid = :2',(new_pass2,empid))
                        cur.execute('commit')
                        print("PASSWORD SUCCESSFULLY CHANGED")
                    else:
                        print("PASSWORD CANNOT BE CHANGED, PLEASE TRY AGAIN !!")
                    while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
              
            elif choice == '8':
                while(option == 'r'):#JUST BELOW CHOICE
                    sal = input("ENTER SALARY")
                    chk = valid.validSalary(sal)
                    if chk:
                        cur.execute('update employees set salary = :1 where empid = :2',(sal,empid))
                        cur.execute('commit')
                        print("SALARY SUCCESSFULLY CHANGED TO : ",sal)
                    else:
                        print("INVALID SALARY ENETRED ! SHOULD BE NUMERIC ONLY !!")
                    while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                    
            elif choice == '9':
                while(option == 'r'):#JUST BELOW CHOICE
                    des = input("ENTER DESIGNATION CASHIER/MANAGER/ADMIN OR 1/2/3")
                    des = des.upper()
                    if des in ['CASHIER','MANAGER','ADMIN','1','2','3']:
                        if des == '1':
                            des = 'CASHIER'
                        if des == '2':
                            des = 'MANAGER'
                        if des == '3':
                            des = 'ADMIN'
                        cur.execute('update employees set designation = :1 where empid = :2',(des,empid))
                        cur.execute('commit')
                        print("DESIGNATION SUCCESSFULLY CHANGED TO : ",des)
                    else:
                        print("PLEASE ENTER A VALID DESIGNATION AND TRY AGAIN")
                    while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                    
            else:
                break
        else:
            print("PLEASE ENTER A VALID OPTION AND TRY AGAIN !!")
    return  choice.lower()             
    
def changeMenuSingle(prid, cur):#TESTED
    #LETS MANAGER AND ADMIN EDIT THE MENU
    cur.execute("select * from menu where prid=:1",(prid,))
    res = cur.fetchall()
    if res == []:
        print("SORRY NO SUCH PRODUCT EXISTS")
        return "q"
    else:
        print("PRODUCT DETAILS : ")
        res = res[0]
        print("PRODUCT ID: ",res[0],"PRODUCT NAME : ",res[1],"SHORTCUT : ",res[5],"TYPE : ",res[6])
        print("PRICE-    SMALL: ",res[2],"    MEDIUM: ",res[3],"    LARGE: ",res[4])
        print("DETAILS : ",res[7])
        print()
        msg = """
        ENTER :
        1 =======> CHANGE PRODUCT NAME
        2 =======> CHANGE PRICE FOR SMALL
        3 =======> CHANGE PRICE FOR MEDIUM
        4 =======> CHANGE PRICE FOR LARGE
        5 =======> CHANGE SHORTCUT
        6 =======> CHANGE TYPE
        7 =======> CHANGE DETAILS
        
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        """
        while(True):
            msgoption = """
            ENTER : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            """
            option = 'r'
            choice = input(msg)
            if choice in ['1','2','3','4','5','6','7','q','Q','m','M']:
                choice = choice.lower()
                if choice == '1':
                    while(option == 'r'):#JUST BELOW CHOICE
                        new_pname = input("ENTER NEW PRODUCT NAME")
                        chk = valid.validPizzaNameandDetails(new_pname)
                        if not chk:
                            print("INVALID PRODUCT NAME")
                            print("PRODUCT NAME SHOULD CONTAIN LETTER,DIGITS,SPACES ONLY")
                            print("PLEASE TRY AGAIN !!")
                        else:
                            new_pname = new_pname.upper()
                            cur.execute('update menu set name=:1 where prid=:2',(new_pname,prid))
                            cur.execute('commit')
                            print("NAME SUCCESSFULLY CHANGED TO : ",new_pname)
                        while(True):#WITHIN CHOICE LOOP
                            option = input(msgoption)
                            option = option.lower()
                            if option in  ['q','m','r']:
                                if option == 'q':
                                        break
                                elif option == 'm':
                                    return 'm'
                                elif option =='r':
                                    print("RELOADED ")
                                    break
                            else:
                                print("PLEASE ENTER A VALID OPTION")
                elif choice == '2':
                    while(option == 'r'):#JUST BELOW CHOICE
                        price = input("ENTER PRICE FOR SMALL")
                        chk = valid.validNumber(price)
                        if not chk:
                            print("INVALID PRICE ! SHOULD CONTAIN ONLY DIGITS !!")
                        else:
                            cur.execute('update menu set price_s=:1 where prid=:2',(price,prid))
                            cur.execute('commit')
                            print("PRICE FOR SMALL SUCCESSFULLY CHANGED TO : ",price)
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                elif choice == '3':
                    while(option == 'r'):#JUST BELOW CHOICE
                        price = input("ENTER PRICE FOR MEDIUM")
                        chk = valid.validNumber(price)
                        if not chk:
                            print("INVALID PRICE ! SHOULD CONTAIN ONLY DIGITS !!")
                        else:
                            cur.execute('update menu set price_m=:1 where prid=:2',(price,prid))
                            cur.execute('commit')
                            print("PRICE FOR MEDIUM SUCCESSFULLY CHANGED TO : ",price)
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                elif choice == '4':
                    while(option == 'r'):#JUST BELOW CHOICE
                        price = input("ENTER PRICE FOR LARGE")
                        chk = valid.validNumber(price)
                        if not chk:
                            print("INVALID PRICE ! SHOULD CONTAIN ONLY DIGITS !!")
                        else:
                            cur.execute('update menu set price_l=:1 where prid=:2',(price,prid))
                            cur.execute('commit')
                            print("PRICE FOR LARGE SUCCESSFULLY CHANGED TO : ",price)
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                        
                elif choice == '5':
                    while(option == 'r'):#JUST BELOW CHOICE
                        shrt = input("ENTER SHORTCUT")
                        if len(shrt)>9:
                            print("SHORTCUT TOO LARGE")
                        else:
                            try:
                                cur.execute('update menu set shortcut=:1 where prid=:2',(shrt,prid))
                            #res = cur.fetchall()
                            #print(res)
                            except:
                                print("SHORTCUT ALREADY EXISTS")
                            else:
                                cur.execute('commit')
                                print("SHORTCUT SUCCESSFULLY CHANGED TO : ",shrt)
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                        
                elif choice == '6' :
                    while(option == 'r'):#JUST BELOW CHOICE
                        typ = input("ENTER TYPE AS VEG/NON-VEG OR N/V 0R 1/2")
                        typ = typ.upper()
                        if typ in ["VEG","NON-VEG","N","V","1","2"]:
                            if typ == "1" or typ == "V":
                                typ = "VEG"
                            elif typ == '2' or typ == 'N':
                                typ = "NON-VEG"
                            cur.execute('update menu set type=:1 where prid=:2',(typ,prid))
                            cur.execute('commit')
                            print("TYPE SUCCESSFULLY CHANGED TO : ",typ)
                        else:
                            print("PLEASE ENTER CORRECT CHOICE AND TRY AGAIN!!")
                        while(True):#WITHIN CHOICE LOOP
                                option = input(msgoption)
                                option = option.lower()
                                if option in  ['q','m','r']:
                                    if option == 'q':
                                            break
                                    elif option == 'm':
                                        return 'm'
                                    elif option =='r':
                                        print("RELOADED ")
                                        break
                                else:
                                    print("PLEASE ENTER A VALID OPTION")
                            
                elif choice == '7':
                    while(option == 'r'):#JUST BELOW CHOICE
                        det = input("ENTER DETAILS")
                        chk = valid.validPizzaNameandDetails(det)
                        if not chk:
                            print("DETAILS SHOULD BE ONLY CHARACTERS, NUMBERS AND SPACES")
                            print("INVALID DETAIL PLEASE TRY AGAIN!!")
                            
                        else:
                            cur.execute('update menu set details=:1 where prid=:2',(det,prid))
                            cur.execute('commit')
                            print("DETAILS SUCCESSFULLY CHANGED TO : ",det)
                        while(True):#WITHIN CHOICE LOOP
                                    option = input(msgoption)
                                    option = option.lower()
                                    if option in  ['q','m','r']:
                                        if option == 'q':
                                                break
                                        elif option == 'm':
                                            return 'm'
                                        elif option =='r':
                                            print("RELOADED ")
                                            break
                                    else:
                                        print("PLEASE ENTER A VALID OPTION")
                else:
                    break
           
            else:
                print("PLEASE ENTER A VALID OPTION AND TRY AGAIN !!")
        return  choice.lower()   
                
def changeShortcut(cur):#TESTED
    #LETS MANAGER AND ADMIN CHANGE THE SHORTCUTS
    cur.execute('select prid,name,shortcut from menu order by prid')
    res = cur.fetchall()
    lid = []
    linm = []
    print("  =======    =======  MENU  =======    =======  ")
    print("PRODUCT_ID \t\t NAME \t\t SHORTCUT")
    for tup in res:
        #print(type(tup[0]))
        lid.append(tup[0])
        linm.append(tup[1])
        print(tup[0],"\t\t",tup[1],"\t\t",tup[2])
    print("\n\n")
    msgoption = """
            ENTER : 
            d =======> DONE
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            """             
    print(msgoption)
    print("ENTER ID or NAME with corresponding SHORTCUT to change e.g. 'ID @ SHORTCUT' or 'NAME @ SHORTCUT'")
    while(True):
        ch = input()
        ch = ch.lower()
        if ch in ['d','q','m']:
            if ch == 'd':
                cur.execute('select prid,name,shortcut from menu order by prid')
                res = cur.fetchall()
                print("CHANGED MENU IS : ")
                print("  =======    =======  MENU  =======    =======  ")
                print("PRODUCT_ID \t\t NAME \t\t SHORTCUT")
                for tup in res:
                    print(tup[0],"\t\t",tup[1],"\t\t",tup[2])
                while(True):
                    msgoption = """
                    ENTER : 
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    """             
                    ch2 = input(msgoption)
                    ch2 = ch2.lower()
                    if ch2 in ['q','m']:
                        return ch2
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")
            else:
                return ch
        else:
            short = ch.split('@')
            if len(short) != 2:
                print("PLEASE PROVIDE EXACTLY 2 PARAMETERS AND TRY AGAIN !!")
            else:
                name,shrt = short
                name = name.strip()
                shrt = shrt.strip()
                if valid.validNumber(name):
                    if int(name) in lid:
                        if len(shrt) > 9:
                            print("SHORTCUT TOO LARGE ! PLEASE ENTER A SMALLER SHORTCUT !!")
                        else:
                            try :
                                cur.execute('update menu set shortcut=:1 where prid=:2',(shrt,int(name)))
                                
                            except :
                                print("SHORTCUT ALREADY EXISTS !!")
                            else:
                                cur.execute('commit')
                                print("SHORTCUT CHANGED SUCCESFULLY TO : ",shrt)
                    else:
                        print("NO SUCH ID EXISTS !!")
                elif name.upper() in linm:
                    if len(shrt) > 9:
                        print("SHORTCUT TOO LARGE ! PLEASE ENTER A SMALLER SHORTCUT !!")
                    else:
                        try :
                            cur.execute('update menu set shortcut=:1 where name=:2',(shrt,name))
                            
                        except :
                            print("SHORTCUT ALREADY EXISTS !!")
                        else:
                            cur.execute('commit')
                            print("SHORTCUT CHANGED SUCCESFULLY TO : ",shrt)
                else:
                    print("INVALID ID OR NAME ! PLEASE TRY AGAIN !!")
        print(msgoption)
        print("ENTER ID or NAME with corresponding SHORTCUT to change e.g. 'ID @ SHORTCUT' or 'NAME @ SHORTCUT'")
 
def changeDiscount(prid, dis, cur):#TESTED
    #IT WILL BE USED BY OTHER FUNCTIONS SO NOT PRONE TO WRONG INPUT
    dis = int(dis)
    dis = dis/100
    cur.execute('select price_s,price_m,price_l from menu where prid=:1',(prid,))
    res = cur.fetchall()
    res = res[0]
    s,m,l = res
    s = int(s)
    m = int(m)
    l = int(l)
    dis1 = int(s - s*dis)
    dis2 = int(m - m*dis)
    dis3 = int(l - l*dis)
    cur.execute('update menu set price_s=:1,price_m=:2,price_l=:3 where prid=:4',(dis1,dis2,dis3,prid))
    cur.execute('commit')
    
def changeOffers(specific, cur):#TESTED
    #SPECIFIC IN ALL or ONE
    msgoption = """
    ENTER : 
    r =======> RETRY
    d =======> DONE
    q =======> GO BACK
    m =======> GO TO MAIN MENU """
    
    cur.execute('select prid,name,shortcut,price_s,price_m,price_l from menu order by prid')
    res = cur.fetchall()
    lid = []
    linm = []
    print("=======    =======   =======    =======  MENU  =======    =======  =======    ======= ")
    print("PRODUCT_ID \t\t NAME \t\t SHORTCUT \t\t SMALL \t\t MEDIUM \t\t LARGE")
    for tup in res:
        #print(type(tup[0]))
        lid.append(tup[0])
        linm.append(tup[1])
        print(tup[0],"\t\t",tup[1],"\t\t",tup[2],"\t\t",tup[3],"\t\t",tup[4],"\t\t",tup[5])
    specific = specific.lower()
    opt = 'r'
    if specific == 'all':
        while(True):
            if opt == 'r':
                print("ENTER OFFERED DISCOUNT ")
                dis = input()
                chk = valid.validNumber(dis)
                if not chk:
                    print("NOT VALID DISCOUNT VALUE")
                else:
                    dis = int(dis)
                    if dis>100:
                        print("DISCOUNT CANNOT BE GREATER THAN 100% !")
                    else:
                        cur.execute('select prid from menu')
                        res = cur.fetchall()
                        for tup in res:
                            prid = tup[0]
                            changeDiscount(prid, dis, cur)
                        print("DISCOUNT APPLIED SUCCESSFULLY !")
            elif opt == 'q' or opt == 'm':
                return opt
            elif opt == 'd':
                break
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            print(msgoption)
            opt = input()
            opt = opt.lower()
        cur.execute('select prid,name,shortcut,price_s,price_m,price_l from menu order by prid')
        res = cur.fetchall()
        print("=======    =======   =======    =======  MENU  =======    =======  =======    ======= ")
        print("PRODUCT_ID \t\t NAME \t\t SHORTCUT \t\t SMALL \t\t MEDIUM \t\t LARGE")
        for tup in res:
            #print(type(tup[0]))
            print(tup[0],"\t\t",tup[1],"\t\t",tup[2],"\t\t",tup[3],"\t\t",tup[4],"\t\t",tup[5])
        msgoption = """
        ENTER : 
       
        q =======> GO BACK
        m =======> GO TO MAIN MENU """
        while(True):
            ch = input(msgoption)
            ch = ch.lower()
            if ch in ['q','m']:
                return ch
            else:
                print("PLEASE ENTER A VALID OPTION AND TRY AGAIN !!")
    elif specific == 'one':
        cur.execute('select prid,name,shortcut from menu')
        lpr = []
        lnm = []
        lshr = []
        res = cur.fetchall()
        for tup in res:
            lpr.append(str(tup[0]).upper())
            lnm.append(str(tup[1]).upper())
            lshr.append(str(tup[2]))
        while(True):
            if opt == 'r':
                prid = input("ENTER ID or NAME or SHORTCUT")
                xpd = prid
                prid = prid.upper()
                
                if prid in lpr:
                    print("ENTER OFFERED DISCOUNT ")
                    dis = input()
                    chk = valid.validNumber(dis)
                    if not chk:
                        print("NOT VALID DISCOUNT VALUE")
                    else:
                        dis = int(dis)
                        if dis>100:
                            print("DISCOUNT CANNOT BE GREATER THAN 100% !")
                        else:
                            cur.execute('select price_s,price_m,price_l from menu where prid=:1',(int(prid),))
                            res = cur.fetchall()
                            res = res[0]
                            sb,mb,lb = res
                            changeDiscount(prid, dis, cur)
                            cur.execute('select price_s,price_m,price_l from menu where prid=:1',(int(prid),))
                            res = cur.fetchall()
                            res = res[0]
                            sa,ma,la = res
                            print("DISCOUNT OFFERED SUCCESSFULLY !!")
                            print("PRICE CHANGED FROM S:",sb," M:",mb," L:",lb," TO S:",sa," M:",ma," L:",la)
                elif prid in lnm:
                    print("ENTER OFFERED DISCOUNT ")
                    dis = input()
                    chk = valid.validNumber(dis)
                    if not chk:
                        print("NOT VALID DISCOUNT VALUE")
                    else:
                        dis = int(dis)
                        if dis>100:
                            print("DISCOUNT CANNOT BE GREATER THAN 100% !")
                        else:
                            cur.execute('select price_s,price_m,price_l from menu where name=:1',(prid,))
                            res = cur.fetchall()
                            res = res[0]
                            sb,mb,lb = res
                            cur.execute('select prid from menu where name=:1',(prid,))
                            res  =cur.fetchall()
                            pr = res[0][0]
                            changeDiscount(pr, dis, cur)
                            cur.execute('select price_s,price_m,price_l from menu where name=:1',(prid,))
                            res = cur.fetchall()
                            res = res[0]
                            sa,ma,la = res
                            
                            
                            print("DISCOUNT OFFERED SUCCESSFULLY !!")
                            print("PRICE CHANGED FROM S:",sb," M:",mb," L:",lb," TO S:",sa," M:",ma," L:",la)
                elif xpd in lshr:
                    print("ENTER OFFERED DISCOUNT ")
                    dis = input()
                    chk = valid.validNumber(dis)
                    if not chk:
                        print("NOT VALID DISCOUNT VALUE")
                    else:
                        dis = int(dis)
                        if dis>100:
                            print("DISCOUNT CANNOT BE GREATER THAN 100% !")
                        else:
                            cur.execute('select price_s,price_m,price_l from menu where shortcut=:1',(xpd,))
                            res = cur.fetchall()
                            res = res[0]
                            sb,mb,lb = res
                            cur.execute('select prid from menu where shortcut=:1',(xpd,))
                            res  =cur.fetchall()
                            pr = res[0][0]
                            changeDiscount(pr, dis, cur)
                            cur.execute('select price_s,price_m,price_l from menu where shortcut=:1',(xpd,))
                            res = cur.fetchall()
                            res = res[0]
                            sa,ma,la = res
                            
                            
                            print("DISCOUNT OFFERED SUCCESSFULLY !!")
                            print("PRICE CHANGED FROM S:",sb," M:",mb," L:",lb," TO S:",sa," M:",ma," L:",la)
                else:
                    print("NO SUCH DETAILS EXISTS ! PLEASE TRY AGAIN !!")
                print(msgoption)
                opt = input()
                opt = opt.lower()
            elif opt == 'd':
                break
            elif opt == 'q' or opt == 'm':
                return opt
            else:
                print("INVALID CHOICE ! PLEASE TRY AGAIN !!")
                opt = 'r'
        cur.execute('select prid,name,shortcut,price_s,price_m,price_l from menu order by prid')
        res = cur.fetchall()
        print("=======    =======   =======    =======  MENU  =======    =======  =======    ======= ")
        print("PRODUCT_ID \t\t NAME \t\t SHORTCUT \t\t SMALL \t\t MEDIUM \t\t LARGE")
        for tup in res:
            #print(type(tup[0]))
            print(tup[0],"\t\t",tup[1],"\t\t",tup[2],"\t\t",tup[3],"\t\t",tup[4],"\t\t",tup[5])
        msgoption = """
        ENTER : 
   
        q =======> GO BACK
        m =======> GO TO MAIN MENU """
        while(True):
            ch = input(msgoption)
            ch = ch.lower()
            if ch in ['q','m']:
                return ch
            else:
                print("PLEASE ENTER A VALID OPTION AND TRY AGAIN !!")
    else:
        print("SYSTEM ERROR ! PLEASE SELECT A VALID OPTION IN 'ALL' or 'SPECIFIC'")
        
def changeEmployeeStatusFire(specific, cur):#TESTED
    #ASKS FOR AN EMPLOYEE AND FIRE HIM OR REHIRE HIM
    specific =specific.upper()
    if specific in ['REHIRE','FIRE']:
        while(True):
            print("ENTER EMPLOYEE ID : ")
            empid = input()
            chk = valid.validNumber(empid)
            if chk:
                empid = int(empid)
                choice = ''
                cur.execute('select empid from employees ')
                res =cur.fetchall()
                
                loemp = []
                for tup in res:
                    loemp.append(tup[0])
                if empid not in loemp:
                    #print(loemp)
                    print("EMPLOYEE ID DOES'NT EXIST ! PLEASE TRY AGAIN !!")
                else:
                    view.viewDetailsEmployee(empid, cur)
                    msg = """
                                    ENTER : 
                                    r =======> RETRY
                                    c =======> CONFIRM
                                    q =======> GO BACK
                                    m =======> GO TO MAIN MENU
                                    """
                    while(True):
                        choice = input(msg)
                        choice = choice.lower()
                        if choice in ['r','c','q','m']:
                            if choice == 'r':
                                break
                            elif choice == 'c':
                                doin = datetime.datetime.now().date()
                                mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                                a,b,c = re.split("[./-]",str(doin))
                                doin = c+"/"+mon[int(b)]+"/"+a
                                if specific == 'FIRE':
                                    cur.execute("update employees set status= 'INACTIVE' where empid=:1",(empid,))
                                   
                                    
                                    cur.execute("update employees set doin=:1 where empid=:2",(doin,empid))
                                    cur.execute('commit')
                                    print("EMPLOYEE FIRED ! SUCCESSFULLY !!")
                                else:
                                    cur.execute("update employees set status= 'ACTIVE' where empid=:1",(empid,))
                                    cur.execute("update employees set doin=null,doj=:1 where empid=:2",(doin,empid))
                                    cur.execute('commit')
                                    print("EMPLOYEE RE-HIRED ! SUCCESSFULLY !!")
                                break
                            else :
                                return choice
                        else:
                            print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                if choice == 'c':
                    while(True):
                        msg = """
                                    ENTER : 
                                    r =======> RETRY
                                    d =======> DISPLAY
                                    q =======> GO BACK
                                    m =======> GO TO MAIN MENU
                                    """
                        ch = input(msg)
                        ch = ch.lower()
                        if ch in ['r','d','q','m']:
                            if ch == 'r':
                                break
                            elif ch == 'd':
                                view.viewDetailsEmployee(empid, cur)
                                while(True):
                                    msg = """
                                    ENTER : 
                                    
                                    q =======> GO BACK
                                    m =======> GO TO MAIN MENU
                                    """
                                    ch = input(msg)
                                    ch = ch.lower()
                                    if ch in ['q','m']:
                                        return ch
                                    else:
                                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                            else:
                                return ch
                        else:
                            print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")                           
    else:
        print("SYSTEM ERROR ! SPECIFIC SHOULD BE IN 'REHIRE OR FIRE' ")
                            
def changeEmployeeLock(specific,numberEmp,des, cur):#TESTED
    #CHANGE 'ALL' or 'ONE' EMPLOYEE'S LOCK TO EITHER 'LOCKED' or 'UNLOCKED' 
    #CHANGED BY 'MANAGER' OR 'ADMIN'
    specific = specific.upper()
    numberEmp = numberEmp.upper()
    des = des.upper()
    if specific in ['LOCKED','UNLOCKED'] and numberEmp in['ONE','ALL'] and des in ['MANAGER','ADMIN']:
        if numberEmp == 'ALL':
            if des == 'ADMIN':
                cur.execute("update employees set locks=:1 where designation!='ADMIN' ",(specific,))
                cur.execute('commit')
                if specific == 'LOCKED':
                    print("ALL EMPLOYEES SUCCESSFULLY LOCKED EXCEPT 'ADMIN' ")
                else:
                    print("ALL EMPLOYEES SUCCESSFULLY UNLOCKED ")
            else:
                
                if specific == 'LOCKED':
                    cur.execute("update employees set locks='LOCKED' where designation='CASHIER' ")
                    cur.execute('commit')
                    print("ALL EMPLOYEES SUCCESSFULLY LOCKED -> CASHIER ")
                else:
                    cur.execute("update employees set locks='UNLOCKED' where designation='CASHIER'")
                    cur.execute('commit')
                    print("ALL EMPLOYEES SUCCESSFULLY UNLOCKED -> CASHIER")
            while(True):
                        msg = """
                                    ENTER : 
                                    
                                    d =======> DISPLAY
                                    q =======> GO BACK
                                    m =======> GO TO MAIN MENU
                                    """
                        ch = input(msg)
                        ch = ch.lower()
                        if ch in ['d','q','m']:
                            
                            if ch == 'd':
                                view.viewDetailsEmployeeAll('ACTIVE',des, cur)
                                while(True):
                                    msg = """
                                    ENTER : 
                                    
                                    q =======> GO BACK
                                    m =======> GO TO MAIN MENU
                                    """
                                    ch = input(msg)
                                    ch = ch.lower()
                                    if ch in ['q','m']:
                                        return ch
                                    else:
                                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                            else:
                                return ch
                        else:
                            print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
        else:
            while(True):
                cur.execute("select empid from employees")
                res = cur.fetchall()
                loempid = []
                for i in res:
                    loempid.append(str(i[0]))
                print("ENTER EMPLOYEE ID : ")
                empid = input()
                choice = ''
                chk = valid.validNumber(empid)
                if chk:
                    if empid in loempid:
                        
                        cur.execute('select designation from employees where empid=:1',(empid,))
                        res = cur.fetchall()
                        design = res[0][0]
                        chk = False
                        if des == 'MANAGER':
                            
                            if design == 'CASHIER':
                                chk = True
                            else:
                                chk = False
                          
                                
                        else:
                            if specific == 'LOCKED':
                                if design == 'ADMIN':
                                    chk = False
                                else:
                                    chk = True
                            else:
                                chk = True
                        if chk:
                            view.viewDetailsEmployee(empid, cur)
                            msg = """
                                            ENTER : 
                                            r =======> RETRY
                                            c =======> CONFIRM
                                            q =======> GO BACK
                                            m =======> GO TO MAIN MENU
                                            """
                            while(True):
                                choice = input(msg)
                                choice = choice.lower()
                                if choice in ['r','c','q','m']:
                                    if choice == 'r':
                                        break
                                    elif choice == 'c':
                                        cur.execute("update employees set locks=:1 where empid=:2",(specific,empid))
                                        cur.execute('commit')
                                        
                                        print("EMPID ",empid," SUCCESSFULY ",specific)
                                    
                                        break
                                    else :
                                        return choice
                                else:
                                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        else:
                            print("YOU ARE NOT AUTHORIZED TO CHANGE THIS ACCOUNT ! PLEASE TRY AGAIN !!")
                            choice = 'c'
                    else:
                        print("EMPLOYEE ID DOES NOT EXIST ! PLEASE TRY AGAIN !!")
                        choice = 'c'      
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                if choice == 'c':
                    while(True):
                        msg = """
                                    ENTER : 
                                    r =======> RETRY
                                    d =======> DISPLAY
                                    q =======> GO BACK
                                    m =======> GO TO MAIN MENU
                                    """
                        ch = input(msg)
                        ch = ch.lower()
                        if ch in ['r','d','q','m']:
                            if ch == 'r':
                                break
                            elif ch == 'd':
                                view.viewDetailsEmployee(empid, cur)
                                while(True):
                                    msg = """
                                    ENTER : 
                                    
                                    q =======> GO BACK
                                    m =======> GO TO MAIN MENU
                                    """
                                    ch = input(msg)
                                    ch = ch.lower()
                                    if ch in ['q','m']:
                                        return ch
                                    else:
                                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                            else:
                                return ch
                        else:
                            print("INVALID INPUT ! PLEASE TRY AGAIN !!")
        
    else:
        print("SYSTEM ERROR ! EITHER SPECIFIC OR CHOICE IN NOT VALID !!")                              
                
def changeEmployeeLockLogin(empid, cur):#TESTED
    #LOCKS THE EMPID SENT BY LOGIN AND CHEKS FOR NOT OF 'ADMIN'
    cur.execute('select designation from employees where empid=:1',(empid,))
    res = cur.fetchall()
    des = res[0][0]
    if des == 'ADMIN':
        print("SYSTEM ERROR! CANNOT LOCK ADMIN !!")
    else:
        cur.execute("update employees set locks='LOCKED' where empid=:1",(empid,))
        cur.execute('commit')
        print("YOUR ACCOUNT HAS BEEN LOCKED !!")
        print("CONTACT YOUR ADMIN OR MANAGER !!")
        
def removePizza(cur):
    cur.execute('select prid,name,shortcut from menu')
    res = cur.fetchall()
    lop = []
    for tup in res:
        x = [str(tup[0]),tup[1].upper(),tup[2].upper()]
        lop.append(x)
    opt = 'r'
    while(True):
        if opt == 'r':
            prid = input("ENTER ID or NAME or SHORTCUT OF PIZZA TO BE REMOVED : \n\n")
            prid = prid.upper()
            chk = False
            for li in lop:
                if prid in li:
                    chk = True
                    prid = int(li[0])
                    break
            if chk:
                while(True):
                    view.viewMenu(prid, cur)
                    msg = """
                    ENTER : 
                    r =======> RETRY
                    c =======> CONFIRM
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['r','c','q','m']:
                        if opt == 'r':
                            break
                        elif opt == 'c':
                            cur.execute("select max(prid) from menu")
                            res = cur.fetchall()
                            res = res[0][0]
                            if prid == res:
                                cur.execute("delete from menu where prid=:1",(prid,))
                            else:
                                cur.execute("delete from menu where prid=:1",(prid,))
                                cur.execute("update menu set prid=:1 where prid=:2",(prid,res))
                            cur.execute("commit")
                            print("\nPIZZA DELETED SUCCESSFULLY :  ",prid,"\n")
                            break
                        else:
                            return opt
                    else:
                        return opt
            else:
                print("PIZZA DOES NOT EXIST ! PLEASE TRY AGAIN !!\n\n")
                
        elif opt == 'c':
            while(True):
                    msg = """
                    ENTER : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['r','q','m']:
                        if opt == 'r':
                            break
                        else:
                            return opt
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!\n\n")
        else:
            return opt
        
