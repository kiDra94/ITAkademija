import shelve
 
with shelve.open('ShelveExample') as mutd_jerseys:
    mutd_jerseys['1'] = 'David de Gea'
    mutd_jerseys['2'] = 'Victor Lindelof'
    mutd_jerseys['3'] = 'Eric Bailly'
    mutd_jerseys['4'] = 'Phil Jones'
    mutd_jerseys['5'] = 'Harry Maguire'
    mutd_jerseys['6'] = 'Paul Pogba'
    mutd_jerseys['7'] = 'Alexis Sanchez'
    mutd_jerseys['8'] = 'Juan Mata'
    
    for key in mutd_jerseys:
        print(key,' : ',mutd_jerseys[key])

with shelve.open('ShelveExample') as mutd_jerseys:
    mutd_jerseys['7'] = 'David Beckham'
