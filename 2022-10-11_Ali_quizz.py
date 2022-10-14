# kontroll av svar
def kontrollera_gisning(rätt):
    global poäng 
    if rätt:
        print('Rätt svar')
        poäng += 2
        return True
    else:
        print('Fel')
        poäng -= 1
        return False

#frågar frågorna            
def fråga(fråga,svar):                                                                                                                                                                                                                                                                                                      
    for a in range(3):
        print('\n')
        print(fråga)
        return input('skriv a,b,c,d: ').lower() == svar

#variabler n för index för lista
poäng = 0
n = 0

#lista med frågor
frågor_biblotek = ['Vad  är dem första 4 deciamaler av pi.\na)3.1456\nb)3.1415\nc)3.1581\nd)3.1412\nIngen avrundning!'
,'Vad betyder .islower()\na)gör att alla bokstäver till små bokstäver\nb)existerar inte\nc)är en funktion som talar om det är alla bokstäver är små eller inte\nd)talar om ett sträng innehåller ett små bokstav'
,'Vem är störst Den afrikanska elefanten eller den indiska elefanten\na)Afrikanska elefanten\nb)Indiska elefanten\nc)Dem är lika stora\nd)Elefanter finns inte'
,'Den amerkaniska kontinenten och Europa rör sig ifrån varandra. Hur mycket rör sig dem per år\na)2.5cm\nb)2.5dm\nc)2.5m\nd)Den rör sig inte'
,'I vilken månad föddes Magdelena Andersson\na)April,\nb)Septemper\nc)Juni\nd)Januari'
,'Vilken månad motsvarar ramadan i vår kalender\na)Juni\nb)Augusti\nc)Septemper\nd)Det finns ingen månad'
,'Vilket år blev Gustav Vasa kung\na)1613\nb)1523\nc)1590\nd)1499'                                                                                                                                                                                                                                                                                            
]


#lista med svaren
svar_biblotek = ['b','c','b','a','d','d','b']

#en loop med funktionerna 
for b in range(len(svar_biblotek)):
    #ger två försök
    for a in range(2):
        #om rätt går ur loopen
        if kontrollera_gisning(fråga(frågor_biblotek[n],svar_biblotek[n])):
            break
        else:
            if a == 1:
                #ifall fel två gånger adderar två poäng så att man får inte negativa poäng
                poäng += 2
            continue

    #nästa fråga och svar i listan
    n += 1

#utskrift av poäng
print(f'Grattis! Du fick {poäng} av 14!')


