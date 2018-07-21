
#----------------------------------------------------------------------------------------------------
#---------------------------------------------CASHIER------------------------------------------------
#----------------------------------------------------------------------------------------------------

class menuCashier():
    
    def __init__(self, cashier):
        self.cash = cashier 
    
    @staticmethod
    def menu_1():
        while(True):
            msg = """
        CASHIER 
        press : 
        1 =======> TAKE ORDER
        2 =======> VIEW MENU
        3 =======> VIEW CUSTOMER-DETAILS
        4 =======> CHANGE PASSWORD
        5 =======> EDIT PROFILE
        6 =======> VIEW PROFILE
        
        x =======> LOG OUT
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','4','5','6','x']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_11(self):
        return self.cash.takeOrder()
     
    @staticmethod   
    def menu_12():
        while(True):
            msg = """
        MENU
        press : 
        1 =======> SINGLE PIZZA
        2 =======> ALL PIZZA
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_121(self):
        return self.cash.viewPizzaSingle()
    
    @staticmethod
    def menu_122():
        while(True):
            msg = """
        MENU
        press : 
        1 =======> EVERYTHING
        2 =======> ONLY VEG
        3 =======> ONLY NON-VEG
        
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_1221(self):
        return self.cash.viewPizzaEverything()
    
    def menu_1222(self):
        return self.cash.viewPizzaVeg()
    
    def menu_1223(self):
        return self.cash.viewPizzaNONVEG()
    
    @staticmethod
    def menu_13():
        while(True):
            msg = """
        CUSTOMER DETAILS
        press : 
        1 =======> VIEW ORDERS OF A CUSTOMER
        2 =======> VIEW DETAILS OF A CUSTOMER
       
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    def menu_131(self):
        return self.cash.viewOrdersCustomer()
    
    def menu_132(self):
        return self.cash.viewOrdersCustomer()
    
    def menu_14(self):
        return self.cash.changePassword()
    
    def menu_15(self):
        return self.cash.editProfile()
    
    def menu_16(self):
        return self.cash.viewProfile()
#----------------------------------------------------------------------------------------------------
#---------------------------------------------MANAGER------------------------------------------------
#----------------------------------------------------------------------------------------------------

