import mysql.connector 
def show():
   show=1
   while show:
      print()
      print(" -----------------------------SHOW---------------------------------------------- ")
      print("|                             1. BOOKING DETAILS                                |")
      print("|                             2. CUSTOMER INFORMATION                           |")
      print("|                             3. ROOMS                                          |")
      print("|                             4. BILLS                                          |")
      print(" --------------------------------------------------------------------------------")
      print()
      ch=int(input("Enter your choice:: "))
      print()
      con=mysql.connector.connect(host="localhost",user="root",passwd="Password4MySQL",database="hotel_mang_prj")
      cur=con.cursor()

      
      #TO SHOW BOOKING DETAILS OF CUSTOMER
      if ch==1:
         record=0
         query="select * from cust_book"
         cur.execute(query)
         data=cur.fetchall()

         #IF "CUSTOMER" TABLE HAS RECORDS  
         if data and record==0:
            print("| Rg_N |Name of Customer| Rm_No | Ch_In_Date | ch_Out_Date |Fd_Type|Advance|Room_Type|")
            print("| ---- |----------------| ----- | ---------- | ----------- |-------|-------|---------|")
            record=1
            #TO ADJUST THE RETIEVED INFORMATION IN TABULAR FORM
            for i in data:
               p=""
               len_name=16-len(i[1])
               for j in range(0,len_name-1):
                  p=p+" "
                  
               print(" "+str(i[0])+"   ",i[1]+p," "+str(i[2])+" ","   "+str(i[3])+" "," "+str(i[4])+"    ",i[5],"  ",i[6],"  ",i[7])
               print()

         #IF NO RECORD PRESENT IN CUSTOMER i.e. data=0 AFTER cur.fetchall()
         elif record==0:
            print("----------------------------SORRY NO MORE RECORDS---------------------")
            print()

         

      #TO SHOW CUSTOMER DETAILS FROM TABLE CUSTOMER
      elif ch==2:
         query="select * from customer"
         cur.execute(query)
         data=cur.fetchall()

         #AFTER RETRIEVING RECORDS FROM TABLE CUSTOMER
         if data:
            print("| Rg_N |        Name        |     Address    |   Phone no   |   Status   |")
            print("| ---- |    ------------    |    ---------   |   ---------  |  --------  |")
            for i in data:
               p=""
               l_name=20-len(i[1])
               for j in range(0,l_name):
                  p=p+" "
               q=""
               l_add=16-len(i[2])
               for j in range(0,l_add-1):
                  q=q+" "
               r=""
               l_ph=10-len(str(i[3]))
               for j in range(0,l_ph-1):
                  r=r+" "
               s=""
               l_status=12-len(i[4])
               for j in range(0,l_status-1):
                  s=s+" "
               print(" "+str(i[0]),"   ",i[1]+p," ",i[2]+q,str(i[3])+r,"   ",i[4]+s)
               print()
         #IF NO RECORDS IN TABLE CUSTOMER
         else:
            print("-------------------------------NO MORE RECORDS----------------------------------")



      #IF CHOICE IS TO SHOW ROOM DETAILS
      elif ch==3:
         query="select * from rooms"
         cur.execute(query)
         data=cur.fetchall()
         print("|RoomNo| RoomType | RoomRent | Status |")
         print("---------------------------------------")
         #AFTER RETRIEVING RECORDS FROM TABLE ROOMS,TO ADJUST RECORDS IN TABULAR FORM
         for i in data:
            if i[1]=='AC':
               print(" ",i[0],"    ",i[1],"      ",i[2],"  ",i[3])
            else:
               print(" ",i[0],"   ",i[1],"    ",i[2],"  ",i[3])



      #IF CHOICE IS TO SHOW BILL DETAILS
      elif ch==4:
         query="select * from bill"
         cur.execute(query)
         data=cur.fetchall()
         print("|RegNo| NoOfDays | CheckInDate | TotalAmt |RoomNo| Paid  | Advance |FoodType")
         print("----------------------------------------------------------------------------")
         #AFTER RETRIEVING RECORDS FROM TABLE BILL
         if data:
            for i in data:
               p=""
               len_rno=6-len(str(i[0]))
               for j in range(0,len_rno-1):
                  p=p+" "
               q=""
               len_rno=10-len(str(i[3]))
               for j in range(0,len_rno-1):
                  q=q+" "
               s=""
               len_rno=9-len(str(i[6]))
               for j in range(0,len_rno-1):
                  s=s+" "
               print(str(i[0])+p,"    ",i[1],"      ",i[2],"  ",str(i[3])+q,i[4],"  ",i[5],"   ",str(i[6])+s,i[7])
            print("-----------------------------------------------------------------------------")
         else:
            print("                          SORRY, NO MORE RECORDS                               ")
      else:
         show=int(input("do you want to continue to show details again? 1/0:: "))
   


   
