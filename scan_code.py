codes = [1111,2222,3333,4444,5555,6666,7777,8888,9999]
produkt_namn = ['Snicker  ','Nutella  ','Water 6p','milk      ','mini-pump','Ice cream','Bread 700g','Cornflake','premium Lax']
prices = [5,35,49,12,109,39,15,19,89]
köp_listan = []
Summa = 0
while True:
    produkt = input('Skriv produkt nummer: ')
    try:
        produkt = int(produkt)
    except:
        print('ogiltig input')

    if produkt == 0000:
        for c in range(len(köp_listan)):
            Summa += köp_listan[c][1]
        break



    for b in range(0,9):
        if produkt == codes[b]:
            köp_listan.append([produkt_namn[b],prices[b]])
            break
        elif b == 8:
            print('item not found')

    for a in range(len(köp_listan)):
        
        print(f'{köp_listan[a][0]}\t{köp_listan[a][1]} Kr')


print('+--------------------------------+')
print(f'|Välkommen till Best deals\t |')
print('|\t\t\t\t |\n|\t\t\t\t |')
for a in range(len(köp_listan)):
        
    print(f'|{köp_listan[a][0]}\t{köp_listan[a][1]} Kr\t\t |')
print(f'|Totals:\t{Summa} Kr\t\t |')

print('+--------------------------------+')