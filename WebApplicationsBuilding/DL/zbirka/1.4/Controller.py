from Model import Proizvod
import View
def showAll():
   b = Proizvod(21231,'321312',321)   
   proizvodi_u_bazi = b.getAll()
   #calls view
   return View.ukupanRacun(proizvodi_u_bazi)
   #return View.showAllView(proizvodi_u_bazi)
   

def start():
    View.startView()
    showAll()
    View.endView()
if __name__ == "__main__":
   #running controller function
   start()
   
def main():
    print('hajde')