def update_info():
   update=1
   while update:
      print(" ---------------------------UPDATE---------------------------------- ")
      print("|                      1. CUSTOMER INFORMATION                      |")
      print("|                      2. ROOMS                                     |")
      print(" ------------------------------------------------------------------- ")
      ch=int(input("\nEnter your choice::"))
      con=mysql.connector.connect(host="localhost",user="root",passwd="Password4MySQL",database="hotel_mang_prj")
      cur=con.cursor()
      
      #CHOOSING OPTION TO UPDATE CUSTOMER INFORMATION
      if ch==1:
         c_info=1
         '''TO UPDATE, RETRIEVE INFORMATION FROM CUSTOMER TABLE OF THOSE CUSTOMER, WHOSE REGISTRATION
         NUMBER IS MATCHED WITH THE REGISTRATION NUMBER ENTERED BY THE USER AND ROOM_STATUS=RESERVED'''
         while c_info:
            flag=0
            query="select * from customer where room_status='reserved'"
            cur.execute(query)
            data=cur.fetchall()
            if data and flag==0:
               print("| reg_no |      name      |     address    |  phone number  |   room_status  |")
               print("|----------------------------------------------------------------------------|")
               for i in data:
                  n=""
                  len_nam=16-len(str(i[1]))
                  for j in range(0,len_nam-1):
                     n=n+" "
                  k=""
                  len_add=16-len(str(i[2]))
                  for j in range(0,len_add-1):
                     k=k+" "
                  m=""
                  len_ph=16-len(str(i[3]))
                  for j in range(0,len_ph-1):
                     m=m+" "
                  print("   ",i[0]," "," ",i[1]+n,"    ",i[2]+k,str(i[3])+m,i[4]+n)
               
               
               reg_no=int(input("\n\nEnter the registration number whose information needs to be updated::"))
               query="select room_status from customer where r_no={} and room_status='reserved'".format(reg_no)
               cur.execute(query)
               data=cur.fetchall()
               print(data)
               for i in data:
                  #UPDATE INFORMATION OF RESERVED CUSTOMER AFTER RETRIEVING RECORDS FROM TABLE CUSTOMER
                  if i[0]=="reserved":
                     name=input("\n\nEnter the name::")
                     addr=input("Enter the address::")
                     phno=input("Enter the phone number::")
                     query="update customer set name='{}',addr='{}',phno='{}' where r_no={}".format(name,addr,phno,reg_no)
                     cur.execute(query)
                     

                     #UPDATE CUST_BOOK TABLE TOO(CONTAINS CUSTOMERS WHO RESERVED THE ROOM)
                     query="update cust_book set name='{}' where reg_no={}".format(name,reg_no)
                     cur.execute(query)
                     print("\n\n                            Updated successfully\n\n")
                     con.commit()
                     flag=1

                     query="select * from customer where room_status='reserved'"
                     cur.execute(query)
                     data=cur.fetchall()

                     #AFTER RETRIEVING RECORDS FROM TABLE CUSTOMER
                     if data:
                        print("| Rg_N |        Name        |     Address    |   Phone no   |   Status   |")
                        print("| ---- |    ------------    |    ---------   |   ---------  |  --------  |")
                        for i in data:
                           p=""
                           l_name=20-len(i[1])
                           for j in range(0,l_name):
                              p=p+" "
                           q=""
                           l_add=16-len(i[2])
                           for j in range(0,l_add-1):
                              q=q+" "
                           r=""
                           l_ph=10-len(str(i[3]))
                           for j in range(0,l_ph-1):
                              r=r+" "
                           s=""
                           l_status=12-len(i[4])
                           for j in range(0,l_status-1):
                              s=s+" "
                           print(" "+str(i[0]),"   ",i[1]+p," ",i[2]+q,str(i[3])+r,"   ",i[4]+s)
                           print()

                     
                  break
            if flag==0:
               print("Sorry, No more reserved customer's data")
            c_info=int(input("Do u want to update customer's information again? 1/0::"))


      #CHOOSING OPTION TO UPDATE ROOM'S INFORMATION  
      elif ch==2:
         r_info=1
         while r_info:
            print("THE ROOM INFORMATION AVAILABLE IS")
            print("---------------------------------\n")
            query="select * from rooms"
            cur.execute(query)
            data=cur.fetchall()
            print("|RoomNo| RoomType | RoomRent | Status |")
            print("---------------------------------------")
            for i in data:
               if i[1]=='AC':
                  #TO ARRANGE THE DATA IN TABULAR FORM
                  print(" ",i[0],"    ",i[1],"      ",i[2],"  ",i[3])
               else:
                  print(" ",i[0],"   ",i[1],"    ",i[2],"  ",i[3])
            print(" --------------------------- ")
            print("|         1. ADD            |")
            print("|         2. UPDATE         |")
            print(" --------------------------- ")
         
            ch=int(input("Enter your choice::"))

            #THIS QUERY IS COMMON TO 1.ADD AND 2.UPDATE
            query="select room_no,room_type from rooms"
            cur.execute(query)
            data=cur.fetchall()
            

            
            #CHOICE 1 TO ADD NEW ROOM NUMBER, SELECT ITS ROOM TYPE, AC/DELUX/NONAC
            if ch==1:
               list1=[]
               #ARRANGE ALL EXISTED ROOMS IN A SINGLE LIST
               for i in data:
                  print(i[0]," ",i[1])
                  list1.append(i[0])
               r_no=int(input("Enter the room number::"))
               #IF ENTERED ROOM NUMBER IS NOT IN THE LIST THEN AND THEN ONLY ADD IT, OTHERWISE REJECT
               if r_no not in list1:
                  r_type=input("Enter the room_type")
                  if r_type=='AC':
                     r_rent=3200.00
                  elif r_type=="DELUX":
                     r_rent=3000.00
                  else:
                     r_rent=2200.00
                  status='free'
                  query="insert into rooms values({},'{}',{},'{}')".format(r_no,r_type,r_rent,status)
                  cur.execute(query)
                  con.commit()
                  print("successfully added")
                  flag=1
               else:
                  print("room number is already existed, try for another room number")


            #CHOICE 2 TO UPDATE ROOM'S INFORMATION
            elif ch==2:
               list1=[]
               for i in data:
                  print(i[0],i[1])
                  list1.append(i[0])
               #print(list1)
               r_no=int(input("\n\nEnter the room number whose information has to be updated"))
               if r_no not in list1:
                  print("room number is not existed, updation is not possible,try once again")
               else:
                  r_type=input("Enter the room_type")
                  r_rent=float(input("Enter the room rent"))
                  status=input("Enter the status")
                  query="update rooms set room_type='{}',room_rent={},status='{}' where room_no={}".format(r_type,r_rent,status,r_no)
                  cur.execute(query)
                  con.commit()
                  print("Updated successfully")
            else:      
               r_info=int(input("Do you want to continue update of customer's information? 1/0:: "))
      else:
         print("\n")     
         update=int(input("Do u want to continue with update 1/0::"))

