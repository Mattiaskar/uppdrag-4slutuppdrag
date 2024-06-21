#importera andra filer och replit
import replit
from getkey import getkey, keys
import second
import second2
import second3


print("Med EuropTour till alla European städer\n")
input("\tTryck Enter för att gå till menyn")

# Menu 
menuOptions = ["1. Buss och land\t\t", "2. Bagagevikt\t\t", "3. Forsäkring\t\t", "4. Hotell\t\t", "5. Avsluta\t\t"]
menuSelected = 0

while (True):
  replit.clear()
  print("\x1b[?25l")
  
  if menuSelected == 0:
    print(menuOptions[0] + "<---")
    print(menuOptions[1])
    print(menuOptions[2])
    print(menuOptions[3])
    print(menuOptions[4])

  elif menuSelected == 1:
    print(menuOptions[0] )
    print(menuOptions[1] + "<---")
    print(menuOptions[2])
    print(menuOptions[3])
    print(menuOptions[4])

  elif menuSelected == 2:
    print(menuOptions[0] )
    print(menuOptions[1])
    print(menuOptions[2] + "<---")
    print(menuOptions[3])
    print(menuOptions[4])

  elif menuSelected == 3:
    print(menuOptions[0])
    print(menuOptions[1])
    print(menuOptions[2])
    print(menuOptions[3] + "<---")
    print(menuOptions[4])

  elif menuSelected == 4:
    print(menuOptions[0])
    print(menuOptions[1])
    print(menuOptions[2])
    print(menuOptions[3])
    print(menuOptions[4] + "<---")
  keyPressed = getkey()

  if keyPressed == keys.DOWN and menuSelected + 1 != len(menuOptions):
     menuSelected += 1
  elif keyPressed == keys.UP and not (menuSelected == 0):
         menuSelected -= 1
  elif keyPressed == keys.ENTER:
    
    if menuSelected == 0:
      second.land() 
      
    elif menuSelected == 1:
      #returvärde som räknar antal vikt
      replit.clear()
      def bagage(vikt):
        antal = vikt * y
        return antal
      y = int (input("Hur manga bagage har du med dig? "))
      x = bagage(float(input("Hur mycket har vikt värje bagage?  ")))
        
      replit.clear()
      print ("Du har {0} bagage som har sammanlagt {1} vikt (tillåt last 40)".format(y, x))
      input()  
         
    elif menuSelected == 2:
      second2.forsakring()
  
      
    elif menuSelected == 3:
       second3.hotell()
    
    elif menuSelected == 4:
      #exit
      replit.clear()
      print("\n\tAvsluta programmet?\n")
      input("Trycka Enter for att avsluta ..")
      print("\x1b[?25h")
      replit.clear()
      exit("Avslut")
      break