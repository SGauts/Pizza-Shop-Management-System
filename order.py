import view
import validation as valid
import create
import re
import datetime


orders = []
cust = []
current_order = 0
def printBill(bill):#TESTED
    #WRITES THE BILL IN A FILE TO BE PRINTED
    filename = "bill_"+str(current_order)+".txt"
    order = open(filename,"w")
    order.write(bill)
    order.close()
    print(" ORDER :",current_order," PRINTED AS : ",filename)
    print("\n\n")
    

def showHalfMenu(cur):#TESTED
    #SHOW SHORT MENU
    cur.execute('select prid,name,price_s,price_m,price_l,type from menu order by prid')
    res = cur.fetchall()
    msg = """
    ---------------------------------------------------------------------------------------------
                                            MENU
    ---------------------------------------------------------------------------------------------
    PRID \t\t NAME \t\t\t S/M/L \t\t TYPE
    """
    print(msg)
    for tup in res:
        print(tup[0]," \t\t ",tup[1]," \t\t ",tup[2],"/",tup[3],"/",tup[4]," \t\t ",tup[5])
    print("---------------------------------------------------------------------------------------------\n")
        
def getCustomers(cur):#TESTED
    #GET ALL CURRENT CUSTOMERS
    global cust
    cur.execute('select mobile from customers')
    res = cur.fetchall()
    for tup in res:
        cust.append(str(tup[0]))

def viewOrder():#TESTED
    #VIEW THE ORDERS IN THE 'ORDERS' LIST
    global orders
    if len(orders)!=0:
        for i in orders:
            print("NAME : ",i[0],"SIZE : ",i[1].upper(),"QUANTITY : ",i[2])
            
        print("\n\n")
    
    else:
        print("NO ORDER TO DISPLAY !!")
        print("\n\n")
    
def removeLast():#TESTED
    #REMOVE LAST ORDER FROM THE 'ORDERS' LIST
    global orders
    if len(orders) == 0:
        print("EMPTY ORDER BASKET ! CANNOT REMOVE ANYTHING !!")
        print("\n\n")
    else:
        i = orders.pop()
        print("REMOVED : ")
        print("NAME : ",i[0],"SIZE : ",i[1].upper(),"QUANTITY : ",i[2])
        print("\n\n")
    
def startOrder(empid,cur):#TESTED_MAIN
    #MAIN PROGRAM WHICH STARTS THE ORDER
    global orders 
    oup = '' #REINTIALIZATION FOR NEXT ORDER
    while(oup not in ['q','m']):
        orders = []
        oup = takeOrder(empid,cur)
        oup = oup.lower()
    return oup
    