#TO DELETE ROOM'S INFORMATION AND CUSTOMER'S INFORMATION FROM DATABASE                 
def delete_info():
   del_info=1
   con=mysql.connector.connect(host="localhost",user="root",passwd="Password4MySQL",database="hotel_mang_prj")
   cur=con.cursor()
   while del_info:
      print(" -------------------DELETE INFORMATION---------------------")
      print("|                   1. ROOMS(delete if free)              |")
      print("|                   2. CUSTOMER INFORMATION                    |")
      print(" ----------------------------------------------------------")
      ch=int(input("\n\nEnter your choice::  "))
      if ch==1:
         #TO DELETE ROOM'S INFORMATION, FETCH ROOM NUMBER AND ITS STATUS, TO CHECK WHETHER THE ROOM IS
         #FREE OR RESERVED
         query="select room_no,status from rooms"
         cur.execute(query)
         data=cur.fetchall()
         flag=0
         if data:
            for i in data:
               print(i)
            con.commit()
            #ROOM CAN BE REMOVED FROM DATABASE, IF ITS STATUS IS FREE.
            r_no=int(input("Enter the room number which is to be removed from database"))
            query="delete from rooms where room_no={} and status='free'".format(r_no)
            cur.execute(query)
            con.commit()
            print("                               Deleted successfully\n\n")
         else:
            print("room can not be removed from database because the room's status is reserved")
         
      elif ch==2:
      #TO DELETE CUSTOMER'S INFORMATION
         query="select * from customer"
         cur.execute(query)
         data=cur.fetchall()
         #TO ARRANGE THE CUSTOMER'S INFORMATION IN TABULAR FORM
         print("   reg_no    |      name     |     address    |     phone_no   |    status  |")
         print("-----------------------------------------------------------------------------")
         for i in data:
            n=""
            len_nam=16-len(str(i[1]))
            for j in range(0,len_nam-1):
               n=n+" "
            k=""
            len_add=16-len(str(i[2]))
            for j in range(0,len_add-1):
               k=k+" "
            m=""
            len_ph=16-len(str(i[3]))
            for j in range(0,len_ph-1):
               m=m+" "
            print("   ",i[0]," "," ",i[1]+n,"    ",i[2]+k,str(i[3])+m,i[4]+n)
         print()
         rg_no=int(input("\n\nEnter the registration number of customer whose information has to be deleted if his room status is free::"))
         del_record=0
         for i in data:
            #CUSTOMER'S INFORMATION CAN BE UPDATED, ONLY IF REGISTRATION NUMBER IS MATCHED WITH THE
            #USER'S REGISTRATION NUMBER AND STATUS IS FREE
            if rg_no==i[0] and i[4]=="free":
               query="delete from customer where r_no={} and room_status='free'".format(rg_no)
               cur.execute(query)
               con.commit()
               #IF CONDITION IS SATISFIED, DELETION IS DONE AND RECORD WILL BE DELETED FROM CUSTOMER TABLE
               del_record=1
               print("                             Deleted successfully\n\n")

               query="select * from customer"
               cur.execute(query)
               data=cur.fetchall()

               #AFTER RETRIEVING RECORDS FROM TABLE CUSTOMER
               if data:
                  print("| Rg_N |        Name        |     Address    |   Phone no   |   Status   |")
                  print("| ---- |    ------------    |    ---------   |   ---------  |  --------  |")
                  for i in data:
                     p=""
                     l_name=20-len(i[1])
                     for j in range(0,l_name):
                        p=p+" "
                     q=""
                     l_add=16-len(i[2])
                     for j in range(0,l_add-1):
                        q=q+" "
                     r=""
                     l_ph=10-len(str(i[3]))
                     for j in range(0,l_ph-1):
                        r=r+" "
                     s=""
                     l_status=12-len(i[4])
                     for j in range(0,l_status-1):
                        s=s+" "
                     print(" "+str(i[0]),"   ",i[1]+p," ",i[2]+q,str(i[3])+r,"   ",i[4]+s)
                     print()

               
         #IF CONDITION IS NOT SATISFIED,THEN DELETION WILL NOT POSSIBLE, BECAUSE RECORD IS NOT PRESENT
         if del_record==0:
            print("Registration number is not valid/room is already reserved, can't be deleted") 
      else:
         del_info=int(input("Do u want to continue to delete information? 1/0 :: "))
         
