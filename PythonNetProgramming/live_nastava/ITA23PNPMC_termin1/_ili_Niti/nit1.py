#Niti su laki procesi; manje meomirje jednostavniji za implementaciju
#hocemo da malo radi jedan proces malo drugi (kao multitasking); do sad smo radili sa jednom Nit (radili smo linearno!!!)
import threading #potreban da se pravi Nit

def worker(num):
    """thread worker function"""
    print('Worker: %s' % num) #%s -> ocekuje tip string!
    return

threads = []
for i in range(25):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start() # pokrece nit!

print("--------") # nekad uskoci kad hoce tj Nit ne ide po odredjenom redoslijedu

