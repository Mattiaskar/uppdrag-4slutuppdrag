import replit
from getkey import getkey, keys
import second1

# Andra menyn 
def land():
        replit.clear()
        print("\n\tVilket land vill du resa? \n")
        print("Välja land för att se buss och pris\n")
        landLista =["1. Italien\t\t","2. Tyskland\t\t", "3. Austria\t\t","4. Turkiet\t\t", "5. Frankrike\t\t", "6. Tillbaka till menyn\t\t"]
        landSelected = 0
  
        while (True):
          replit.clear()
          print("\x1b[?25l")
        
          if landSelected == 0:
            print(landLista [0] + "<---")
            print(landLista[1])
            print(landLista[2])
            print(landLista[3])
            print(landLista[4])
            print(landLista[5] )
            
        
          elif landSelected == 1:
            print(landLista[0] )
            print(landLista[1] + "<---")
            print(landLista[2])
            print(landLista[3])
            print(landLista[4])
            print(landLista[5] )
            
        
          elif landSelected == 2:
            print(landLista[0] )
            print(landLista[1])
            print(landLista[2] + "<---")
            print(landLista[3])
            print(landLista[4])
            print(landLista[5] )
            
        
          elif landSelected == 3:
            print(landLista[0])
            print(landLista[1])
            print(landLista[2])
            print(landLista[3] + "<---")
            print(landLista[4])
            print(landLista[5] )
            
        
          elif landSelected == 4:
            print(landLista[0])
            print(landLista[1])
            print(landLista[2])
            print(landLista[3])
            print(landLista[4] + "<---")
            print(landLista[5] )
            

          elif landSelected == 5:
            print(landLista[0])
            print(landLista[1])
            print(landLista[2])
            print(landLista[3])
            print(landLista[4] )
            print(landLista[5] + "<---")
          keyPressed = getkey()
        
          if keyPressed == keys.DOWN and landSelected + 1 != len(landLista):
             landSelected += 1
          elif keyPressed == keys.UP and not (landSelected == 0):
                 landSelected -= 1
          elif keyPressed == keys.ENTER:
           
            if landSelected == 0:
              second1.bussLista()
            
            elif landSelected == 1:
              second1.bussLista()
              
            elif landSelected == 2:
                second1.bussLista()
              
            elif landSelected == 3:
                 second1.bussLista()
            
            elif landSelected == 4:
              second1.bussLista()
            elif landSelected ==5:
              # Tillbaka till första sidan
              replit.clear()
              import main
            input("Trycka Enter for att tillbaka till första sidan ..")