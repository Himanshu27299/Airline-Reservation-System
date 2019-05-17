class Reservation:
     def __init__(self):
          self.name, self.age, self.sex, self.address, self.contact, self.email = None, None, None, None, None, None
          self.counter, self.seat, self.Ques, self.Q1, self.Flight_No = None, None, None, None,None
          self.file, self.temp = None, None

     def Navigation(self):
          print ()
          self.Ques = input("# Do you want to return to the Home Page (H) or Quit (Any Key):")
          if (self.Ques.upper() == "H"):
               print ()
               print ()
               self.Home()
          else:
               print ("\t\tTHANK YOU FOR USING FASTEST FAST AIRLINES.")
               quit()

     def Seating_Plan(self):             
          print ("           *SEATING PLAN (Showing Only Available Seats)*")
          print ()
          print ("( A )  ( B )  ( C )  ( D )  ( E )  ( F )  ( G )  ( H )  ( I )  ( J )")
          self.file.seek(258)
          self.b, self.counter = self.file.read(), 1
          self.c = self.b.split()
          self.temp = open("temp.txt","w")

          for i in range(len(self.b)):
               self.d = self.c[i]
               if (self.d == "(100)"):
                    print ("       ")
                    self.temp.write("(100)\n")
                    break
               elif (self.d[0] == "(" and self.d[4] == ")" and self.c[i+5] != "Name"):
                    if (int(self.d[1:4])%10 == 0):
                         print (self.d + " ")
                    else:
                         print (self.d + " ", end=" ")
               elif (self.d[0] == "(" and self.d[4] == ")" and self.c[i+5] == "Name"):
                    if (int(self.d[1:4])%10 == 0):
                         print ("      ")
                         self.temp.write(self.d)
                         self.temp.write("\n")
                         self.counter+=1
                    else:
                         print ("      ", end=" ")
                         self.temp.write(self.d)
                         self.temp.write("\n")
                         self.counter+=1
          self.temp.close()
          print ()
          print ("*Seats 1-60: Economy Class;   Seats 61-100: Business Class")
          print ("Seats remaining:", 100-self.counter,"/ 100")
          print ()
                  
     def Enquiry(self):                                                                              
          print ("Available Flights: (1) F2 238   (2) F2 427   (3) F2 532   (4) F2 624")
          self.Q1 = int(input("# Enter the option number of your desired flight: "))
          print ()
          print ()
          
          if (self.Q1 == 1):                                                                          # F2 238
               self.Flight_No = "238"
               self.file = open("F2 238.txt","r+")
               self.a = self.file.read(258)
               print (self.a)
               print ()
               
          elif (self.Q1 == 2):                                                                        # F2 427
               self.Flight_No = "427"
               self.file = open("F2 427.txt","r+")
               self.a = self.file.read(270)
               print (self.a)
               print ()
               
          elif (self.Q1 == 3):                                                                        # F2 532
               self.Flight_No = "532"
               self.file = open("F2 532.txt","r+")
               self.a = self.file.read(257)
               print (self.a)
               print ()
               
          elif (self.Q1 == 4):                                                                        # F2 624
               self.Flight_No = "624"
               self.file = open("F2 624.txt","r+")
               self.a = self.file.read(258)
               print (self.a)
               print ()
               
          else:
               print ("Invalid Input. Please Try Again Later.")
               print ("You are now been directed to the Home Page.")
               print ()
               self.Home()
     
     def Flight_Enquiry(self):                                                                       # MAIN (Part 1)
          self.Enquiry()
          self.Seating_Plan()
          self.Navigation()

     def Booking_Entry(self):
          import os
          self.outfile = open("Outfile.txt","w")
          self.file = open("F2 "+self.Flight_No+".txt","r")
                         
          self.name = input("# Enter your Full Name: ")                                            # Query Starts (Booking)
          self.age = int(input("# Enter your Age: "))
          self.sex = input("# Enter your Sex: ")
          self.address = input("# Enter your Address: ")
          self.contact = int(input("# Enter your Contact Number: "))
          self.email = input("# Enter your E-Mail ID: ")

          self.record = "Name           : "+self.name+"\nAge            : "+str(self.age)+\
                        "\nSex            : "+self.sex+"\nAddress        : "+self.address\
                        +"\nContact Number : "+str(self.contact)+"\nE-Mail ID      : "+self.email
          while True:
               self.line=self.file.readline()
               if (not self.line):
                    break
               else:
                    if ("("+str(self.seat)+")" in self.line):
                         self.outfile.write("(")
                         self.outfile.write(self.seat)
                         self.outfile.write(") Ticket Number  : F2-")
                         self.outfile.write(self.Flight_No)
                         self.outfile.write("-")
                         self.outfile.write(self.seat)
                         self.outfile.write("\n")
                         self.outfile.write(self.record)
                         self.outfile.write("\n")
                    else:
                         self.outfile.write(self.line)
          self.file.close()
          self.outfile.close()
          os.remove("F2 "+self.Flight_No+".txt")
          os.rename("Outfile.txt","F2 "+self.Flight_No+".txt")

     def Booking(self):                                                                              # MAIN (Part 2)
          self.Enquiry()
          self.Seating_Plan()
          self.no_of_tickets = int(input("# Enter the number of tickets you want to book: "))
          self.loop = self.no_of_tickets + 2
          
          if (self.no_of_tickets > 100-self.counter):
               print ("We don't have enough tickets available. Sorry!")
               print ("You are now been directed to the Home Page.")
               print ()
               self.Home()
          for i in range(1,self.loop-1):
               print ()
               print ("\t\tTICKET",i)

               self.seat = int(input("# Enter your desired seat number : "))
               self.temp = open("temp.txt","r")
               self.a1 = self.temp.read()
               self.b1 = self.a1.split()
                
               for i in range(len(self.b1)):
                    if (int(self.b1[i][1:4]) == self.seat):
                         print ("Entered Seat Number has been already booked.")
                         print ("You are now been directed to the Home Page.")
                         print ()
                         self.Home()
               if (self.seat < 10 and self.seat > 0):
                    self.seat = "00"+str(self.seat)
               elif (self.seat <100 and self.seat > 9):
                    self.seat = "0"+str(self.seat)
               elif (self.seat == 100):
                    pass
               else:
                    print ("Invalid Input.")
                    self.Home()
               self.Booking_Entry()
               print ()
               print ("Payment Received.")
               print ("Booking Confirmed.")
          self.Navigation()

     def Cancellation(self):                                                                         # MAIN (PART 3)
          self.Enquiry()
          self.confirm = input("Please confirm whether these are the correct flight details (Y/N):")
          if (self.confirm.upper() == "Y"):
               self.SeatNo_Check()
               import os
               self.outfile = open("Outfile.txt","w")
               self.file = open("F2 "+self.Flight_No+".txt","r")
                         
               while True:
                    self.line = self.file.readline()
                    if (not self.line):
                         break
                    else:
                         if ("("+str(self.seat)+")" in self.line):
                              self.outfile.write(self.line)
                              self.file.readline()
                              self.file.readline()
                              self.file.readline()
                              self.file.readline()
                              self.file.readline()
                              self.file.readline()
                         else:
                              self.outfile.write(self.line)
               self.file.close()
               self.outfile.close()
               os.remove("F2 "+self.Flight_No+".txt")
               os.rename("Outfile.txt","F2 "+self.Flight_No+".txt")
               self.temp.close()
               print ()
               self.Navigation()
                   
          elif (self.confirm.upper() == "N"):
               self.Navigation()
          else:
               print ("Invalid Input. Please Try Again Later.")
               print ("You are now been directed to the Home Page.")
               print ()
               self.Home()               

     def Print_temp(self):
          self.file.seek(268)
          self.b = self.file.read()
          self.c = self.b.split()
          self.temp = open("temp.txt","w")

          for i in range(len(self.b)):
               self.d = self.c[i]
               if (self.d == "(100)"):
                    self.temp.write("(100)\n")
                    break
               elif (self.d[0] == "(" and self.d[4] == ")" and self.c[i+5] == "Name"):
                    if (int(self.d[1:4])%10 == 0):
                         self.temp.write(self.d)
                         self.temp.write("\n")
                    else:
                         self.temp.write(self.d)
                         self.temp.write("\n")
          self.temp.close()
          

     def Enquiry_Print(self):                                                                              
          print ("Available Flights: (1) F2 238   (2) F2 427   (3) F2 532   (4) F2 624")
          self.Q1 = int(input("# Enter the option number of your flight: "))
          print ()
          print()
          
          if (self.Q1 == 1):                                                                           # F2 238
               self.Flight_No = "238"
               self.file = open("F2 238.txt","r+")
               self.a = self.file.read(152)
               print (self.a)
               self.Print_temp()
                    
          elif (self.Q1 == 2):                                                                         # F2 427
               self.Flight_No = "427"
               self.file = open("F2 427.txt","r+")
               self.a = self.file.read(154)
               print (self.a)
               self.Print_temp()
               
          elif (self.Q1 == 3):                                                                         # F2 532
               self.Flight_No = "532"
               self.file = open("F2 532.txt","r+")
               self.a = self.file.read(153)
               print (self.a)
               self.Print_temp()
               
          elif (self.Q1 == 4):                                                                         # F2 624
               self.Flight_No = "624"
               self.file = open("F2 624.txt","r+")
               self.a = self.file.read(159)
               print (self.a)
               self.Print_temp()
               
          else:
               print ("Invalid Input. Please Try Again Later.")
               print ("You are now been directed to the Home Page.")
               print ()
               self.Home()
     def SeatNo_Check(self):
          self.seat = int(input("# Enter your seat number : "))
          self.temp = open("temp.txt","r")
          self.a1 = self.temp.read()
          self.b1 = self.a1.split()
          self.counter = 0
                
          for i in range(len(self.b1)):
               if (int(self.b1[i][1:4]) == self.seat):
                    self.counter = 1
                    break
          if (self.counter != 1):
               print ("Entered Seat Number is unreserved.")
               print ("You are now been directed to the Home Page.")
               print ()
               self.Home()
          if (self.seat < 10 and self.seat > 0):
               self.seat = "00"+str(self.seat)
          elif (self.seat <100 and self.seat > 9):
               self.seat = "0"+str(self.seat)
          elif (self.seat == 100):
               pass
          else:
               print ("Invalid Input.")
               self.Home()
                              
     def Printing(self):                                                                               # MAIN (Part 4)
          self.Enquiry_Print()
          self.SeatNo_Check()
          self.file.seek(0,0)
          while True:
               self.line = self.file.readline()
               self.m = self.line[0:5]
               if (self.m[0] == "(" and int(self.m[1:4]) == int(self.seat) and self.m[4] == ")"):
                    print ()
                    print ("\t* YOUR TICKET DETAILS *")
                    print ()
                    print (self.line[6:])
                    print (self.file.readline())
                    print (self.file.readline())
                    print (self.file.readline())
                    print (self.file.readline())
                    print (self.file.readline())
                    print (self.file.readline())
                    break
               elif (not self.line):
                    break
          self.file.close()
          self.temp.close()
          print ()
          self.Navigation()
    
     def Home(self):
          print ("\t\t!! FASTEST FAST AIRLINES WELCOMES YOU !!")
          print ("(1) Flight Enquiry")
          print ("(2) Book Ticket")
          print ("(3) Cancel Ticket")
          print ("(4) Print Ticket")
          print ("(5) Exit")
          Q = input("# Enter the number of the option you would like to choose: ")
          if (Q == "1"):
               print ()
               self.Flight_Enquiry()
          elif (Q == "2"):
               print ()
               self.Booking()
          elif (Q == "3"):
               print ()
               self.Cancellation()
          elif (Q == "4"):
               print ()
               self.Printing()
          elif (Q == "5"):
               print ()
               print ("\t\tTHANK YOU FOR USING FASTEST FAST AIRLINES.")
               quit()
          else:
               print ()
               print ("Invalid Input. Please try again later.")
               print ()
               print ("\t\tTHANK YOU FOR USING FASTEST FAST AIRLINES.")
               quit()

R=Reservation()
R.Home()
