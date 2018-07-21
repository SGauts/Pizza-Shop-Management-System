import sqlite3
import menu
import change
import validation as valid
import view
import order
import employee

welcome = """
*********************************************************************************************
                        WELCOME TO PIZZA SHOP MANAGEMENT SYSTEM
                                            by- S&G PVT LTD.
*********************************************************************************************                  
"""

thankyou = """
*********************************************************************************************
                        THANKYOU FOR USING  PIZZA SHOP MANAGEMENT SYSTEM
                        ----------------COME BACK AGAIN----------------- 
                        ----------------HAVE A NICE DAY-----------------
                                            by- S&G PVT LTD.
*********************************************************************************************                  
"""

line = "*********************************************************************************************"

def custLogin(cur):
    global welcome,thankyou
    while(True):
        print(welcome)
        print("WELCOME CUSTOMER")
        mob = input("PLEASE ENTER YOUR REGISTERED MOBILE NUMBER : ")
        chk = valid.validMobile(mob)
        if chk:
            cur.execute("select * from customers where mobile=:1",(mob,))
            res = cur.fetchall()
            if len(res) == 0:
                print("CUSTOMER MOBILE NUMBER NOT REGISTERED ! PLEASE TRY AGAIN !!")
            else:
                res = res[0]
                while(True):
                    print("WELCOME ",res[0])
                    msg = """
                    CUSTOMER ACCOUNT
                    press : 
                    1 =======> VIEW MENU
                    2 =======> VIEW YOUR LAST ORDER
                    3 =======> VIEW YOUR ORDER HISTORY
                    4 =======> VIEW YOUR POINTS
                    5 =======> VIEW YOUR ACCOUNT DETAILS
                    
                    x =======> LOG OUT
                    """
                    msg2 = """
                    press : 
                   
                    q =======> GO BACK 
                    x =======> LOG OUT
                    """
                    ch = input(msg)
                    ch = ch.lower()
                    if ch in ['1','2','3','4','5','x']:
                        if ch ==  '1':
                            order.showHalfMenu(cur)
                            while(True):
                                choice = input(msg2)
                                choice = choice.lower()
                                if choice == 'q':
                                    break
                                elif choice == 'x':
                                    return choice
                                else:
                                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                                
                        elif ch == '2' :
                            view.viewOrdersCustomerLatest(mob, cur)
                            while(True):
                                choice = input(msg2)
                                choice = choice.lower()
                                if choice == 'q':
                                    break
                                elif choice == 'x':
                                    return choice
                                else:
                                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        elif ch == '3':
                            view.viewOrdersCustomer(mob, cur)
                            while(True):
                                choice = input(msg2)
                                choice = choice.lower()
                                if choice == 'q':
                                    break
                                elif choice == 'x':
                                    return choice
                                else:
                                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        elif ch == '4':
                            view.viewPoints(mob, cur)
                            while(True):
                                choice = input(msg2)
                                choice = choice.lower()
                                if choice == 'q':
                                    break
                                elif choice == 'x':
                                    return choice
                                else:
                                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        elif ch == '5':
                            view.viewDetailsCustomer(mob, cur)
                            while(True):
                                choice = input(msg2)
                                choice = choice.lower()
                                if choice == 'q':
                                    break
                                elif choice == 'x':
                                    return choice
                                else:
                                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        else:
                            return ch
                        
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    print("\n",line,"\n")
                
        else:
            print("INVALID MOBILE NUMBER ! PLEASE TRY AGAIN !!")
        while(True):
            msg = """
            
    press : 
    r =======> RETRY
    x =======> EXIT
            
            """
            ch = input(msg)
            ch = ch.lower()
            if ch == 'r':
                break
            elif ch == 'x':
                return ch
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
def empLogin(cur):
    global welcome
    chance = 3
    while(True):
        print(line,"\nWELCOME EMPLOYEE")
        empid = input("PLEASE ENTER YOUR ID : ")
        pwd = input("PLEASE ENTER YOUR PASSWORD : \n")
        chk = valid.validNumber(empid)
        if chk:
            cur.execute("select status,locks,designation,password,name from EMPLOYEES where EMPID='1'",(empid,))
            res = cur.fetchall()
            if len(res) == 0:
                print("EMPLOYEE ID DOES NOT EXIST ! PLEASE TRY AGAIN !! \n\n")
            else:
                res = res[0]
                if res[0] == 'INACTIVE':
                    print("YOU ARE NO LONGER AN EMPLOYEE ! \n ACCESS DENIED \n\n!!")
                else:
                    if res[1] == 'LOCKED':
                        print("YOUR ACCOUNT IS LOCKED !")
                        if res[2] == 'CASHIER':
                            print("PLEASE CONTACT YOUR MANAGER OR ADMIN !! ")
                            print("ACCESS DENIED!!!\n\n")
                        else:
                            print("PLEASE CONTACT YOUR ADMIN !")
                            print("ACCESS DENIED!!!\n\n")
                    else:#PASSWORD CHECKING
                        start = ''
                        redirect =  ''
                        if pwd == res[3]:
                            print(line,"\n","WELCOME ",res[4].upper())
                            if res[2] == 'CASHIER':
                                start = "1"
                                cashier = employee.Cashier(empid, cur)
                                redirect = menu.menuCashier(cashier)
                            elif res[2] == 'MANAGER':
                                start = "2"
                                manager = employee.Manager(empid, cur)
                                redirect = menu.menuManager(manager)
                            else:
                                start = "3"
                                admin = employee.Admin(empid, cur)
                                redirect = menu.menuAdmin(admin)
                            path = "menu_"+start
                            result = ''
                            while(result != 'x'):
                                print("\n",line,"\n")
                                result = getattr(redirect, path)()
                                if result == 'q':
                                    path = path[:-1]
                                elif result == 'm':
                                    path = "menu_"+start
                                else:
                                    path = path+result
                            return result
                            
                        else:
                            print("INCORRECT ID OR PASSWORD ! PLEASE TRY AGAIN !!\n")
                            chance = chance - 1
                            if res[2] in ['CASHIER','MANAGER']:
                                
                                if chance <= 0:
                                    change.changeEmployeeLockLogin(empid, cur)
                                    print("DUE TO 3 CONSECUTIVE FAILED LOGIN ATTEMPT ! \nYOUR ACCOUNT HAS BEEN LOCKED !!\n\n")
                                else:
                                    print("YOU HAVE ONLY ",chance," LEFT !!\n\n")
                                    continue
                            else:
                                if chance <= 0:
                                    print("YOU HAVE TRIED YOU MAXIMUM LIMIT FOR NOW !")
                                    print("PLEASE TRY AFTER SOME TIME !! \n\n")
                                    
                                else:
                                    continue   
        else:
            print("INVALID INPUT ! PLEASE TRY AGAIN !!\n\n")
        while(True):
            msg = """
            
    press : 
    r =======> RETRY
    x =======> EXIT
            
            """
            ch = input(msg)
            ch = ch.lower()
            if ch == 'r':
                break
            elif ch == 'x':
                return ch
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!\n")               
                            
            
    
if __name__ == "__main__":
    try:
        conn = sqlite3.connect('pds.db', timeout=10)
        cur = conn.cursor()
        while(True):
            print(welcome,"\n\n")
            msg = """
        LOGIN       
        press : 
        1 =======> CUSTOMER
        2 =======> EMPLOYEE
        
        x =======> EXIT       
                """
            ch = input(msg)
            ch = ch.lower()
            if ch == '1':
                custLogin(cur)
            elif ch == '2':
                empLogin(cur)
            elif ch == 'x':
                print("\n",thankyou)
                break
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!\n")
    except Exception as e:
        print("OOPS ! SOME ERROR OCCURED !! PLEASE CONTACT S&G PVT LTD. !!!")
        print("PROGRAM TERIMINATED SUCCESSFULLY !!!!")
        print(e)
    else:
        print("!!! END OF PROGRAM SUCCESSFULLY !!!")   