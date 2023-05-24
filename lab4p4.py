from datetime import date

room = []
solv = []
risk = []
time = []
while True:
#This is the main menu of the program
    imp = int(input("1) add room    2) show room \n 3) Exit \n"))
    #This loop will ask the user to enter data after adding room
    if imp == 1: #add room
        room.append(input("What is the room: ")) #simple string asking for the room name
        print("What is the type of Hazard")
        i = 0
        while i == 0:
            ans = int(input("1) Water Leakage   2)Fire Hazard \n3)Electricity outage    4)Physical \n5)Others \n"))
            if ans == 1:
                solv.append("Water Leakage")
                i += 1
            elif ans == 2:
                solv.append("Fire Hazard")
                i += 1
            elif ans == 3:
                solv.append("Electricity Outage")
                i += 1
            elif ans == 4:
                solv.append("Physical")
                i += 1
            elif ans == 5:
                solv.append(input("Please enter the hazard \n"))
                i += 1
        print(" What is the risk of Hazard")
        i = 0

        while i == 0:
            ans = int(input("1) High risk     2) Medium risk      3) Low Risk \n"))
            if ans == 1:
                risk.append("High")
                i += 1
            elif ans == 2:
                risk.append("Medium")
                i += 1
            elif ans == 3:
                risk.append("Low")
                i += 1
            else:
                print("Please enter a real option")
        time.append(date.today())
    #This loop prints data added after adding rooms       
    elif imp == 2: #show room
        i = 0
        for num in room:
            print("Record ",i+1)
            print("Room name: ",room[i])
            print("Hazard type: ",solv[i])
            print("Risk level: ",risk[i])
            print("Time recorded: ",time[i])
            print("_____________")
            i += 1
    #This ends the toolkit and closes the program
    elif imp == 3: #Exit
        print("Thank you for using this mini toolkit")
        break