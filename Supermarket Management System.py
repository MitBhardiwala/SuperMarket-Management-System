import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234')
c=conn.cursor()
# c.execute("create database grocery_shop")
# print("data base created")    

import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234',database='grocery_shop')
if conn.is_connected():
    print('successfully connected')

c=conn.cursor()
# c.execute('create table customer_details(phone_no INT,cust_name varchar(25),expenditure float(10))')
# print('customer_details table created')

# c.execute('create table stock_details(product_name varchar(25),price_per_kg float(10),stock float(20))')
# print('stock_details table created')

# c.execute('create table worker_details(worker_name varchar(25),worker_work varchar(30),worker_age int(3), worker_salary float(10),phone_no int(13))')
# print('worker_details table created')

# c.execute("drop database grocery_shop")
# print("successfully deleted")

import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234',database='grocery_shop')
if conn.is_connected():
    print('successfully connected')
c=conn.cursor()

while conn.is_connected():
    print('                       Super Market Management System')
    print('                                  1.login')
    print('                                  2.exit')
    choice=int(input('enter your choice:'))
    if choice==1:
        user_name=input('enter user name: ')
        password=input('enter password: ')
        while (user_name=='het' or user_name=='meet') and password=='hpmb':
            print("===============================================================================")
            print('                                    Super Market')
            print('                                  1.Purchase')
            print('                                  2.Customer details')
            print('                                  3.Stock details')
            print('                                  4.Worker details')
            print('                                  5.Exit')
            choice=int(input('enter your choice: '))
            
            if choice==1:
                import mysql.connector as sql
                conn=sql.connect(host='localhost',user='root',passwd='1234',database='grocery_shop')
                c=conn.cursor()
                p=0
                x=True
                while x:
                    print("------------------------------------------------------------------------------")
                    z=str(input("Enter the product name: "))
                    c.execute('select product_name,stock,price_per_kg from stock_details')
                    data=c.fetchall()
                    for row in data:
                        if row[0]==z:
                            print("Available Stock Details")
                            print("Product name:",row[0])
                            print("Stock:",row[1],"Kg")
                            print("Price per Kg: Rs",row[2])
                            conn.commit()
                            if row[1]>0:
                                ch=input("Do you want to buy this item? (yes/no): ")
                                if ch=='yes':
                                    q=float(input("enter how much quantity(in kg) do you want to buy: "))
                                    if q<=row[1]:
                                        g=float(row[2])*q
                                        print("The amount is: Rs",g)
                                        cho=input("Do you want to continue? (yes/no): ")
                                        if cho=='yes':
                                            c.execute('update stock_details set stock=stock- '+ str(q) +' where product_name=("{}")'.format(z))
                                            conn.commit()
                                            print("Stock updated successfully")
                                            print(q,"Kg",z,"worth Rs.",g,"is added to the bill.")
                                            p+=g
                                        elif cho=='no':
                                            print("------------------------------------------------------------------------------")
                                            continue
                                        else:
                                            print("Invalid choice")
                                            print("------------------------------------------------------------------------------")
                                            break
                                    elif q>row[1]:
                                        print('Entered quantity exceeds stock!')
                                        print("Available stock of",z,"is",row[1],"Kg")
                                        r=input("Do you want to buy remaining available stock? (yes/no): ")
                                        if r=='yes':
                                            g=float(row[2])*(row[1])
                                            print("The amount is: Rs",g)
                                            cho=input("Do you want to continue? (yes/no): ")
                                            if cho=='yes':
                                                c.execute('update stock_details set stock=0 where product_name=("{}")'.format(z))
                                                conn.commit()
                                                print("Stock updated successfully")
                                                print(row[1],"Kg",z,"worth Rs.",g,"is added to the bill.")
                                                p+=g
                                            elif cho=='no':
                                                print("------------------------------------------------------------------------------")
                                                continue
                                            else:
                                                print("Invalid choice")
                                                print("------------------------------------------------------------------------------")
                                                break
                                        elif r=='no':
                                            print("------------------------------------------------------------------------------")
                                            break
                                        else:
                                            print("Invalid choice")
                                            print("------------------------------------------------------------------------------")
                                            continue   
                                elif ch=='no':
                                    print("------------------------------------------------------------------------------")
                                    break
                                else:
                                    print("Invalid choice")
                                    print("------------------------------------------------------------------------------")
                                    continue
                            else:
                                print("Stock is empty! Sorry, you can't purchase this item")
                                print("------------------------------------------------------------------------------")
                                break
                    
                    ch=input("Do you want to buy more items? (yes/no): ")
                    if ch=='no':
                        print("------------------------------------------------------------------------------")
                        x=False
                        name=input("Enter customer's name: ")
                        import csv
                        with open(r"M:\projects\customer.csv","r") as csvread_file:
                            reader=csv.reader(csvread_file)
                            lines=[]
                            for rec in reader:
                                lines.append(rec) 
                        for i in range(1):
                            for row in lines:
                                if row[1]==name:
                                    a=int(row[2])+p
                                    row.remove(row[2])
                                    row.insert(2,a)
                                    f1=(r"E:\Projects\CS project\Project File\customer.csv")  
                                    with open(f1,'w',newline='') as f:
                                        csv_w=csv.writer(f,delimiter=',')
                                        for rec in lines:
                                            csv_w.writerow(rec)
                                    print("Successfully updated Customer record")
                                    print("Bill Amount: Rs.",p)
                                    print("Items purchased successfully")
                                    print("Thank You")
                                    break
                            if row[1]!=name:
                                phone_number=input("Enter customer's phone no. : ")
                                rows = [phone_number,name,p]
                                f1=(r"M:\projects\customer.csv")
                                with open(f1,'a+',newline='') as f:
                                    csv_w=csv.writer(f,delimiter=',')
                                    csv_w.writerow(rows)
                                print("Successfully added Customer record")
                                print("Bill Amount: Rs.",p)
                                print("Items purchased successfully")
                                print("Thank You")
                        
            while choice==2:
                print("------------------------------------------------------------------------------")
                print("                                  Customer Details")
                print("                                  1.Add Customer")
                print("                                  2.View all Customers")
                print("                                  3.Search Customer")
                print("                                  4.Delete")
                print("                                  5.Update")
                print("                                  6.Back")
                
                def inserttocsv():
                    phone_number=str(input("Enter phone number: "))
                    customername=input("Enter name: ")
                    
                    rows = [phone_number,customername,exp]
                    f1=(r"M:\projects\customer.csv")
                    with open(f1,'a+',newline='') as f:        
                        csv_w=csv.writer(f,delimiter=',')
                        csv_w.writerow(rows)
                    print("successfully added")
                    
                def readingfromcsv():
                    import csv
                    with open(r"M:\projects\customer.csv","r") as csv_file:
                        reader=csv.reader(csv_file)

                        for rec in reader:
                            print(rec)
                        row_count=len(list(reader))
                        if(row_count==0):
                            print("Empty list")
                        

                def searchingrecord():
                    import csv
                    csv_file=open(r"M:\projects\customer.csv","r")
                    reader=csv.reader(csv_file)
                    name=input("Enter name you want to search: ")
                    
                    for i in range(1):
                        for row in reader:
                            if row[1]==name:
                                print(row)
                                break
                        if row[1]!=name:
                            print("NO SUCH NAME EXISTS!")

                def deleltingrecord():
                    import csv
                    with open(r"M:\projects\customer.csv","r") as csvread_file:
                        reader=csv.reader(csvread_file)
                        name=input("Enter name you want to delete: ")
                        lines=[]
                        for row in reader:
                            lines.append(row)
                    for i in range(1):
                        for row in lines:
                            if row[1]==name:
                                lines.remove(row)
                                f1=(r"M:\projects\customer.csv")  
                                with open(f1,'w',newline='') as f:        
                                    csv_w=csv.writer(f,delimiter=',')
                                    for rec in lines:
                                        csv_w.writerow(rec)
                                print("successfully deleted")
                                break
                        if row[1]!=name:
                            print("NO SUCH NAME EXISTS!")

                def updatingrecord():
                    import csv
                    with open(r"M:\projects\customer.csvv","r") as csvread_file:
                        reader=csv.reader(csvread_file)
                        name=input("Enter name you want to update: ")
                        lines=[]
                        for row in reader:
                            lines.append(row)
                    for i in range(1):
                        new_name=''
                        for row in lines:
                            if row[1]==name:
                                new_number=str(input("Enter new number: "))
                                new_name=input("Enter new name: ")
                                new_exp=int(input("Enter new expenditure: "))
                                row.remove(row[0])
                                row.insert(0,new_number)
                                row.remove(row[1])
                                row.insert(1,new_name)
                                row.remove(row[2])
                                row.insert(2,new_exp)
                                f1=(r"M:\projects\customer.csv")  
                                with open(f1,'w',newline='') as f:        
                                    csv_w=csv.writer(f,delimiter=',')
                                    for rec in lines:
                                        csv_w.writerow(rec)
                                print("successfully updated")
                                break
                        if row[1]!=new_name:
                            print("NO SUCH NAME EXISTS!")

                ch=int(input("enter your choice: "))
                import csv
                if ch==1:
                    inserttocsv()
                elif ch==2:
                    readingfromcsv()
                elif ch==3:
                    searchingrecord()
                elif ch==4:
                    deleltingrecord()
                elif ch==5:
                    updatingrecord()
                elif ch==6:
                    break
                else:
                    print("Invalid input!! Enter again")
                    continue


            while choice==3:
                print("------------------------------------------------------------------------------")
                print("                                  Stock Details")
                print("                                  1.Add stock")
                print("                                  2.View stock")
                print("                                  3.Add new product")
                print("                                  4.Delete product")
                print("                                  5.See all products")
                print("                                  6.Search product")
                print("                                  7.Update product detail")
                print("                                  8.Back")
                ch=int(input("Enter the Choice: "))
                if ch==1:
                    import mysql.connector as sql
                    import datetime
                    conn=sql.connect(host='localhost',user='root',passwd='1234',database='grocery_shop')
                    c=conn.cursor()
                    c.execute("select product_name,price_per_kg,stock from stock_details")
                    data=c.fetchall()
                    print("(Product name, Price per Kg, Stock)")
                    for i in data:
                        print(i)
                    a=input("Enter the product name: ")
                    b=float(input("Enter how much stock to be added: "))
                    t='update stock_details set stock = stock + '+str(b)+' where product_name =("{}")'.format(a)
                    c.execute(t)
                    conn.commit()
                    c.execute('select product_name,price_per_kg,stock from stock_details where product_name=("{}")'.format(a))
                    data=c.fetchall()
                    for row in data:
                        print("Available Stock Details")
                        print("Product name: ",row[0])
                        print("Price per Kg: Rs.",row[1])
                        print("Stock: ",row[2],"Kg")
                        print("updated succesfully")

                elif ch==2:
                    import mysql.connector as sql
                    conn=sql.connect(host='localhost',user='root',passwd='1234',database='grocery_shop')
                    c=conn.cursor()
                    c.execute("select product_name,price_per_kg,stock from stock_details")
                    data=c.fetchall()
                    z=input("Enter the Product Name: ")
                    for i in range(1):
                        for i in data:
                            if i[0]==z:
                                c.execute("select product_name,price_per_kg,stock from stock_details where product_name=('{}')".format(z))
                                data=c.fetchall()
                                for row in data:
                                    print("Available Stock Details")
                                    print("Product name: ",row[0])
                                    print("Price per Kg: Rs",row[1])
                                    print("Stock: ",row[2],"Kg")
                                break
                        if i[0]!=z:
                            print("NO SUCH PRODUCT EXISTS IN STOCK!")

                elif ch==3:
                    new_product_name=input("Enter the new product name: ")
                    new_product_cost=float(input("Enter price per Kg: "))
                    new_product_stock=float(input("Enter the stock to be updated: "))
                    c.execute("insert into stock_details values('"+(new_product_name)+"',"+str(new_product_cost)+","+str(new_product_stock)+")")
                    print("updated successfully")
                    conn.commit()

                elif ch==4:
                    c.execute('select * from stock_details')
                    data=c.fetchall()
                    a=input('Enter name of the product which you want to delete: ')
                    for i in range(1):
                        for row in data:
                            if row[0]==a:
                                t='delete from stock_details where product_name=("{}")'.format(a)
                                c.execute(t)
                                conn.commit()
                                print("successfully deleted")
                                break
                        if row[0]!=a:
                            print("NO SUCH PRODUCT EXISTS IN STOCK!")

                elif ch==5:
                    t=conn.cursor()
                    t.execute('select*from stock_details')
                    record=t.fetchall()
                    print("(Product name, Price per Kg, Stock)")
                    for i in record:
                        print(i)

                elif ch==6:
                    a=input('Enter product name you want to search: ')
                    q='select * from stock_details'
                    c.execute(q)
                    data=c.fetchall()
                    for i in range(1):
                        for i in data:
                            if i[0]==a:
                                t='select*from stock_details where product_name=("{}")'.format(a)
                                c.execute(t)
                                v=c.fetchall()
                                print(v)
                                break
                        if i[0]!=a:
                            print("NO SUCH PRODUCT EXISTS IN STOCK!")

                elif ch==7:
                    a=input('Enter product name you want to update: ')
                    q='select * from stock_details'
                    c.execute(q)
                    data=c.fetchall()
                    for i in range(1):
                        for row in data:
                            if row[0]==a:
                                x=input("Enter what do you want to update(name/cost): ")
                                if x=='name':
                                    var1=input("Enter the new name: ")
                                    t='update stock_details set product_name=("{}")'.format(var1)
                                    s=' where product_name=("{}")'.format(a)
                                    print("successfully updated")
                                elif x=='cost':
                                    var1=input("Enter the new cost: ")
                                    t='update stock_details set price_per_kg='+(var1)+' where product_name=("{}")'.format(a)
                                    s=''
                                    print("successfully updated")
                                c.execute(t+s)
                                conn.commit()
                                break
                        if row[0]!=a:
                            print("NO SUCH PRODUCT EXISTS IN STOCK!")

                elif ch==8:
                    break

                else:
                    print("invalid input!! enter again")
                    continue

            while choice==4:
                print("------------------------------------------------------------------------------")
                print("                                  Employee Details")
                print("                                  1.Add Employee")
                print("                                  2.View all details")
                print("                                  3.Search Employee")
                print("                                  4.Delete")
                print("                                  5.Update")
                print("                                  6.Back")
                ch=int(input("enter your choice: "))
                if ch==1:
                    worker_name=input('Enter name: ')
                    worker_work=input('Enter work: ')
                    worker_age=int(input('Enter age: '))
                    worker_salary=float(input('Enter salary: '))
                    phone_no =int(input('Enter phone number: '))
                    sql_insert="insert into worker_details values(" "'"+(worker_name)+"'," "'"+(worker_work)+"',"+str(worker_age)+","+str(worker_salary)+","+str(phone_no)+")"
                    c.execute(sql_insert)
                    conn.commit()
                    print("updated successfully")

                elif ch==2:
                    t=conn.cursor()
                    t.execute('select*from worker_details')
                    record=t.fetchall()
                    for i in record:
                        print(i)

                elif ch==3:
                    a=input('Enter name you want to search: ')
                    q='select * from worker_details'
                    c.execute(q)
                    data=c.fetchall()
                    for i in range(1):
                        for i in data:
                            if i[0]==a:
                                t='select*from worker_details where worker_name=("{}")'.format(a)
                                c.execute(t)
                                v=c.fetchall()
                                print(v)
                                break
                        if i[0]!=a:
                            print("NO SUCH NAME EXISTS!")

                elif ch==4:
                    a=input('Enter name you want to delete: ')
                    q='select * from worker_details'
                    c.execute(q)
                    data=c.fetchall()
                    for i in range(1):
                        for row in data:
                            if row[0]==a:
                                t='delete from worker_details where worker_name=("{}")'.format(a)
                                c.execute(t)
                                conn.commit()
                                print("successfully deleted")
                                break
                        if row[0]!=a:
                            print("NO SUCH NAME EXISTS!")

                elif ch==5:
                    a=input('Enter name you want to update: ')
                    q='select * from worker_details'
                    c.execute(q)
                    data=c.fetchall()
                    for i in range(1):
                        for row in data:
                            if row[0]==a:
                                x=input("Enter what do you want to update(name/phone/salary/age/work): ")
                                if x=='name':
                                    var1=input("Enter the new name: ")
                                    t='update worker_details set worker_name=("{}")'.format(var1)
                                    s='where worker_name=("{}")'.format(a)
                                    c.execute(t+s)
                                    conn.commit()
                                    print("successfully updated")
                                elif x=='phone':
                                    var1=input("Enter the new phone_no: ")
                                    t='update worker_details set phone_no='+(var1)+' where worker_name=("{}")'.format(a)
                                    c.execute(t)
                                    conn.commit()
                                    print("successfully updated")
                                elif x=='salary':
                                    var1=input("Enter salary: ")
                                    t='update worker_details set worker_salary='+(var1)+' where worker_name=("{}")'.format(a)
                                    c.execute(t)
                                    conn.commit()
                                    print("successfully updated")
                                elif x=='age':
                                    var1=input("Enter the new age: ")
                                    t='update worker_details set worker_age='+(var1)+' where worker_name=("{}")'.format(a)
                                    c.execute(t)
                                    conn.commit()
                                    print("successfully updated")
                                elif x=='work':
                                    var1=input("Enter the new work: ")
                                    t='update worker_details set worker_work=("{}")'.format(var1)
                                    s='where worker_name=("{}")'.format(a)
                                    c.execute(t+s)
                                    conn.commit()
                                    print("successfully updated")
                                break
                        if row[0]!=a:
                            print("NO SUCH NAME EXISTS!")

                elif ch==6:
                    break

                else:
                    print("Invalid input!! Enter again")
                    continue

            while choice==5:
                exit()

            if choice not in [1,2,3,4,5]:
                print("Invalid input!! Enter again")

        else:
            print('Wrong username or password!! Try again')
            
    elif choice==2:
        exit()
