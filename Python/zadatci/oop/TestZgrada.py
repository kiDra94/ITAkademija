#isti cas kao opp5 i opp6
#povezan sa Zgradom
import Zgrada as z

# Kreira tri vlasnika
raja = z.Vlasnik('Raja', 'Patakovic', '123456')
gaja = z.Vlasnik('Gaja', 'Patakovic', '123457')
vlada = z.Vlasnik('Vladimir', 'Putinic', '123458')
#print(raja.ime_sadrzi('atak'))

# Kreira cetiri stana u zgradi P+1
s0_1 = z.Stan(50, 0) # sprat 0 je prizemlje
s0_2 = z.Stan(100, 0)
s1_1 = z.Stan(75, 1)
s1_2 = z.Stan(75, 1)
zgrada = z.Zgrada('Radnicka 4', [s0_1, s0_2, s1_1, s1_2])

# Posle kupovine stanova

s0_1.promeni_vlasnika(raja)
s0_2.promeni_vlasnika(gaja)
s1_1.promeni_vlasnika(vlada)
s1_2.promeni_vlasnika(raja) # opet Raja

# Posle velikog interesovanja ide nadgradnja
s2_1 = z.Stan(150, 2)
zgrada.dodaj_stan(s2_1)
s2_1.promeni_vlasnika(raja) # opet Raja

# Ispis podataka o zgradi
print(zgrada)

# Vlasnici u zgradi koji u imenu imaju 'aja'
print('Vlasnici sa "aja" u imenu:\n')
for stanovi in zgrada.stanovi_vlasnika('aja').values():
    total = 0
    for stan in stanovi:
        total += stan.povrsina()
    print(stan.vlasnik())
    print('Ukupno', total, 'm2\n')