class menuManager():
    
    def __init__(self, manager):
        self.man = manager

    @staticmethod
    def menu_2():
        while(True):
            msg = """
        MANAGER 
        press : 
        1 =======> TAKE ORDER
        2 =======> PIZZA'S
        3 =======> EMPLOYEE
        4 =======> SALES
        5 =======> CUSTOMER
        6 =======> CHANGE PASSWORD
        7 =======> EDIT PROFILE
        8 =======> VIEW PROFILE
        
        x =======> LOG OUT
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','4','5','6','7','8','x']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_21(self):
        return self.man.takeOrder()
    
    @staticmethod
    def menu_22():
        while(True):
            msg = """
        PIZZA'S
        press : 
        1 =======> VIEW MENU
        2 =======> CHANGE MENU
        3 =======> CHANGE SHORTCUT
        4 =======> APPLY OFFERS
        5 =======> CREATE PIZZA
       
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','4','5','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod    
    def menu_221():
        while(True):
            msg = """
        VIEW MENU
        press : 
        1 =======> SINGLE PIZZA
        2 =======> ALL PIZZA
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
        
    def menu_2211(self):#IGNORE _ ERROR PREVENTIVE
        return self.man.viewPizzaSingle()
    
    @staticmethod
    def menu_2212():
        while(True):
            msg = """
        MENU
        press : 
        1 =======> EVERYTHING
        2 =======> ONLY VEG
        3 =======> ONLY NON-VEG
        
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_22121(self):
        return self.man.viewPizzaEverything()
    
    def menu_22122(self):
        return self.man.viewPizzaVeg()
    
    def menu_22123(self):
        return self.man.viewPizzaNONVEG()
    
    def menu_222(self):
        return self.man.changeMenu()
    
    def menu_223(self):
        return self.man.changeShortcut()
     
    @staticmethod   
    def menu_224():
        while(True):
            msg = """
        OFFERS
        press : 
        1 =======> ON SINGLE PIZZA
        2 =======> ON EVERY PIZZA
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
        
    def menu_2241(self):
        return self.man.applyOffersSP()
    
    def menu_2242(self):
        return self.man.applyOffersEP()
    
    def menu_225(self):
        return self.man.createPizza()
    
    @staticmethod
    def menu_23():
        while(True):
            msg = """
        EMPLOYEES
        press : 
        1 =======> VIEW EMPLOYEE DETAILS
        2 =======> CHANGE EMPLOYEE DETAILS
        3 =======> LOCK/UNLOCK EMPLOYEE ACCOUNT
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod           
    def menu_231():
        while(True):
            msg = """
        VIEW EMPLOYEE DETAILS
        press : 
        1 =======> PARTICULAR EMPLOYEE
        2 =======> ALL EMPLOYEES
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_2311(self):#IGNORE _ ERROR PREVENTIVE
        return self.man.viewParticularEmployee()
    
    @staticmethod
    def menu_2312():
        while(True):
            msg = """
        ALL EMPLOYEES
        press : 
        1 =======> CURRENT EMPLOYEES
        2 =======> FIRED EMPLOYEES
        3 =======> ALL EMPLOYEES
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_23121(self):
        return self.man.viewCurrentEmployees()
    
    def menu_23122(self):
        return self.man.viewFiredEmployees()
    
    def menu_23123(self):
        return self.man.viewAllEmployees()
    
    def menu_232(self):
        return self.man.changeEmployeeDetails()
    
    @staticmethod
    def menu_233():
        while(True):
            msg = """
            LOCK/UNLOCK EMPLOYEE ACCOUNT
            press : 
            1 =======> LOCK ACCOUNT
            2 =======> UNLOCK ACCONT
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod
    def menu_2331():
        while(True):
            msg = """
            LOCK ACCOUNT
            press : 
            1 =======> PARTICULAR EMPLOYEE
            2 =======> ALL EMPLOYEE
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    def menu_23311(self):
        return self.man.lockParticularEmployee()
    
    def menu_23312(self):
        return self.man.lockAllEmployee()
    
    @staticmethod    
    def menu_2332():
        while(True):
            msg = """
            UNLOCK ACCOUNT
            press : 
            1 =======> PARTICULAR EMPLOYEE
            2 =======> ALL EMPLOYEE
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_23321(self):
        return self.man.unlockParticularEmployee()
    
    def menu_23322(self):
        return self.man.unlockAllEmployee()
    
    @staticmethod
    def menu_24():
        while(True):
            msg = """
            SALES
            press : 
            1 =======> SALES BY EMPLOYEE
            2 =======> SALES BY MONTH
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod    
    def menu_241():
        while(True):
            msg = """
            SALES BY EMPLOYEE
            press : 
            1 =======> ON A PARTICULAR DAY
            2 =======> ON A PARTICULAR MONTH
            3 =======> CURRENT MONTH
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_2411(self):
        return self.man.saleByEmployeeParticularDay()
    
    def menu_2412(self):
        return self.man.saleByEmployeeParticularMonth()
    
    @staticmethod
    def menu_2413():
        while(True):
            msg = """
            CURRENT MONTH
            press : 
            1 =======> HIGHEST SALE EMPLOYEE
            2 =======> LOWEST SALE EMPLOYEE
            3 =======> ALL EMPLOYEES SALE
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_24131(self):
        return self.man.saleByEmployeeCurrentMonthHigh()
    
    def menu_24132(self):
        return self.man.saleByEmployeeCurrentMonthLow()
    
    def menu_24133(self):
        return self.man.saleByEmployeeCurrentMonthAll()
    
    @staticmethod
    def menu_242():
        while(True):
            msg = """
            SALE BY MONTH
            press : 
            1 =======> MONTHLY
            2 =======> DAILY
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod        
    def menu_2421():
        while(True):
            msg = """
            MONTHLY
            press : 
            1 =======> CURRENT MONTH
            2 =======> PAST MONTHS
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_24211(self):
        return self.man.saleByMonthCurrentMonth()
    
    def menu_24212(self):
        return self.man.saleByMonthPastMonth()
    
    @staticmethod
    def menu_2422():
        while(True):
            msg = """
            DAILY
            press : 
            1 =======> TODAY
            2 =======> PARTICULAR DAY OF A MONTH
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_24221(self):
        return self.man.saleByMonthToday()
    
    def menu_24222(self):
        return self.man.saleByMonthParticularDay()
    
    @staticmethod
    def menu_25():
        while(True):
            msg = """
        CUSTOMER DETAILS
        press : 
        1 =======> VIEW ORDERS OF A CUSTOMER
        2 =======> VIEW DETAILS OF A CUSTOMER
       
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    def menu_251(self):
        return self.man.viewOrdersCustomer()
    
    def menu_252(self):
        return self.man.viewDetailsCustomer()
    
    def menu_26(self):
        return self.man.changePassword()
    
    def menu_27(self):
        return self.man.editProfileManager()
    
    def menu_28(self):
        return self.man.viewProfile()