#TO BOOK ROOM FOR NEW CUSTOMER BY USING DATABASE TABLE "cust_book"
def booking_info():
   con=mysql.connector.connect(host="localhost",user="root",passwd="Password4MySQL",database="hotel_mang_prj")
   cur=con.cursor()
   #TO SHOW ALREADY DETAILS OF BOOKED CUSTOMER WITH REGISTERED NUMBERS
   query="select reg_no from cust_book"
   cur.execute(query)
   print("                             already registered numbers are::            ")
   print("                            ---------------------------------            ")
   data=cur.fetchall()
   if data:
      for i in data:
         print("                                      ",i[0],"                          ")
   else:
      print("                            SORRY....!NO MORE REGISTERED RECORDS                  \n\n")
   #ENTER THE CUSTOMER'S INFORMATION
   reg_no=int(input("Enter the 4 digit registraton number to book for new customer::"))
   name=input("Enter the name of customer::")
   addr=input("Enter the address of customer::")
   pno=int(input("Enter the phone number::"))
   check_in=input("Enter the check-in date::")
   check_out=input("Enter the check-out date::")
   r_type=input("Enter the room type AC/DELUX/NONAC?::")
   menu_type=input("Enter your menu type, VEG/NONVEG?::")
   if menu_type=='VEG':
      veg=int(input("Enter the veg type::1. THAALI 2. SNACKS::"))
      if veg==1 or veg==2:
         charges=500
   else:
      charges=500
   advance=float(input("Enter the advance amount above 1000::"))
   #TO ALLOT ROOM, FETCH FREE ROOMS FROM DATABASE ROOMS 
   query="select room_no from rooms where room_type='{}' and status='{}'".format(r_type,'free')
   cur.execute(query)
   data=cur.fetchall()
   print("                AVAILABLE ROOMS ARE                  ")
   for i in data:
      print("                          ",i[0],"                 ")
   r_no=int(input("Enter the alloted room number::"))
   query="insert into cust_book values({},'{}',{},'{}','{}','{}',{},'{}')".format(reg_no,name,r_no,check_in,check_out,menu_type,advance,r_type)
   cur.execute(query)
   #BOOKING DETAILS OF CUSTOMER ALSO HAS TO SAVE IN CUSTOMER TABLE FOR FUTURE USE
   query="insert into customer values({},'{}','{}',{},'{}')".format(reg_no,name,addr,pno,'reserved')
   cur.execute(query)
   #THE ALLOTED ROOM SHOULD BE SET AS 'RESERVED' IN ROOM TABLE TOO, SO THAT THE SAME ROOM NUMBER SHOULDN'T ALLOTED AGAIN.
   query="update rooms set status='{}' where room_no={}".format("reserved",r_no)
   cur.execute(query)
   print("\n                                successfully registered                                     \n\n")
   query="select * from cust_book"
   cur.execute(query)
   data=cur.fetchall()

   #IF "CUSTOMER" TABLE HAS RECORDS  
   if data:
      print("| Rg_N |Name of Customer| Rm_No | Ch_In_Date | ch_Out_Date |Fd_Type|Advance|Room_Type|")
      print("| ---- |----------------| ----- | ---------- | ----------- |-------|-------|---------|")
      #record=1
      #TO ADJUST THE RETIEVED INFORMATION IN TABULAR FORM
      for i in data:
         p=""
         len_name=16-len(i[1])
         for j in range(0,len_name-1):
            p=p+" "
            
         print(" "+str(i[0])+"   ",i[1]+p," "+str(i[2])+" ","   "+str(i[3])+" "," "+str(i[4])+"    ",i[5],"  ",i[6],"  ",i[7])
         print()
   con.commit()




