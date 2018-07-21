import view
import change
import order
import validation as valid
import create
from datetime import datetime


class Employee:
    
    def __init__(self, empid, cur):
        self._empid = empid
        cur.execute("select name,mobile,gender,designation,status,locks from employees where empid=:1",(empid,))
        res = cur.fetchall()
        res = res[0]
        self._name = res[0]
        self._mobile = res[1]
        self._gender = res[2]
        self._designation = res[3]
        self._status = res[4]
        self._lock = res[5]
        self._cur = cur
        
    def disp(self):
        print(self._empid,self._name,self._mobile,self._gender,self._designation,self._status,self._lock)
        
    def changePassword(self):
        while(True):
            change.changePassword(self._empid, self._cur)
            msg = """
            CHANGE PASSWORD
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
        
    def editProfile(self):
        ret = change.changeEmployeeDetailsByCashier(self._empid, self._cur)
        return ret
        
    def viewProfile(self):
        while(True):
            view.viewDetailsEmployee(self._empid, self._cur)
            msg = """
            VIEW PROFILE
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")

class Cashier(Employee):
    
    def __init__(self, empid, cur):
        super().__init__(empid, cur)       
        
    def viewPizzaSingle(self):
        cur = self._cur
        cur.execute("select prid,name,shortcut from menu")
        res = cur.fetchall()
        lot = []
        for i in res:
            x = (str(i[0]),i[1].lower(),i[2])
            lot.append(x)
        while(True):
            choice = input("ENTER PIZZA ID, PIZZA NAME OR SHORTCUT")
            ch1 = choice.lower()
            prid = False
            for tup in lot:
                if ch1 in tup:
                    prid = tup[0]
                    break
            if prid == False:
                print("NO SUCH PIZZA DETAILS FOUND ! PLEASE TRY AGAIN !!")
            else :
                view.viewMenu(prid, self._cur)
            msg = """
            SINGLE PIZZA
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def viewPizzaEverything(self):
        while(True):
            view.viewMenuAll("ALL", self._cur)
            msg = """
            EVERYTHING
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def viewPizzaVeg(self):
        while(True):
            view.viewMenuAll("VEG", self._cur)
            msg = """
            EVERYTHING
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def viewPizzaNONVEG(self):
        while(True):
            view.viewMenuAll("NON-VEG", self._cur)
            msg = """
            EVERYTHING
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def takeOrder(self):
        op = order.startOrder(self._empid, self._cur)
        return op
    
    def viewDetailsCustomer(self):
        cur = self._cur
        cur.execute("select mobile from customers")
        res = cur.fetchall()
        locust = []
        for i in res:
            locust.append(str(i[0]))
        while(True):
            mob = input("ENTER CUSTOMER MOBILE NUMBER : ")
            chk = valid.validMobile(mob)
            if chk:
                if mob in locust:
                    view.viewDetailsCustomer(mob, cur)
                else:
                    print("CUSTOMER DOES NOT EXIST ! PLEASE TRY AGAIN !! ")
            else:
                print("INVALID MOBILE NUMBER ! PLEASE TRY AGAIN !!")
            msg = """
            CUSTOMER DEATILS
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    
    def viewOrdersCustomer(self):
        cur = self._cur
        cur.execute("select mobile from customers")
        res = cur.fetchall()
        locust = []
        for i in res:
            locust.append(str(i[0]))
        while(True):
            mob = input("ENTER CUSTOMER MOBILE NUMBER : ")
            chk = valid.validMobile(mob)
            if chk:
                if mob in locust:
                    view.viewOrdersCustomer(mob, cur)
                else:
                    print("CUSTOMER DOES NOT EXIST ! PLEASE TRY AGAIN !! ")
            else:
                print("INVALID MOBILE NUMBER ! PLEASE TRY AGAIN !!")
            msg = """
            CUSTOMER ORDERS
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")

