
def viewPoints(cust_id,cur):#TESTED
    cur.execute('select points from customers where mobile = :1',(cust_id,))
    res = cur.fetchall()
    res = res[0][0]
    print("Your points are : ",str(res))                                    

def viewOrdersCustomerLatest(cust_id,cur):#TESTED
    cur.execute('select max(ordid) from orders where custid=:1',(cust_id,))
    res = cur.fetchall()
    res = res[0]
    cur.execute("select * from orders where ordid=:1",(res[0],))
    last = cur.fetchall()
    last = last[0]
    cur.execute('select name from customers where mobile=:1',(cust_id,))
    res = cur.fetchall()
    name = res[0][0]
    print("Name :",name)
    print("Order id : ",last[0])
    print("Date : ",last[3])
    print("Bill amount : ",last[4])
    print("Bill Details : ",last[5])
    
def viewOrdersCustomer(cust_id,cur):#TESTED
    cur.execute('select name from customers where mobile=:1',(cust_id,))
    res = cur.fetchall()
    name = res[0][0]
    cur.execute('select * from orders where custid=:1 order by ordid',(cust_id,))
    res = cur.fetchall()
    print("Name :",name)
    for last in res:
        #print(last) FOR CHECKING/DEBUGGING PURPOSE
        print("Order id : ",last[0])
        print("Date : ",last[3])
        print("Bill amount : ",last[4])
        print("Bill Details : ",last[5])
        print("\n\n")
        
def viewDetailsEmployee(empid, cur):#TESTED
    #VIEW DETAILS OF ANY EMPLYOYEE ADMIN/MANAGER/CASHIER
    cur.execute('select * from employees where empid=:1',(empid,))
    res = cur.fetchall()
    res = res[0]
    print("EMPLOYEE ID : ",res[0])
    print("NAME : ",res[1])
    print("MOBILE NUMBER : ",res[2])
    print("ADDRESS : ",res[3])
    print("GENDER : ",res[4])
    print("DATE OF BIRTH : ",res[5])
    print("DATE OF JOINING : ",res[6])
    if res[8] == "INACTIVE":#TO CHECK WHETHER EMPLOYEE IS STILL ACTIVE OR FIRED
        print("DATE OF FIRED : ",res[7])
    print("STATUS : ",res[8])
    print("PASSWORD : ",res[9])
    print("SALARY : ",res[10])
    print("DESIGNATION : ",res[11])
    print("LOCK STATUS : ",res[12])
        
def viewDetailsEmployeeAll(specific, des, cur):#TESTED
    #DETAILS OF EVERY EMPLOYEE
    #DES FOR SEPRATE VIEW'S TO MANAGER AND ADMIN - MANAGER , ADMIN
    #SPECIFIC CAN TAKE ONLY 3 PARAMTERS - ACTIVE , INACTIVE, ALL
    specific = specific.upper()
    des = des.upper()
    if specific == 'ACTIVE':
        if des == 'ADMIN':
            cur.execute("select empid from employees where status='ACTIVE' order by empid")
        else:
            cur.execute("select empid from employees where status='ACTIVE' and designation = 'CASHIER' order by empid")
    elif specific =='INACTIVE':
        if des == 'ADMIN':
            cur.execute("select empid from employees where status='INACTIVE' order by empid")
        else:
            cur.execute("select empid from employees where status='INACTIVE' and designation = 'CASHIER' order by empid")
    else :
        if des == 'ADMIN':
            cur.execute("select empid from employees order by empid")
        else:
            cur.execute("select empid from employees where designation = 'CASHIER' order by empid")
    res = cur.fetchall()
    for tup in res:
        empid = tup[0]
        viewDetailsEmployee(empid, cur)
        print("---------------------------------------------------------------------")

def viewDetailsCustomer(cust_id, cur):#TESTED
    cur.execute('select * from customers where mobile=:1',(cust_id,))
    res = cur.fetchall()
    res = res[0]
    print("NAME : ",res[0])
    print("MOBILE : ",res[1])
    print("GENDER : ",res[2])
    print("CUSTOMER SINCE : ",res[3])
    print("POINTS : ",res[4])
    print()
    print()
    print("LAST ORDER WAS")
    viewOrdersCustomerLatest(cust_id, cur)
    
def viewMenu(prid, cur):#TESTED
    cur.execute("select * from menu where prid=:1",(prid,))
    res = cur.fetchall()
    res = res[0]
    print("PRODUCT ID : ",res[0])
    print("PRODUCT NAME : ",res[1])
    print("PRICE-    SMALL: ",res[2],"    MEDIUM: ",res[3],"    LARGE: ",res[4])
    print("SHORTCUT : ",res[5])
    print("TYPE : ",res[6])
    print("DETAILS : ",res[7])

def viewMenuAll(specific, cur):#TESTED
    #CAN TAKE ALL VEG NON_VEG AS PARAMETERS
    if specific == 'VEG':
        cur.execute("select prid from menu where type='VEG'")
    elif specific == 'NON-VEG':
        cur.execute("select prid from menu where type='NON-VEG'")
    else:
        cur.execute("select prid from menu")
    res = cur.fetchall()
    for tup in res:
        prid = tup[0]
        viewMenu(prid, cur)
        print("---------------------------------------------------------------------")
        
