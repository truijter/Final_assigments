    #fucties
def toon_aantal_kluizen_vrij():
    #Variabelen
    zin_beschikbaar = '******* \n Deze kuizen zijn nog beschikbaar: \n'
    kluizen_lijst = [1,2,3,4,5,6,7,8,9,10,11,12]
    kluizen_READ = readkluisfile()

    #CODE

    gebruiktekluizenlijst = [int(nummer.split(';')[0]) for nummer in kluizen_READ.split()[0:]]
    for kluis in gebruiktekluizenlijst :

        if kluis in gebruiktekluizenlijst:
            kluizen_lijst.remove(kluis)

    print(zin_beschikbaar + str(kluizen_lijst))
    return kluizen_lijst


def nieuwe_kluis():
    #Variabelen
    kluizen_vrij = toon_aantal_kluizen_vrij()
    zin_nieuwekluis = 'Welke kluis wilt u gebruiken? \n'
    zin_code = 'Voer een code in \n'
    kluis_file = open('kluizen.txt', 'a')
    aanvraag_kluis = 0
    # CODE

    while int(aanvraag_kluis) not in kluizen_vrij:
        aanvraag_kluis = input(zin_nieuwekluis)
    code = input(zin_code)
    kluis_file.write(aanvraag_kluis +';' + code +'\n' )

    kluis_file.close()

def readkluisfile():
    kluizen_OPEN = open('kluizen.txt', 'r')
    kluizen_READ = kluizen_OPEN.read()
    kluizen_OPEN.close()
    return kluizen_READ


def kluis_openen():
    #Variabelen
    kluizen_READ = readkluisfile()
    zin_kluis_open = 'Voer uw kluisnummer in'
    zin_kuis_open_pass = 'Voer uw code in'

    #CODE
    nummer = input(zin_kluis_open)
    code = input(zin_kuis_open_pass)
    combinatie = str(nummer) +";"+ str(code)

    if combinatie in kluizen_READ:
        print('kluis is open')
    else:
        print('Onjuiste code probeer het opnieuw')


def kluis_teruggeven():
    #Variabelen
    kluizen_READ = readkluisfile()
    zin_kluis_open = 'Voer uw kluisnummer in'
    zin_kuis_open_pass = 'Voer uw code in'
    zin_teruggeef = 'uw Kluis is terug gegeven'

    #CODE
    nummer = input(zin_kluis_open)
    code = input(zin_kuis_open_pass)
    combinatie = str(nummer) +";"+ str(code)

    kluizen_OPEN = open("kluizen.txt", "w")
    for line in kluizen_READ:
        if line != combinatie + "\n":
            kluizen_OPEN.write(line)
            print(zin_teruggeef)

    kluizen_OPEN.close()


def Begin():
    #Variabelen
    Opties = [1, 2, 3, 4]
    optie1 = 1
    optie2 = 2
    optie3 = 3
    optie4 = 4
    zin_menu = '************************************** \n \t MENU \n************************************** \n1: Ik wil weten hoeveel kluizen nog vrij zijn' + '\n' + '2: Ik wil een nieuwe kluis' + '\n' + '3: Ik wil even iets uit mijn kluis halen' + '\n' + '4: Ik geef mijn kluis terug' + '\n' + 'Voer een nummer in :  '
    Menu = 0
    #CODE

    while Menu not in Opties:
        print ('Voer een geldig nummer in')
        Menu = int(input(zin_menu))

    else:
            if Menu == optie1:
                toon_aantal_kluizen_vrij()
            elif Menu == optie2:
                nieuwe_kluis()
            elif Menu == optie3:
                kluis_openen()
            elif Menu == optie4:
                kluis_teruggeven()



Begin()
