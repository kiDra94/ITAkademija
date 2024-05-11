from Model import Osoba
import View
def showAll():

   b = Osoba(12321312,'fdfd',2020)   
   persons_in_db = b.getAll()
   #calls view
   return View.showAllView(persons_in_db)
def start():
    View.startView()
    showAll()
    View.endView()
if __name__ == "__main__":
   #running controller function
   start()
   

def main():
    print('ajde')