class Manager(Cashier):
    
    def __init__(self, empid, cur): 
        super().__init__(empid, cur)
        
    def editProfileManager(self):
        #print("manger")
        ret = change.changeEmployeeDetailsByCashier(self._empid, self._cur)
        return ret
        
    def changeMenu(self):
        cur = self._cur
        cur.execute("select prid,name,shortcut from menu")
        res = cur.fetchall()
        lot = []
        for i in res:
            x = (str(i[0]),i[1].lower(),i[2])
            lot.append(x)
        while(True):
            choice = input("ENTER PIZZA ID, PIZZA NAME OR SHORTCUT")
            ch1 = choice.lower()
            prid = False
            for tup in lot:
                if ch1 in tup:
                    prid = tup[0]
                    break
            if prid == False:
                print("NO SUCH PIZZA DETAILS FOUND ! PLEASE TRY AGAIN !!")
            else :
                ret = change.changeMenuSingle(prid, cur)
                if ret =='m':
                    return ret
            msg = """
            CHANGE MENU
            press : 
            r =======> RETRY
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg)
            opt = opt.lower()
            if opt in ['q','m']:
                return opt
            elif opt == 'r':
                print("RETRY....")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def changeShortcut(self):
        return change.changeShortcut(self._cur)
    
    def applyOffersSP(self):
        return change.changeOffers("ONE", self._cur)
           
    def applyOffersEP(self):
        return change.changeOffers('ALL', self._cur)
    
    def createPizza(self):
        return create.createPizza(self._cur)
                
    def viewParticularEmployee(self):#WILL BE OVERRIDEN
        self._cur.execute("select empid,designation from employees ")
        res = self._cur.fetchall()
        
        while(True):
            print("ENTER EMPLOYEE ID : ")
            id = input()
            chk = valid.validNumber(id)
            if chk:
                val1 = False
                des = ''
                for i in res:
                    if str(i[0]) ==  id:
                        val1 = True
                        des = i[1]
                        break
                if val1:
                    if des in ['ADMIN','MANAGER']:
                        print("YOU ARE NOT AUTHORIZED TO VIEW ",des," ACCOUNT !")
                    else:
                        view.viewDetailsEmployee(id, self._cur)
                else:
                    print("NO SUCH EMPLOYEE EXISTS ! PLEASE TRY AGAIN !!")
            else:
                print("INVALID ID! PLEASE TRY AGAIN !!")
            while(True):
                msg = """
                PARTICULAR EMPLOYEE
                press : 
                r =======> RETRY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                
                    
                """
                opt = input(msg)
                opt = opt.lower()
                if opt in ['q','m']:
                    return opt
                elif opt == 'r':
                    print("RETRY....")
                    break
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def viewCurrentEmployees(self):#WILL BE OVERRIDEN
        cur =self._cur
        while(True):
            view.viewDetailsEmployeeAll('ACTIVE', 'MANAGER', cur)
            while(True):
                msg = """
                CURRENT EMPLOYEES
                press : 
                r =======> RETRY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                
                    
                """
                opt = input(msg)
                opt = opt.lower()
                if opt in ['q','m']:
                    return opt
                elif opt == 'r':
                    print("RETRY....")
                    break
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    
    def viewFiredEmployees(self):#WILL BE OVERRIDEN
        cur =self._cur
        while(True):
            view.viewDetailsEmployeeAll('INACTIVE', 'MANAGER', cur)
            while(True):
                msg = """
                FIRED EMPLOYEES
                press : 
                r =======> RETRY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                
                    
                """
                opt = input(msg)
                opt = opt.lower()
                if opt in ['q','m']:
                    return opt
                elif opt == 'r':
                    print("RETRY....")
                    break
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    
    def viewAllEmployees(self):#WILL BE OVERRIDEN
        cur =self._cur
        while(True):
            view.viewDetailsEmployeeAll('ALL', 'MANAGER', cur)
            while(True):
                msg = """
                ALL EMPLOYEES
                press : 
                r =======> RETRY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                
                    
                """
                opt = input(msg)
                opt = opt.lower()
                if opt in ['q','m']:
                    return opt
                elif opt == 'r':
                    print("RETRY....")
                    break
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    
    def changeEmployeeDetails(self):#WILL BE OVERRIDEN
        cur = self._cur
        cur.execute("select empid from employees")
        res  = cur.fetchall()
        while(True):
            empid = input("ENTER EMPLOYEE ID : ")
            chk = valid.validNumber(empid)
            if chk:
                val = False
                for i in res:
                    if str(i[0]) == empid:
                        val = True
                        break
                if val:
                    x = change.changeEmployeeDetailsByManager(empid, cur)
                    if x == 'm':
                        return x
                else:
                    print("EMPLOYEE ID DOES NOT EXIST ! PLEASE TRY AGAIN !!")
            else:
                print("INVALID EMPLOYEE ID ! PLEASE TRY AGAIN !!")
            while(True):
                    msg = """
                    CHANGE EMPLOYEE DETAILS
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def lockParticularEmployee(self):#WILL BE OVERRIDEN - UNLOCKS ONLY CASHIER
        return change.changeEmployeeLock('LOCKED', 'ONE', 'MANAGER', self._cur)
    
    def lockAllEmployee(self):#WILL BE OVERRIDEN - - LOCKS ONLY CASHIER
        return change.changeEmployeeLock('LOCKED', 'ALL', 'MANAGER', self._cur)
    
    def unlockParticularEmployee(self):#WILL BE OVERRIDEN - LOCKS ONLY CASHIER
        return change.changeEmployeeLock('UNLOCKED', 'ONE', 'MANAGER', self._cur)
    
    def unlockAllEmployee(self):#WILL BE OVERRIDEN - UNLOCKS ONLY CASHIER
        return change.changeEmployeeLock('UNLOCKED', 'ALL', 'MANAGER', self._cur)
    
    def saleByEmployeeParticularDay(self):
        cur = self._cur
        cur.execute("select empid from employees")
        res = cur.fetchall()
        loempid = []
        for i in res:
            loempid.append(str(i[0]))
        while(True):
            print("ENTER DATE OF SALES AS dd/mm/yyyy : ")
            dat = input()
            if len(dat.split("/")) !=  3:
                print("INVALID DATE FORMAT ! PLEASE TRY AGAIN !!")
            else:
                chk = valid.validDate(dat)
                if chk:
                    empid = input("ENTER EMPLOYEE ID : ")
                    chk2 = valid.validNumber(empid)
                    if chk2:
                        if empid in loempid:
                            print("\n\n")
                            view.viewSaleDayEmployee(dat, empid, cur)
                        else:
                            print("EMPLOYEE ID DOES NOT EXIST ! PLEASE TRY AGAIN !!")
                    else:
                        print("INVALID EMPLOYEE ID ! PLEASE TRY AGAIN !!")
                else:
                    print("INVALID DATE FORMAT ! PLEASE TRY AGAIN !!")
            while(True):
                    msg = """
                    EMPLOYEE SALES ON A PARTICULAR DAY
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def saleByEmployeeParticularMonth(self):
        cur = self._cur
        cur.execute("select empid from employees")
        res = cur.fetchall()
        loempid = []
        months = [("1","JANUARY","JAN"),("2","FEBRUARY","FEB"),("3","MARCH","MAR"),("4","APRIL","APR"),("5","MAY","MAY"),("6","JUNE","JUN"),
                  ("7","JULY","JUL"),("8","AUGUST","AUG"),("9","SEPTEMBER","SEP"),("10","OCTOBER","OCT"),("11","NOVEMBER","NOV"),("12","DECEMBER","DEC"),]
        for i in res:
            loempid.append(str(i[0]))
        while(True):
            print("ENTER MONTH NUMBER or MONTH NAME : ")
            mon = input().upper()
            chk = False
            for i in months:
                if mon in i:
                    chk = True
                    mon = i[0]
                    break
            
            if not chk:
                print("INVALID MONTH ! PLEASE TRY AGAIN !!")
            else:
                empid = input("ENTER EMPLOYEE ID : ")
                chk2 = valid.validNumber(empid)
                if chk2:
                    if empid in loempid:
                        print("\n\n")
                        view.viewSaleMonthEmployee(mon, empid, cur)
                    else:
                        print("EMPLOYEE ID DOES NOT EXIST ! PLEASE TRY AGAIN !!")
                else:
                    print("INVALID EMPLOYEE ID ! PLEASE TRY AGAIN !!")
                
            while(True):
                    msg = """
                    EMPLOYEE SALES ON A PARTICULAR MONTH
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def saleByEmployeeCurrentMonthHigh(self):
        cur = self._cur
        while(True):
            print("\n")
            current = datetime.now().month
            view.viewSaleMonthEmployeeAll(current, "HIGHEST", cur)
            while(True):
                    msg = """
                    EMPLOYEE SALES ON A PARTICULAR MONTH -> HIGHEST
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def saleByEmployeeCurrentMonthLow(self):
        cur = self._cur
        while(True):
            print("\n")
            current = datetime.now().month
            view.viewSaleMonthEmployeeAll(current, "LOWEST", cur)
            while(True):
                    msg = """
                    EMPLOYEE SALES ON A PARTICULAR MONTH -> LOWEST
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def saleByEmployeeCurrentMonthAll(self):
        cur = self._cur
        while(True):
            print("\n")
            current = datetime.now().month
            view.viewSaleMonthEmployeeAll(current, "ALL", cur)
            while(True):
                    msg = """
                    EMPLOYEE SALES ON A PARTICULAR MONTH -> ALL
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def saleByMonthCurrentMonth(self):
        cur = self._cur
        while(True):
            print("\n")
            current = datetime.now().month
            view.viewSalesMonth(current, self._cur)
            while(True):
                    msg = """
                    SALE BY MONTH -> CURRENT MONTH
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def saleByMonthPastMonth(self):
        cur = self._cur
        months = [("1","JANUARY","JAN"),("2","FEBRUARY","FEB"),("3","MARCH","MAR"),("4","APRIL","APR"),("5","MAY","MAY"),("6","JUNE","JUN"),
                  ("7","JULY","JUL"),("8","AUGUST","AUG"),("9","SEPTEMBER","SEP"),("10","OCTOBER","OCT"),("11","NOVEMBER","NOV"),("12","DECEMBER","DEC"),]
       
        while(True):
            print("ENTER MONTH NUMBER or MONTH NAME : ")
            mon = input().upper()
            chk = False
            for i in months:
                if mon in i:
                    chk = True
                    mon = i[0]
                    break
            
            if not chk:
                print("INVALID MONTH ! PLEASE TRY AGAIN !!")
            else:
                view.viewSalesMonth(int(mon), cur)
            while(True):
                    msg = """
                    SALE BY MONTH -> PAST MONTH
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def saleByMonthToday(self):
        cur = self._cur
        while(True):
            tod = ((str(datetime.today())).split())[0]
            a,b,c = tod.split("-")
            tod = c+"/"+b+"/"+a
            view.viewSalesDay(tod, cur)
            while(True):
                    msg = """
                    SALE BY MONTH -> TODAY
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def saleByMonthParticularDay(self):
        cur = self._cur
        while(True):
            print("ENTER DATE OF SALES AS dd/mm/yyyy : ")
            dat = input()
            if len(dat.split("/")) !=  3:
                print("INVALID DATE FORMAT ! PLEASE TRY AGAIN !!")
            else:
                chk = valid.validDate(dat)
                if chk:
                    view.viewSalesDay(dat, self._cur)
            while(True):
                    msg = """
                    SALE BY MONTH -> PARTICULAR DAY
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    

class Admin(Manager):
    
    def __init__(self, empid, cur):
        super().__init__(empid, cur)  
        
    def editProfileAdmin(self):
        #print("admin")
        ret = change.changeEmployeeDetailsByAdmin(self._empid, self._cur)
        return ret
    
    def viewParticularEmployee(self):#OVERRIDEN
        self._cur.execute("select empid,designation from employees ")
        res = self._cur.fetchall()
        
        while(True):
            print("ENTER EMPLOYEE ID : ")
            id = input()
            chk = valid.validNumber(id)
            if chk:
                val1 = False
                des = ''
                for i in res:
                    if str(i[0]) ==  id:
                        val1 = True
                        des = i[1]
                        break
                if val1:
                    view.viewDetailsEmployee(id, self._cur)
                else:
                    print("NO SUCH EMPLOYEE EXISTS ! PLEASE TRY AGAIN !!")
            else:
                print("INVALID ID! PLEASE TRY AGAIN !!")
            while(True):
                msg = """
                PARTICULAR EMPLOYEE
                press : 
                r =======> RETRY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                
                    
                """
                opt = input(msg)
                opt = opt.lower()
                if opt in ['q','m']:
                    return opt
                elif opt == 'r':
                    print("RETRY....")
                    break
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def viewCurrentEmployees(self):#OVERRIDEN
        cur =self._cur
        while(True):
            view.viewDetailsEmployeeAll('ACTIVE', 'ADMIN', cur)
            while(True):
                msg = """
                CURRENT EMPLOYEES -> CASHIER , MANAGER, ADMIN
                press : 
                r =======> RETRY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                
                    
                """
                opt = input(msg)
                opt = opt.lower()
                if opt in ['q','m']:
                    return opt
                elif opt == 'r':
                    print("RETRY....")
                    break
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    
    def viewFiredEmployees(self):#OVERRIDEN
        cur =self._cur
        while(True):
            view.viewDetailsEmployeeAll('INACTIVE', 'ADMIN', cur)
            while(True):
                msg = """
                FIRED EMPLOYEES -> CASHIER , MANAGER, ADMIN
                press : 
                r =======> RETRY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                
                    
                """
                opt = input(msg)
                opt = opt.lower()
                if opt in ['q','m']:
                    return opt
                elif opt == 'r':
                    print("RETRY....")
                    break
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    
    def viewAllEmployees(self):#OVERRIDEN
        cur =self._cur
        while(True):
            view.viewDetailsEmployeeAll('ALL', 'ADMIN', cur)
            while(True):
                msg = """
                ALL EMPLOYEES -> CASHIER , MANAGER, ADMIN
                press : 
                r =======> RETRY
                q =======> GO BACK
                m =======> GO TO MAIN MENU
                
                    
                """
                opt = input(msg)
                opt = opt.lower()
                if opt in ['q','m']:
                    return opt
                elif opt == 'r':
                    print("RETRY....")
                    break
                else:
                    print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                    
    def changeEmployeeDetails(self):#OVERRIDEN
        cur = self._cur
        cur.execute("select empid from employees")
        res  = cur.fetchall()
        while(True):
            empid = input("ENTER EMPLOYEE ID : ")
            chk = valid.validNumber(empid)
            if chk:
                val = False
                for i in res:
                    if str(i[0]) == empid:
                        val = True
                        break
                if val:
                    x = change.changeEmployeeDetailsByAdmin(empid, cur)
                    if x == 'm':
                        return x
                else:
                    print("EMPLOYEE ID DOES NOT EXIST ! PLEASE TRY AGAIN !!")
            else:
                print("INVALID EMPLOYEE ID ! PLEASE TRY AGAIN !!")
            while(True):
                    msg = """
                    CHANGE EMPLOYEE DETAILS
                    press : 
                    r =======> RETRY
                    q =======> GO BACK
                    m =======> GO TO MAIN MENU
                    
                        
                    """
                    opt = input(msg)
                    opt = opt.lower()
                    if opt in ['q','m']:
                        return opt
                    elif opt == 'r':
                        print("RETRY....")
                        break
                    else:
                        print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                        
    def lockParticularEmployee(self):#OVERRIDEN
        return change.changeEmployeeLock('LOCKED', 'ONE', 'ADMIN', self._cur)
    
    def lockAllEmployee(self):#OVERRIDEN
        return change.changeEmployeeLock('LOCKED', 'ALL', 'ADMIN', self._cur)
    
    def unlockParticularEmployee(self):#OVERRIDEN
        return change.changeEmployeeLock('UNLOCKED', 'ONE', 'ADMIN', self._cur)
    
    def unlockAllEmployee(self):#OVERRIDEN
        return change.changeEmployeeLock('UNLOCKED', 'ALL', 'ADMIN', self._cur)
    
    def hireEmployee(self):
        return create.createEmployeeAccount(self._cur)
    
    def fireEmployee(self):
        return change.changeEmployeeStatusFire('FIRE', self._cur)
    
    def rehireEmployee(self):
        return change.changeEmployeeStatusFire('REHIRE', self._cur)
    
    def removePizza(self):
        return change.removePizza(self._cur)
    
            