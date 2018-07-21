import validation as valid
import view
import re
import datetime


def createCustomerAccount(cur):#TESTED
    #CREATES CUSTOMER ACCOUNT AND RETURN CUSTOMER-ID
    name, mob, gender = '','',''
    
    while(True):
        name = input("ENTER YOUR NAME : ")
        chk = valid.validName(name)
        if chk:
            break
        else:
            print("INVALID NAME ! PLEASE TRY AGAIN !!")
    
    cur.execute('select mobile from customers')
    res = cur.fetchall()
    lmob = []
    for tup in res:
        lmob.append(str(tup[0]))
    while(True):
        mob = input("ENTER MOBILE NUMBER : ")
        chk = valid.validMobile(mob)
        if chk:
            if mob in lmob :
                print("MOBILE NUMBER ALREADY EXISTS !!")
            else:
                break
        else:
            print("INVALID MOBILE NUMBER ! PLEASE TRY AGAIN !!")
    while(True):
        gender = input("ENTER GENDER AS MALE/FEMALE/OTHER or M/F/O : ")
        gender = gender.upper()
        if gender in ['MALE','FEMALE','OTHER','M','F','O']:
            if gender == 'M':
                gender = 'MALE'
            if gender == 'F':
                gender = 'FEMALE'
            if gender == 'O':
                gender = 'OTHER'
            break
        else:
            print("INVALID GENDER ! PLEASE TRY AGAIN !! ")
    cur.execute('insert into customers(name,mobile,gender) values(:1,:2,:3)',(name,mob,gender))
    cur.execute('commit')
    print("CUSTOMER ACCOUNT CREATED SUCCESSFULLY")
    return mob
                
def createEmployeeAccount(cur):#TESTED
    #CREATES EMPLOYEE ACCOUNT BY ADMIN 
    while(True):
        doj = datetime.datetime.now().date()
        mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
        a,b,c = re.split("[./-]",str(doj))
        doj = c+"/"+mon[int(b)]+"/"+a
        #print(doj)
        empid, name, mob, address, dob, password, salary, designation = '','','','','','','',''
        status = 'ACTIVE'
        cur.execute('select max(empid) from employees')
        res = cur.fetchall()
        empid = res[0][0] + 1
        while(True):
            name = input("ENTER EMPLOYEE NAME : ")
            chk = valid.validName(name)
            if chk:
                break
            else:
                print("INVALID NAME ! PLEASE TRY AGAIN !!")
        
        cur.execute('select mobile from employees')
        res = cur.fetchall()
        lmob = []
        for tup in res:
            lmob.append(str(tup[0]))
        while(True):
            mob = input("ENTER MOBILE NUMBER : ")
            chk = valid.validMobile(mob)
            if chk:
                if mob in lmob :
                    print("MOBILE NUMBER ALREADY EXISTS !!")
                else:
                    mob = int(mob)
                    break
            else:
                print("INVALID MOBILE NUMBER ! PLEASE TRY AGAIN !!")
        while(True):
            gender = input("ENTER GENDER AS MALE/FEMALE/OTHER or M/F/O : ")
            gender = gender.upper()
            if gender in ['MALE','FEMALE','OTHER','M','F','O']:
                if gender == 'M':
                    gender = 'MALE'
                if gender == 'F':
                    gender = 'FEMALE'
                if gender == 'O':
                    gender = 'OTHER'
                break
            else:
                print("INVALID GENDER ! PLEASE TRY AGAIN !! ")
        while(True):
            address = input("ENTER ADDRESS : ")
            if len(address)!=0:
                break
            else:
                print("ADDRESS CANNOT BE EMPTY ! PLEASE TRY AGAIN !!")
        while(True):
            dob = input("ENTER DATE OF BIRTH dd/mm/yyyy : ")
            chk = valid.validDate(dob)
            if chk:
                mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                a,b,c = re.split("[./-]",dob)
                dob = a+"/"+mon[int(b)]+"/"+c
                break
            else:
                print("INVALID DATE OF BIRTH ! PLEASE TRY AGAIN !!")
        while(True):
            salary = input("ENTER SALARY : ")
            chk = valid.validSalary(salary)
            if chk:
                salary = int(salary)
                break
            else:
                
                print("INVALID SALARY ! PLEASE TRY AGAIN !!")
        while(True):
            password = input("ENTER PASSWORD : or PRESS 'd' for DEFAULT PASSWORD GENERATION :: ")
            if password in ['d','D']:
                password = name + "1234" + "!@#$"
                break
            else:
                chk = valid.validPassword(password)
                if chk:
                    break
                else:
                    print("INVALID PASSWORD ! PLEASE TRY AGAIN !!")
        while(True):
            designation = input("ENTER DESIGNATION 'ADMIN/MANAGER/CASHIER' or 'A/M/C' or '1/2/3' ")
            designation = designation.upper()
            if designation in ['ADMIN','MANAGER','CASHIER','A','M','C','1','2','3']:
                if designation in ['A','1']:
                    designation = 'ADMIN'
                if designation in ['M','2']:
                    designation = 'MANAGER'
                if designation in ['C','3']:
                    designation = 'CASHIER'
                break
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
        cur.execute('insert into employees(empid,name,mobile,address,gender,dob,status,password,salary,designation,doj) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)',(empid,name,mob,address,gender,dob,status,password,salary,designation,doj))
        cur.execute('commit')
        print("EMPLOYEE CREATED SUCCESSFULLY ")
        msgoption = """
                ENTER : 
                r =======> RETRY
                d =======> DISPLAY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                """
        while(True):
                ch = input(msgoption)
                ch = ch.lower()
                if ch in ['r','d','q','m']:
                    if ch == 'd':
                        view.viewDetailsEmployee(empid, cur)
                        while(True):
                            msg = """
                                ENTER : 
                                r =======> RETRY
                                q =======> GO BACK
                                m =======> GO TO MAIN MENU
                                """
                            c = input(msg)
                            c = c.lower()
                            if c in ['q','m']:
                                return c
                            elif c == 'r':
                                ch = 'r'
                                break
                            else:
                                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    if ch == 'r':
                        break
                    if ch in ['q','m']:
                        return ch
                else:
                    print("INAVLID INPUT ! PLEASE TRY AGAIN !!")

