#Schrijf functie standaardprijs(afstandKM).
#  Iedere treinrit kost 80 cent per kilometer, maar als de rit langer is dan 50 kilometer betaal je een vast bedrag
#  van €15,- plus 60 cent per kilometer. Ga bij invoer van negatieve afstanden uit van een afstand van 0 kilometer (prijs is dan dus 0 Euro).

def standaardprijs(afstandKM):
    KMgrens= 50 #inKM
    varkostenlangeritPercentage = 0.60
    VASTkostenlangerit = 15
    VARkortrit = 0.80

    if afstandKM >= KMgrens :
        Prijs = (afstandKM * varkostenlangeritPercentage) + VASTkostenlangerit
    else :
        Prijs = (VARkortrit * afstandKM)
    return Prijs

standaardprijs(25)

#Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met 30% korting. In het weekend reist deze
# groep met 35% korting. De overige leeftijdsgroepen reizen betalen de gewone prijs, behalve in het weekend, dan reist deze leeftijdsgroep met 40% korting.

def ritprijs(leeftijd, inhetweekend, afstandKM):
    Varprijs = standaardprijs(afstandKM)
    weekendkortinggroepOUD = 0.65           # korting = berekend door 1 - korting  te doen
    weekendkortingGroepNormaal = 0.60
    Weekdagengroep = 0.70
    leeftijdmin = 12
    leeftijdmax = 65
    leeftijdskorting = leeftijd < leeftijdmin or leeftijd > leeftijdmax
    
    if inhetweekend:

        if leeftijdskorting :
            VastPrijs = (Varprijs * weekendkortinggroepOUD)
        else:
            VastPrijs = (Varprijs * weekendkortingGroepNormaal)

    elif not inhetweekend :
        if leeftijdskorting :
            VastPrijs = (Varprijs * Weekdagengroep)
        else :
            VastPrijs = Varprijs

    return VastPrijs

print(ritprijs(11,True,150))