def generateBillandSave(custid, empid, redeem, cur):#TESTED
    #GENERATE BILL, SAVE ORDER INTO DATABASE, UPDATE CUSTOMERS POINTS
    global current_order
    time = datetime.datetime.now()
    manual = """
    ---------------------------------------------------------------------------------------------
                                    PIZZA DELIVERY SYSTEM
    ---------------------------------------------------------------------------------------------
    Order id : """
    cur.execute('select max(ordid) from orders')
    res = cur.fetchall()
    ordid = res[0][0] + 1
    manual += str(ordid)
    cur.execute('select name from customers where mobile = :1',(custid,))
    res = cur.fetchall()
    custnm = res[0][0]
    current_order = ordid
    manual += "\t CUSTOMER NAME : "+ custnm
    manual += """
    ---------------------------------------------------------------------------------------------
    TIMINGS :
    
    """   
    tm = time
    tm = str(tm)
    tm = tm.split('.')
    tm = tm[0]
    manual += str(tm)
    manual += """
    ---------------------------------------------------------------------------------------------
    NAME \t\t TYPE \t\t SIZE \t\t QUANTITY \t\t PRICE \t\t TOTAL
    ---------------------------------------------------------------------------------------------
    """
    
    bill = 0
    for i in orders:
        name = i[0].upper()
        size = i[1].upper()
        sz = ''
        if size == 'S':
            sz = 'select price_s,type from menu where name=:1'
        if size == 'M':
            sz = 'select price_m,type from menu where name=:1'
        if size == 'L':
            sz = 'select price_l,type from menu where name=:1'
        quan = int(i[2])
        cur.execute(sz,(name,))
        res = cur.fetchall()
        res = res[0]
        #print(res) DEBUGGING
        price = res[0]
        type = res[1]
        b = quan * int(price) 
        st = "\n"
        st = st+name+"\t\t"+type+"\t\t"+size+"\t\t"+str(quan)+"\t\t"+str(price)+"\t\t"+str(b)
        st += "\n ("+type+")"
        manual +=st
        bill = bill + int(b)
    manual += "\n"
    manual += """
    ---------------------------------------------------------------------------------------------
    SUB TOTAL = RS """
    manual += str(bill)
    
    cur.execute('select points from customers where mobile=:1',(custid,))
    res = cur.fetchall()
    points = res[0][0]
    gtotal = 0
    #REDEEMING POINTS
    if redeem:
        if points>bill:
            points -= bill
        else:
            
            gtotal = bill - points
            points = 0
    else:
        gtotal = bill
    manual += """\n
    ---------------------------------------------------------------------------------------------
    POINTS REDEEMED = """
    pointE = int(gtotal/100)
    points += pointE
    manual += str(bill-gtotal)
    manual += """\n
    ---------------------------------------------------------------------------------------------
    GRAND TOTAL  = RS """
    manual += str(gtotal)
    gst = round((0.05)*gtotal,2)
    manual += """\n
    ---------------------------------------------------------------------------------------------
    GST @ 5 % = RS """
    manual += str(gst)
    manual += """\n
    ---------------------------------------------------------------------------------------------
    AMOUNT PAYABLE = RS """
    amount = gtotal+round(gst)
    manual += str(amount)
    
    manual += """\n
    ---------------------------------------------------------------------------------------------
    POINTS EARNED  = """
    manual += str(pointE)
    manual +="""\n
    ---------------------------------------------------------------------------------------------
                    THANK YOU ! FOR SHOPPING WITH US!! KEEP COMING !!!
    ---------------------------------------------------------------------------------------------
                                        HAVE A NICE DAY!!
    ---------------------------------------------------------------------------------------------
    """
    
    
    cur.execute("insert into orders(ordid,custid,empid,time,bill,details) values(:1,:2,:3,:4,:5,:6)",(ordid,custid,empid,time,amount,manual))
    cur.execute('update customers set points=:1 where mobile=:2 ',(points,custid))
    cur.execute('commit')
    return manual
    
        