def createPizza(cur):#TESTED
    #CREATES PIZZA BY MANAGER AND ADMIN
    while(True):
        name,price_s,price_m,price_l,shortcut,type,details = '','','','','','',''
        cur.execute('select name,shortcut from menu')
        res = cur.fetchall()
        lonm = []
        loshrt =[]
        for tup in res:
            lonm.append(tup[0].upper())
            loshrt.append(tup[1].lower())
        while(True):
            name = input("ENTER PIZZA NAME :")
            name = name.upper()
            chk = valid.validPizzaNameandDetails(name)
            if chk:
                if len(name)>=30 :
                    print("NAME TOO LARGE ! SHOULD BE UNDER 30 CHARATERS !!")
                
                else:
                    
                    if name not in lonm:
                        break
                    else:
                        print("NAME ALREADY EXISTS ! PLEASE TRY AGAIN !!")
            else:
                print("INVALID NAME ! SHOULD CONTAINS ONLY LETTER,DIGITS,SPACES,'.','-',',' ")
                print("PLEASE TRY AGAIN !!")
        while(True):
            lis = input("ENTER PRICES FOR SMALL,MEDIUM,LARGE FOLLOWING WITH A SPACE : ")
            lis = lis.split()
            if len(lis) !=3:
                print("SHOULD BE EXACTLY 3 PARAMETERS ! PLEASE TRY AGAIN !!")
            else:
                a,b,c = lis
                if valid.validNumber(a) and valid.validNumber(b) and valid.validNumber(c):
                    price_s, price_m, price_l = int(a), int(b), int(c)
                    break
                else:
                    print("INVALID NUMBER ! PLEASE TRY AGAIN !!")
        while(True):
            shortcut = input("ENTER SHORTCUT : ")
            shortcut = shortcut.lower()
            if len(shortcut) > 9:
                print("SHORTCUT TOO LARGE ! PLEASE TRY AGAIN !!")
            else:
                if shortcut not in loshrt:
                    #print(loshrt)
                    break
                else:
                    print("SHORTCUT ALREADY EXISTS")
                    
        while(True):
            type = input("ENTER TYPE AS VEG/NON-VEG OR V/N 0R 1/2")
            type = type.upper()
            if type in ["VEG","NON-VEG","N","V","1","2"]:
                if type == "1" or type == "V":
                    type = "VEG"
                elif type == '2' or type == 'N':
                    type= "NON-VEG"
                break
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
        while(True):
            details = input("ENTER DETAILS : ")
            chk = valid.validPizzaNameandDetails(details)
            if not chk:
                print("DETAILS SHOULD BE ONLY CHARACTERS, NUMBERS AND SPACES")
                print("INVALID DETAIL ! PLEASE TRY AGAIN!!")
                                
            else:
                break
            
        cur.execute('select max(prid) from menu')
        res = cur.fetchall()
        prid = res[0][0] + 1
        cur.execute('INSERT INTO MENU(prid,name,price_s,price_m,price_l,shortcut,type,details) VALUES(:1,:2,:3,:4,:5,:6,:7,:8)',(prid,name,price_s,price_m,price_l,shortcut,type, details))
        cur.execute('commit')
        print("PIZZA CREATED SUCCESSFULLY !")
        msgoption = """
                ENTER : 
                r =======> RETRY
                d =======> DISPLAY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                """
        while(True):
                ch = input(msgoption)
                ch = ch.lower()
                if ch in ['r','d','q','m']:
                    if ch == 'd':
                        view.viewMenu(prid, cur)
                        while(True):
                            msg = """
                                ENTER : 
                                
                                q =======> GO BACK
                                m =======> GO TO MAIN MENU
                                """
                            c = input(msg)
                            c = c.lower()
                            if c in ['q','m']:
                                return c
                            else:
                                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    elif ch == 'r':
                        print("RETRY...")
                        break
                    else:
                        return ch
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")