#BEFORE LEAVING HOTEL, CUSTOMER HAS TO PAY BILLS
def bill_generate():
   con=mysql.connector.connect(host="localhost",user="root",passwd="Password4MySQL",database="hotel_mang_prj")
   cur=con.cursor()
   #TO GENERATE BILL, SHOW THE DETAILS OF CUSTOMER FROM 'cust_book' TABLE
   query="select reg_no,name from cust_book"
   cur.execute(query)
   data=cur.fetchall()
   if data:
      print("REGISTRATION NUMBER","|","NAME of CUSTOMER")
      for i in data:
         print("      ",i[0],"       ","   ",i[1])
      reg_no=int(input("Enter the registeration number:: "))
      #COPY CUSTOMER DETAILS FROM 'cust_book' TABLE INTO 'bill' TABLE(THE TABLE WHICH CONTAINS THE DETAILS OF CUSTOMER WHO LEFT THE HOTEL)
      query="select reg_no,date(ch_out)-date(ch_in),ch_out,room_no,advance,menu_type from cust_book where reg_no={}".format(reg_no)
      cur.execute(query)
      data=cur.fetchall()
      for i in data:
         d1=i[0]
         d2=i[1]
         d3=i[2]
         d4=i[3]
         d5=i[4]
         d6=i[5]
      query="insert into bill(reg_no,no_days,ch_out,room_no,advance,menu)values({},{},'{}',{},{},'{}')".format(d1,d2,d3,d4,d5,d6)
      cur.execute(query)
      query="select reg_no,menu_type,room_type,date(ch_out)-date(ch_in),advance,room_no from cust_book where reg_no={}".format(reg_no)
      cur.execute(query)
      data=cur.fetchall()
      for i in data:
         if i[0]==reg_no:
            room_number=i[5]
            if i[1]=='VEG':
               if i[2]=='AC':
                  t_amt=i[3]*(500+3200)-i[4]
                  print("Total amount has to be paid is::",t_amt)
                  
                  
               elif i[2]=='DELUX':
                  t_amt=i[3]*(500+3000)-i[4]
                  print("Total amount has to be paid is::",t_amt)
                  
               else:
                  t_amt=i[3]*(500+2200)-i[4]
                  print("Total amount has to be paid is::",t_amt)
                  
            elif i[1]=='NONVEG':
               if i[2]=='AC':
                  t_amt=i[3]*(500+3200)-i[4]
                  print("Total amount has to be paid is::",t_amt)
                  
               elif i[2]=='DELUX':
                  t_amt=i[3]*(500+3000)-i[4]
                  print("Total amount has to be paid is::",t_amt)
                  
               else:
                  t_amt=i[3]*(500+2200)-i[4]
                  print("Total amount has to be paid is::",t_amt)
                  
         '''#AFTER GENERATING BILL OF CUSTOMER, SET STATUS OF RESERVED ROOM NUMBSER 'free'
            query="update bill set total_amt=no_days*(500+300)-advance, paid='done'".format(t_amt)
            cur.execute(query)
            query1="update rooms set status='{}' where room_no={}".format("free",room_number)
            query2="update customer set room_status='free' where r_no={}".format(reg_no)
            #DELETE CUSTMER'S INFORMATION FROM TABLE 'cust_book'
            query="delete from cust_book where reg_no={}".format(reg_no)
            cur.execute(query1)
            cur.execute(query2)
            cur.execute(query)
        
            #IF ENTERED REGISTRATION NUMBER IS NOT VALID
            else:                
                print("Hello")'''
             
         
         
            
            
   else:
       print("                    SORRY NO MORE DATA IN TABLE, ALL CUSTOMERS PAID THE BILLS          ")
      
    
    


