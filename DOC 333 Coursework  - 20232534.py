#initialize
Starting_Country=0
Destination_Country=0
your_choice=0
exiting=0
x=3 #X variable is used for the repitition of the while loop.

#Repetition

while (x>0):
    print("                                     FlightRoutes Company")
    print("                                              Main Menu")
    print("")
    print("1. Display All possible airline routes between two given countries with duration.")
    print("2. Display least time airline route between two given countries.")
    print("3. Exit")

#Input
    your_choice=int(input("                                                                                                 Your Choice: " ))
    print("")
    print("")

#Process   
    if(your_choice==1):
        print("                                              FlightRoutes Company")
        print("          All possible airline routes between two given countries with duration")
        print("")
        print("Only Available Flight routes for the below mentioned countries : ")
        print("")
        print("SL")
        print("UK")
        print("USA")
        print("Japan")
        print("Singapore")
        print("Australia")
        print("")
        Starting_Country=str(input("Enter the Starting Country: "))
        Destination_Country=str(input("Enter the Destination Country: "))
        print("")
        print("")

        if(Starting_Country=="SL" and Destination_Country=="UK"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :United Kingdom(UK)")
            print("")
            print("Route 1: Sri Lanka->United Kingdom              Expected Duration: 11.45hrs")
        elif(Starting_Country=="SL" and Destination_Country=="USA"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :United States of America(USA)")
            print("")
            print("Route 1: Sri Lanka->United Kingdom->United States of America            Expected Duration: 19.45hrs")
            print("Route 2: Sri Lanka->Japan->United States of America                     Expected Duration: 24hrs")
            print("Route 3: Sri Lanka->Singapore->Japan->United States of America          Expected Duration: 24hrs")
        elif(Starting_Country=="SL" and Destination_Country=="Japan"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :Japan")
            print("")
            print("Route 1: Sri Lanka->Japan                            Expected Duration: 8hrs")
            print("Route 2: Sri Lanka->Singapore->Japan     Expected Duration: 8hrs")
        elif(Starting_Country=="SL" and Destination_Country=="Singapore"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :Singapore")
            print("")
            print("Route 1: Sri Lanka->Singapore            Expected Duration: 4hrs")
        elif(Starting_Country=="SL" and Destination_Country=="Australia"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :Australia")
            print("")
            print("Route 1: Sri Lanka->Japan->Australia                           Expected Duration: 18hrs")
            print("Route 2: Sri Lanka->Singapore->Japan->Australia                Expected Duration: 18hrs")
            print("Route 3: Sri Lanka->Singapore->Australia                       Expected Duration: 11.25hrs")
            print("Route 4: Sri Lanka->Australia                                  Expected Duration: 9.25hrs")
        elif(Starting_Country=="UK" and Destination_Country=="USA"):
            print("Starting Country :United Kingdom(UK)             Destination Country :United States of America(USA)")
            print("")
            print("Route 1: United Kingdom->United States of America         Expected Duration: 8hrs")
        elif(Starting_Country=="Japan" and Destination_Country=="USA"):
            print("Starting Country :Japan                          Destination Country :United States of America(USA)")
            print("")
            print("Route 1: Japan->United States of America          Expected Duration: 16hrs")
        elif(Starting_Country=="Japan" and Destination_Country=="Australia"):
            print("Starting Country :Japan                          Destination Country :Australia")
            print("")
            print("Route 1: Japan->Australia                  Expected Duration: 10hrs")
        elif(Starting_Country=="Singapore" and Destination_Country=="USA"):
            print("Starting Country :Singapore                      Destination Country :United States of America(USA)")
            print("")
            print("Route 1: Singapore->Japan->United States of America          Expected Duration: 20hrs")
        elif(Starting_Country=="Singapore" and Destination_Country=="Japan"):
            print("Starting Country :Singapore                      Destination Country :Japan")
            print("")
            print("Route 1: Singapore->Japan              Expected Duration: 4hrs")
        elif(Starting_Country=="Singapore" and Destination_Country=="Australia"):
            print("Starting Country :Singapore                      Destination Country :Australia")
            print("")
            print("Route 1: Singapore->Australia                           Expected Duration: 7.25hrs")
            print("Route 2: Singapore->Japan->Australia                    Expected Duration: 14hrs")
        else:
            print("Error, Flights are available only for above mentioned countries. Thank You!")
        print()

    if(your_choice==2):
        print("                                             FlightRoutes Company")
        print("                 Least duration airline route between two given countries.")
        print("")
        print("Only Available Flights routes for the below mentioned countries:")
        print("SL")
        print("UK")
        print("USA")
        print("Japan")
        print("Singapore")
        print("Australia")
        print("")
        Starting_Country=str(input("Enter the Starting Country:" ))
        Destination_Country=str(input("Enter the Destination Country: "))
        print("")

        if(Starting_Country=="SL" and Destination_Country=="UK"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :United Kingdom(UK)")
            print("")
            print("Route 1: Sri Lanka->United Kindom          Expected Duration: 11.45hrs")
        elif(Starting_Country=="SL" and Destination_Country=="USA"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :United States of America(USA)")
            print("")
            print("Route 1: Sri Lanka->United Kindom->United States of America        Expected Duration: 19.45hrs")
        elif(Starting_Country=="SL" and Destination_Country=="Japan"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :Japan")
            print("")
            print("Route 1: Sri Lanka->Japan          Expected Duration: 8hrs")
        elif(Starting_Country=="SL" and Destination_Country=="Singapore"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :Singapore")
            print("")
            print("Route 1: Sri Lanka->Singapore          Expected Duration: 4hrs")
        elif(Starting_Country=="SL" and Destination_Country=="Australia"):
            print("Starting Country :Sri Lanka(SL)                  Destination Country :Australia")
            print("")
            print("Route 1: Sri Lanka->Australia          Expected Duration: 9.25hrs")
        elif(Starting_Country=="UK" and Destination_Country=="USA"):
            print("Starting Country :United Kingdom(UK)             Destination Country :United States of America(USA)")
            print("")
            print("Route 1: United Kindom->United States of America          Expected Duration: 8hrs")
        elif(Starting_Country=="Japan" and Destination_Country=="USA"):
            print("Starting Country :Japan                          Destination Country :United States of America(USA)")
            print("")
            print("Route 1: Japan->United States of America          Expected Duration: 16hrs")
        elif(Starting_Country=="Singapore" and Destination_Country=="USA"):
            print("Starting Country :Singapore                      Destination Country :United States of America(USA)")
            print("")
            print("Route 1: Singapore->Japan->United States of America          Expected Duration: 20hrs")
        elif(Starting_Country=="Singapore" and Destination_Country=="Japan"):
            print("Starting Country :Singapore                      Destination Country :Japan")
            print("")
            print("Route 1: Singapore->Japan          Expected Duration: 4hrs")
        elif(Starting_Country=="Japan" and Destination_Country=="Australia"):
            print("Starting Country :Japan                          Destination Country :Australia")
            print("")
            print("Route 1: Japan->Australia          Expected Duration: 10hrs")
        elif(Starting_Country=="Singapore" and Destination_Country=="Australia"):
            print("Starting Country :Singapore                      Destination Country :Australia")
            print("")
            print("Route 1: Singapore->Australia          Expected Duration: 7.25hrs")
        else:
            print("Error, Flights are not available. Thank You!")

        print("")
        exiting=str(input("Do you want to Exit?  (Yes/No):"))
        print("")
        
        if(exiting=="Yes"):
            exit()
        elif(exiting=="No"):
            print("")
        else:
            print("Error, Please type Yes/No.")
            print("")
            break       

    if (your_choice==3):
        exit()

    elif(your_choice>3):
        print("Error, Please select Your Choice as 1, 2 or 3")
        break
#End
