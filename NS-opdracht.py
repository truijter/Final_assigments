def inlezen_beginstation(stations):
    zin_askBEGstation = "****************************** \n Wat is je beginstation? "
    begin_station = ''

    while begin_station not in stations:
        begin_station = input(zin_askBEGstation)
        begin_station = begin_station.capitalize()
        if begin_station == 'Maastricht':
            print('dit is het allerlaaste station, dus niet mogelijk probeer het opnieuw')
            begin_station = input(zin_askBEGstation)
            begin_station = begin_station.capitalize()
    return begin_station


def inlezen_eindstation(stations,begin_station):
    zin_askEINstation = "Wat is je eindstation? "
    zin_fout = 'probeer een anders station, deze trein rijdt niet naar '
    eind_station = ''

    while eind_station not in stations:
        eind_station = input(zin_askEINstation)
        eind_station = eind_station.capitalize()
    index_beginstation = (stations.index(beginstation) + 1)
    index_eindstation = (stations.index(eind_station) + 1)

    while index_eindstation < index_beginstation:
        print(zin_fout + eind_station)
        eind_station = input(zin_askEINstation)
        eind_station = eind_station.capitalize()
        index_beginstation = (stations.index(beginstation) + 1)
        index_eindstation = (stations.index(eind_station) + 1)
        if eind_station == 'q':
            inlezen_beginstation()


    return eind_station


def  omroepen_reis(stations, beginstation, eind_station):
    index_beginstation = (stations.index(beginstation) + 1)
    index_eindstation = (stations.index(eind_station) + 1)
    afstand = index_eindstation - index_beginstation
    kosten_rit = 5  #in euro

    prijs = afstand * kosten_rit

    station_richting = stations[index_beginstation]
    zin_beginstation = 'Het beginstation ' + beginstation + ' is het ' + str(index_beginstation) + 'e station in het traject.'
    zin_eindstation = 'Het eindstation ' + eind_station + ' is het ' + str(index_eindstation) + 'e station in het traject.'
    zin_afstand = 'De afstand bedraagt ' + str(afstand) + ' station(s). '
    zin_prijs = 'De prijs van het kaartje is ' + str(prijs) + ' euro. \n'
    zin_instappen = 'Jij stapt in de trein in:' + beginstation + ' - ' + station_richting
    zin_uitstappen = 'Jij stapt uit in: ' + eind_station

    print(zin_beginstation)
    print(zin_eindstation)
    print(zin_afstand)
    print(zin_prijs)
    print(zin_instappen)
    print(zin_uitstappen)


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

beginstation = inlezen_beginstation(stations)
eind_station = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation , eind_station)