#ADMIN PANEL
def admin():
   psswd=int(input("\n\n                              Enter the ADMIN password::    "))
   if psswd==123:
      yes=1
      while yes:
         print() 
         print("-----------------------WELCOME TO ADMIN PANEL----------------------------- ")
         print("|                      ----------------------                             |")
         print("|                            1. SHOW                                      |")
         print("|                            2. UPDATE                                    |")
         print("|                            3. DELETE                                    |")
         print(" ------------------------------------------------------------------------- ")
         print()
         choice=int(input("                       Enter your choice::    "))
         if choice==1:
            show()
         elif choice==2:
            update_info()
         elif choice==3:
            delete_info()
         else:
            yes=int(input("\n\nDo u want to continue SHOW/UPDATE/DELETE? 1/0::"))
      print()
      



#USER PANEL
def user():
   yes=1
   while yes:
      print()
      print(" -----------------------------------WELCOME TO USER PANEL------------------------------- ")
      print("|                                       1. BOOKING                                       |")
      print("|                                       2. BILL_GENERATE                                 |")
      print(" ---------------------------------------------------------------------------------------- ")
      choice=int(input("\nEnter your choice::"))
      if choice==1:
         booking_info()
      elif choice==2:
         bill_generate()
      else:
         print("------------------------------THANK YOU--------------------------------------------")
      yes=int(input("Do u want to continue BOOKING/BILL_GENERATE::"))
   


print("\n\n")
print("     -------------------------------------------------------------------------------------------")
print("    |                                1. ADMIN       2.  USER                                    |")
print("     -------------------------------------------------------------------------------------------")
print()
yes=1
while yes:
   choice=int(input("\n\n                                   Enter your choice::    "))
   if choice==1:
      admin()
   else:
      user()
   yes=int(input("Do u want to continue ADMIN/USER PANEL 1/0?::"))
   if yes==1:
      print("\n\n")
      print("     -------------------------------------------------------------------------------------------")
      print("    |                                1. ADMIN       2.  USER                                    |")
      print("     -------------------------------------------------------------------------------------------")
      print()
   else:
      print("-----------------------------------------------THANK YOU VISIT AGAIN-------------------------------------")
      
           

