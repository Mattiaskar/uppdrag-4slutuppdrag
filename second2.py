import replit
# funktuion med  fel hantering och typomvandling
def forsakring():
  replit.clear()
  print("Du ska registera dig för att bli försäkrad!")
  name = input("Skriv in ditt namn:  ")
  while (True):
    try:
      age = int (input("skriv in din ålder: "))
      break
    except:
      print("Du ska skriva din alder!\n")
    
  place1 = input("Var bor du? ")
  place2 = input("Vart ska du resa? ")

  print("Du heter "+ name + " och har "+ str(age) +" år gammal "+ "och bor i "+ place1+" och vill resa till "+ place2)
  input()