#----------------------------------------------------------------------------------------------------
#-----------------------------------------------ADMIN------------------------------------------------
#----------------------------------------------------------------------------------------------------

class menuAdmin():
    
    def __init__(self, admin):
        self.admin = admin
        
    @staticmethod
    def menu_3():
        while(True):
            msg = """
        ADMIN 
        press : 
        1 =======> TAKE ORDER
        2 =======> PIZZA'S
        3 =======> EMPLOYEE
        4 =======> SALES
        5 =======> CUSTOMER
        6 =======> CHANGE PASSWORD
        7 =======> EDIT PROFILE
        8 =======> VIEW PROFILE
        
        x =======> LOG OUT
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','4','5','6','7','8','x']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    def menu_31(self):
        return self.admin.takeOrder()
    
    @staticmethod
    def menu_32():
        while(True):
            msg = """
        PIZZA'S
        press : 
        1 =======> VIEW MENU
        2 =======> CHANGE MENU
        3 =======> CHANGE SHORTCUT
        4 =======> APPLY OFFERS
        5 =======> CREATE PIZZA
        6 =======> DELETE PIZZA
       
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','4','5','6','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod    
    def menu_321():
        while(True):
            msg = """
        VIEW MENU
        press : 
        1 =======> SINGLE PIZZA
        2 =======> ALL PIZZA
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
        
    def menu_3211(self):
        return self.admin.viewPizzaSingle()
    
    @staticmethod
    def menu_3212():
        while(True):
            msg = """
        MENU
        press : 
        1 =======> EVERYTHING
        2 =======> ONLY VEG
        3 =======> ONLY NON-VEG
        
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_32121(self):
        return self.admin.viewPizzaEverything()
        
    def menu_32122(self):
        return self.admin.viewPizzaVeg()
    
    def menu_32123(self):
        return self.admin.viewPizzaNONVEG()
    
    def menu_322(self):
        return self.admin.changeMenu()
    
    def menu_323(self):
        return self.admin.changeShortcut()
    
    @staticmethod
    def menu_324():
        while(True):
            msg = """
        OFFERS
        press : 
        1 =======> ON SINGLE PIZZA
        2 =======> ON EVERY PIZZA
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
        
    def menu_3241(self):
        return self.admin.applyOffersSP()
    
    def menu_3242(self):
        return self.admin.applyOffersEP()
    
    def menu_325(self):
        return self.admin.createPizza()
    
    def menu_326(self):
        return self.admin.removePizza()
    
    @staticmethod
    def menu_33():
        while(True):
            msg = """
        EMPLOYEES
        press : 
        1 =======> VIEW EMPLOYEE DETAILS
        2 =======> CHANGE EMPLOYEE DETAILS
        3 =======> LOCK/UNLOCK EMPLOYEE ACCOUNT
        4 =======> HIRE/FIRE/REHIRE EMPLOYEE
      
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','4','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod
    def menu_331():
        while(True):
            msg = """
        VIEW EMPLOYEE DETAILS
        press : 
        1 =======> PARTICULAR EMPLOYEE
        2 =======> ALL EMPLOYEES
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_3311(self):
        return self.admin.viewParticularEmployee()
    
    @staticmethod
    def menu_3312():
        while(True):
            msg = """
        ALL EMPLOYEES
        press : 
        1 =======> CURRENT EMPLOYEES
        2 =======> FIRED EMPLOYEES
        3 =======> ALL EMPLOYEES
        
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_33121(self):
        return self.admin.viewCurrentEmployees()
    
    def menu_33122(self):
        return self.admin.viewFiredEmployees()
    
    def menu_33123(self):
        return self.admin.viewAllEmployees()
    
    def menu_332(self):
        return self.admin.changeEmployeeDetails()
    
    @staticmethod
    def menu_333():
        while(True):
            msg = """
            LOCK/UNLOCK EMPLOYEE ACCOUNT
            press : 
            1 =======> LOCK ACCOUNT
            2 =======> UNLOCK ACCONT
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod
    def menu_3331():
        while(True):
            msg = """
            LOCK ACCOUNT
            press : 
            1 =======> PARTICULAR EMPLOYEE
            2 =======> ALL EMPLOYEE
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    def menu_33311(self):
        return self.admin.lockParticularEmployee()
    
    def menu_33312(self):
        return self.admin.lockAllEmployee()
     
    @staticmethod   
    def menu_3332():
        while(True):
            msg = """
            UNLOCK ACCOUNT
            press : 
            1 =======> PARTICULAR EMPLOYEE
            2 =======> ALL EMPLOYEE
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_33321(self):
        return self.admin.unlockParticularEmployee()
    
    def menu_33322(self):
        return self.admin.unlockAllEmployee()
    
    @staticmethod
    def menu_334():
        while(True):
            msg = """
            HIRE/FIRE/REHIRE EMPLOYEE
            press : 
            1 =======> HIRE EMPLOYEE
            2 =======> FIRE EMPLOYEE
            3 =======> REHIRE EMPLOYEE
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_3341(self):
        return self.admin.hireEmployee()
    
    def menu_3342(self):
        return self.admin.fireEmployee()
    
    def menu_3343(self):
        return self.admin.rehireEmployee()
    
    @staticmethod
    def menu_34():
        while(True):
            msg = """
            SALES
            press : 
            1 =======> SALES BY EMPLOYEE
            2 =======> SALES BY MONTH
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod   
    def menu_341():
        while(True):
            msg = """
            SALES BY EMPLOYEE
            press : 
            1 =======> ON A PARTICULAR DAY
            2 =======> ON A PARTICULAR MONTH
            3 =======> CURRENT MONTH
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_3411(self):
        return self.admin.saleByEmployeeParticularDay()
    
    def menu_3412(self):
        return self.admin.saleByEmployeeParticularMonth()
    
    @staticmethod
    def menu_3413():
        while(True):
            msg = """
            CURRENT MONTH
            press : 
            1 =======> HIGHEST SALE EMPLOYEE
            2 =======> LOWEST SALE EMPLOYEE
            3 =======> ALL EMPLOYEES SALE
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','3','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    def menu_34131(self):
        return self.admin.saleByEmployeeCurrentMonthHigh()
    
    def menu_34132(self):
        return self.admin.saleByEmployeeCurrentMonthLow()
    
    def menu_34133(self):
        return self.admin.saleByEmployeeCurrentMonthAll()
    
    @staticmethod
    def menu_342():
        while(True):
            msg = """
            SALE BY MONTH
            press : 
            1 =======> MONTHLY
            2 =======> DAILY
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    @staticmethod        
    def menu_3421():
        while(True):
            msg = """
            MONTHLY
            press : 
            1 =======> CURRENT MONTH
            2 =======> PAST MONTHS
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_34211(self):
        return self.admin.saleByMonthCurrentMonth()
    
    def menu_34212(self):
        return self.admin.saleByMonthPastMonth()
    
    @staticmethod
    def menu_3422():
        while(True):
            msg = """
            DAILY
            press : 
            1 =======> TODAY
            2 =======> PARTICULAR DAY OF A MONTH
            
            q =======> GO BACK
            m =======> GO TO MAIN MENU
            
                
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
            
    def menu_34221(self):
        return self.admin.saleByMonthToday()
    
    def menu_34222(self):
        return self.admin.saleByMonthParticularDay()
    
    @staticmethod
    def menu_35():
        while(True):
            msg = """
        CUSTOMER DETAILS
        press : 
        1 =======> VIEW ORDERS OF A CUSTOMER
        2 =======> VIEW DETAILS OF A CUSTOMER
       
        q =======> GO BACK
        m =======> GO TO MAIN MENU
        
            
            """
            opt = input(msg).lower()
            if opt in ['1','2','q','m']:
                return opt
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    
    def menu_351(self):
        return self.admin.viewOrdersCustomer()
    
    def menu_352(self):
        return self.admin.viewDetailsCustomer()
    
    def menu_36(self):
        return self.admin.changePassword()
    
    def menu_37(self):
        return self.admin.editProfileAdmin()
    
    def menu_38(self):
        return self.admin.viewProfile()


    