def takeOrder(empid, cur):#TESTED
    #INTERFACE TO WORK WITH OTHER FUNCTIONS
    global orders,cust
    msg = """
    ENTER : vm     =======> VIEW MENU
            vo     =======> VIEW ORDER
            create =======> CREATE CUSTOMER ACCOUNT
            cancel =======> CANCEL ORDER
            last   =======> REMOVE LAST PRODUCT IN OPTION
            done   =======> DONE ORDER
            print  =======> PRINT RECEIPT
            next   =======> NEXT ORDER
            q      =======> GO BACK
            m      =======> MAIN MENU
    
    """
    print(msg)
    print("NOTE : YOU COULD TYPE THESE COMMANDS ANYWHERE/ANYTIME WHILE TAKING ORDER")
   
    #print("HERE IS THE TODAY'S MENU")
    #view.viewMenuAll('ALL', cur)needs to be changed
    
    id = ''
    while(True):# GET CUSTOMER ID
        print("ENTER CUSTOMER ID : ")
        getCustomers(cur)
        id = input()
        id = id.lower()
        if id not in ['vm','vo','create','cancel','last','done','print','next','q','m']:
            if valid.validMobile(id):
                if id in cust:
                    break
                else:
                    print("CUSTOMER DOESN'T EXISTS !")
                    print("EITHER CREATE ACCOUNT OR RE-ENTER THE CORRECT ID !!")
                    print("\n\n")
            else:
                print("NOT A VALID MOBILE NUMBER ! ")
                print("PLEASE ENTER A VALID MOBILE NUMBER !!")
                print("\n\n")
        else :
            if id == 'vm':
                showHalfMenu(cur)
            elif id in ['vo','last','done','print','next']:
                print("NO CURRENT ORDER TO PERFORM ACTION!")
                print("\n\n")
            elif id == 'create':
                create.createCustomerAccount(cur)
                print("\n\n")
            elif id == 'cancel':
                print("ORDER CANCELLED ! PLAESE START AGAIN !!")
                print("\n\n")
                return 'cancel'
            else:
                return id
    print("\n\n")
    print("ENTER ORDER AS : ")
    print("PRODUCT_ID/NAME/SHORTCUT  SIZE(S/M/L) QUANTITY ")
    cur.execute('select prid,name,shortcut from menu')
    res = cur.fetchall()
    lotup = []#LOTUP TO CHECK FOR NAME INPRID,SHORTCUT,NAME
    for tup in res:
        a,b,c = tup[0],tup[1],tup[2]
        lotup.append((str(a),str(b).upper(),str(c)))
   
    print("ENTER 'done' to complete ORDER")    
    while(True):#TAKE ORDERS
        prod = input()
        prod = prod.lower()
        if prod not in ['vm','vo','create','cancel','last','done','print','next','q','m']:
            prod = prod.split()
            if len(prod) < 3:
                print("ORDER SHOULD BE ATLEAST 3 PARAMETERS ")
            else:
                if len(prod) > 3:
                    namelist = prod[:-2]
                    size = prod[-2]
                    quan = prod[-1]
                    name = ' '.join(namelist)
                    name = name.upper() 
                else:
                    name, size, quan = prod
                    name = name.upper()
                chk = False
                pizzaname = ''
                for i in lotup:
                    #print(i)
                    if name in i:
                        
                        chk = True
                        pizzaname = i[1]
                      
                        break
                if not chk:
                    print("NO SUCH PRODUCT_ID/NAME/SHORTCUT EXISTS !")
                    print("PLEASE TRY AGAIN !!")
                    print("\n\n")
                else:
                    if size in ['s','m','l']:
                        if valid.validNumber(quan):
                            tup = (pizzaname,size,quan)
                            orders.append(tup)
                        
                        else:
                            print("QUANTITY SHOULD BE A NUMBER !")
                            print("PLEASE TRY AGAIN !!")
                            print("\n\n")
                        
                    else:
                        print("NOT A VALID SIZE !")
                        print("PLEASE TRY AGAIN !!")
                        print("\n\n")
        else:
            if prod == 'vm':
                showHalfMenu(cur)
                print("\n\n")
            elif prod == 'vo':
                viewOrder()
                print("\n\n")
            elif prod == 'create':
                print("CUSTOMER CANOT BE CREATED IN BETWEEN ORDER !!")
                print("\n\n")
                
            elif prod == 'last':
                removeLast()
            
            elif prod == 'done':
                if len(orders)>0:
                    break
                else:
                    print("NO ORDER ! TRY AGAIN !!")
                    print()
            
            elif prod == 'print':
                print("FIRST CONFIRM THE ORDER !")
                print("\n\n")
            elif prod == 'next':
                print("EITHER CONFIRM OR CANCEL ORDER TO GO TO NEXT !")
                print("\n\n")
            elif prod == 'cancel':
                print("ORDER CANCELLED ! PLAESE START AGAIN !!")
                print("\n\n")
                return prod
            else:
                return prod
              
    
    while(True):# FOR ORDER CONFIRMATION
        print("ORDER IS : ")
        viewOrder() 
        print("ENTER 'done' to CONFIRM ")
        print("NOTE : ONCE CONFIRMED ORDER CANNOT BE CANCELLED ")
        ch = input()
        ch = ch.lower()
        if ch in ['vm','vo','create','cancel','last','done','print','next','q','m']:
            if ch == 'vm':
                showHalfMenu(cur)
                print("\n\n")
            elif ch == 'vo':
                viewOrder()
                print("\n\n")
            elif ch == 'create':
                print("CUSTOMER CANNOT BE CREATED IN BETWEEN ORDER !!")
                print("\n\n")
                
            elif ch == 'last':
                removeLast()
            
            elif ch == 'done':
                break
            
            elif ch == 'print':
                print("FIRST CONFIRM THE ORDER !")
                print("\n\n")
            elif ch == 'next':
                print("EITHER CONFIRM OR CANCEL ORDER TO GO TO NEXT !")
                print("\n\n")
            elif ch == 'cancel':
                print("ORDER CANCELLED ! PLEASE START AGAIN !!")
                print("\n\n")
                return ch
            else:
                return ch
        else:
            print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    cur.execute('select points from customers where mobile=:1',(int(id),))
    res = cur.fetchall()
    points = res[0][0]
    pointsredeem = False
    if points > 0:
        while(True):
            print("CUSTOMER HAVE : ",points," POINTS")
            print("ENTER 'done' or 'yes/y' to REDEEM ")
            print("ENTER 'no/n' to NOT REDEEM")
            
            ch = input()
            ch = ch.lower()
            if ch in ['vm','vo','create','cancel','last','done','print','next','yes','no','y','n','q','m']:
                if ch== 'vm':
                    view.viewMenuAll('ALL', cur)
                    print("\n\n")
                elif ch == 'vo':
                    viewOrder()
                    print("\n\n")
                elif ch == 'create':
                    print("CUSTOMER CANNOT BE CREATED IN BETWEEN ORDER !!")
                    print("\n\n")
                    
                elif ch == 'last':
                    print("CONFIRMED ORDER CANNOT BE CHANGED !!")
                
                elif ch in ['done','yes','y'] :
                    pointsredeem = True
                    break
                elif ch in ['no','n']:
                    break
                
                elif ch == 'print':
                    print("FIRST COMPLETE THE ORDER !")
                    print("\n\n")
                elif ch == 'next':
                    print(" FIRST COMPLETE THE ORDER !")
                    print("\n\n")
                elif ch == 'cancel':
                    print("ORDER CANNOT BE CANCELLED !!")
                    print("\n\n")
                    
                else:
                    print("YOU CANNOT GO BACK ! UNTIL ORDER IS COMPLETED !!")
                    print("\n\n")
            else:
                print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                
    bill = generateBillandSave(int(id), empid, pointsredeem, cur)
    print("BILL IS :")
    print(bill)
    print("\n")
    while(True):#PRINTING ORDER
        print("ENTER 'print' to PRINT THE ORDER , 'next'/'done' to COMPLETE THE ORDER")
        ch = input()
        ch = ch.lower()
        if ch in ['vm','vo','create','cancel','last','done','print','next','q','m']:
            if ch == 'vm':
                showHalfMenu(cur)
            elif ch == 'vo':
                viewOrder()
            elif ch == 'create':
                create.createCustomerAccount(cur)
                print("\n\n")
            elif ch == 'last':
                print("ORDER CONFIRMED ! CANNOT BE CHANGED !!")
                print("\n\n")
            elif ch == 'done':
                break
            elif ch == 'cancel':
                print("ORDER COMPLETED SUCCESSFULLY !!")
                print("ORDER CANNOT BE CANCELLED ! RETURN BACK !!")
                return ch
            elif ch == 'next':
                print("ORDER COMPLETED SUCCESSFULLY !!")
                return ch
            elif ch == 'print':
                printBill(bill)
                print()
                break
            else:
                return ch
        else:
            print("ORDER COMPLETED SUCCESSFULLY !!")
            print("INVALID INPUT ! PLEASE TRY AGAIN !!")
    while(True):#GOING NEXT
        m = """
    ENTER : 
            next   =======> NEXT ORDER
            
            q      =======> GO BACK
            m      =======> MAIN MENU
    
    """
        print(m)
        ch = input()
        ch = ch.lower()
        if ch in ['vm','vo','create','cancel','last','done','print','next','q','m']:
            if ch == 'vm':
                showHalfMenu(cur)
            elif ch == 'vo':
                viewOrder()
            elif ch == 'create':
                create.createCustomerAccount(cur)
                print("\n\n")
            elif ch == 'last':
                print("ORDER CONFIRMED ! CANNOT BE CHANGED !!")
                print("\n\n")
            elif ch == 'done':
                return 'q'
            elif ch == 'cancel':
                
                return 'q'
            elif ch == 'next':
                return ch
            else:
                return ch
        else:
            print("INVALID INPUT ! PLEASE TRY AGAIN !!")
                   
                                       