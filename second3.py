import replit
# funktion med nested for och med skippa delar med ifloop
def hotell():
  replit.clear()
  Hotelnummer = ["1. Första hotellet i ","2. Andra hotellet i ", "3. Första hotellet i ", "4. Fjärde hotellet i ", "5. Femte hotellet i " ]
  land = " Italien\t\t"," Tyskland\t\t", " Austria\t\t"," Turkiet\t\t", " Frankrike\t\t"
  for x in  Hotelnummer:
    for y in land:
      if y == " Tyskland\t\t":
        continue

      elif y == " Austria\t\t":
        continue

      elif y == " Turkiet\t\t":
        continue

      elif y == " Frankrike\t\t":
        continue
      
      print (x, y, "\n") 
  input()