def viewSalesDay(day, cur):#TESTED
    #TAKES INPUT ONLY IN dd/mm/yy DISPLAYS SALES OF A PRTICULAR DAY
    a,b,c = day.split('/')
    mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    day = a+"-"+mon[int(b)]+"-"+c
    
    cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 ",(day,))
    res = cur.fetchall()
    #print(res)
    res = res[0]
    if res[2] == None:
        print("NO RECORD TO DISPLAY")
    else:
        print("TOTAL SALES : RS ",res[2])
        print("TOTAL ORDERS : ",res[0])
        print("TOTAL NUMBER OF DISTINCT CUSTOMERS : ",res[1])
    
def viewSalesMonth(monthnum, cur):#TESTED
    #DISPLAY SALES OF A PRTICULAR MONTH
    cur.execute('SELECT count(ordid), count( DISTINCT custid),sum(bill) FROM orders WHERE EXTRACT(month from time) = :1',(monthnum,))
    res = cur.fetchall()
    #print(res)
    res = res[0]
    mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
    if res[2] == None:
        print("NO RECORD OF THE MONTH EXISTS")
    else:
        print("RECORD OF THE MONTH : ",mon[monthnum])
        print("TOTAL SALES : RS ",res[2])
        print("TOTAL ORDERS : ",res[0])
        print("TOTAL NUMBER OF DISTINCT CUSTOMERS : ",res[1])
        cur.execute('select BILL,DY from (select sum(bill) as BILL,trunc(time) as DY from orders group by trunc(time)order by BILL desc ) where rownum = 1')
        res = cur.fetchall()
        res = res[0]
        x = str(res[1])
        dat = x.split();
        dat = dat[0]
        a,b,c = dat.split('-');
        datee = c+"/"+b+"/"+a;
        print("---------------------------------------------------------------------")
        print("HIGHEST SALES DAY WAS: ",datee)
        viewSalesDay(datee, cur)
        print("---------------------------------------------------------------------")
        cur.execute('select BILL,DY from (select sum(bill) as BILL,trunc(time) as DY from orders group by trunc(time)order by BILL ) where rownum = 1')
        res = cur.fetchall()
        res = res[0]
        x = str(res[1])
        dat = x.split();
        dat = dat[0]
        a,b,c = dat.split('-');
        datee = c+"/"+b+"/"+a;
        print("LOWEST SALES DAY WAS: ",datee)
        viewSalesDay(datee, cur)

def viewSaleDayEmployee(day, empid, cur):#TESTED
    #DISPLAY SALES DETAIL OF AN EMPLOYEE ON A PARTICULAR DAY WITH SOME DETAILS
    a,b,c = day.split('/')
    mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    day = a+"-"+mon[int(b)]+"-"+c
    cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 and empid=:2",(day,empid))
    res = cur.fetchall()
    #print(res)
    res = res[0]
    if res[2] == None:
        print("NO RECORD TO DISPLAY")
    else:
        cur.execute('select empid,name,mobile,gender from employees where empid=:1',(empid,))
        res2 = cur.fetchall()
        res2 = res2[0]
        print("TOTAL SALE DONE BY ",res2[1]," is ",res[2])
        print("NUMBER OF ORDERS FULFILLED : ",res[0])
        print("NUMBER OF CUSTOMERS HANDLED : ",res[1])
        print()
        print("OTHER DETAILS :")
        print("EMPID : ",res2[0])
        print("NAME : ",res2[1])
        print("MOBILE : ",res2[2])
        print("GENDER : ",res2[3])
    
def viewSaleMonthEmployee(month, empid, cur):#TESTED
    #DISPLAY SALES BY AN EMPLOYEE OVERALL OF A MONTH
    month = int(month)
    cur.execute('select sum(bill), count(ordid), count(DISTINCT custid) from orders where EXTRACT(month from time) = :1 and empid = :2',(month,empid))
    res = cur.fetchall()
    #print(res)
    res= res[0]
    if res[0] == None:
        print("NO RECORD TO DISPLAY, PLEASE ENTER VALID MONTH OR EMPLOYEE ID")
    else:
        print("EMPLOYEE ID : ",empid)
        mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
        print("MONTH : ",mon[month])
        print("TOTAL SALES : RS ",res[0])
        print("ORDERS TAKEN : ",res[1])
        print("NUMBER OF DISTINCT CUSTOMERS : ",res[2])

def viewSaleMonthEmployeeAll(month, specific, cur):#TESTED
    #GIVES THE EMPLOYEES HIGHEST,LOWEST, ALL details with same parameters
    specific = specific.upper()
    cur.execute('select DISTINCT EXTRACT(MONTH from time) from orders')
    res = cur.fetchall()
    found = False
    for tup in res:
        if tup[0] == month:
            found = True
            break
    if found:#TO VALIDATE WHETHER MONTH EXIST OR NOT
            
        if specific == 'HIGHEST' :
            cur.execute('select empid from(select sum(bill) as BILL, empid from orders group by empid order by BILL desc) where rownum = 1 ')
            res = cur.fetchall()
            empid = res[0][0]
            print("HIGHEST SALES DONE BY : ")
            viewSaleMonthEmployee(month, empid, cur)
        elif specific == "LOWEST":
            cur.execute('select empid from(select sum(bill) as BILL, empid from orders group by empid order by BILL ) where rownum = 1 ')
            res = cur.fetchall()
            empid = res[0][0]
            print("LOWEST SALES DONE BY : ")
            viewSaleMonthEmployee(month, empid, cur)
        else :
            cur.execute('select DISTINCT empid from orders where EXTRACT(month from time) = : 1',(month,))
            res = cur.fetchall()
            for tup in res :
                empid = tup[0]
                viewSaleMonthEmployee(month, empid, cur)
                print("---------------------------------------------------------------------")
    
    else:
        print("NO RECORD OF THE MONTH EXISTS")
                
        
