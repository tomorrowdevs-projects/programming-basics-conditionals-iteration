days = int(input("Inserisci i giorni di durata della vacanza: "))
totalbudget = int(input("Inserisci la quantità di budget, in euro, disponibile per la vacanza: "))

totdays = days
dailylodging = []
dailytransportation = []
dailymeals = []
totalprice = 0

for n in range (days):
    while days > 0:
        print("Per favore inserite le spese giornaliere per le seguenti categorie")
        dailylodging += [float(input("Affitto: "))]
        dailytransportation += [float(input("Trasporti: "))]
        dailymeals += [float(input("Cibo: "))]
        days -= 1

totlodging = sum(dailylodging)
tottransportation = sum(dailytransportation)
totmeals = sum(dailymeals)

for n in range (totdays):
    totalprice += dailylodging[n]
    totalprice += dailytransportation[n]
    totalprice += dailymeals[n]
    
while True:
    correct = input("Desideri correggere i valori immessi? Per favore rispondere con si o no: ")
    if correct == "si":
        day_to_correct = int(input(f"Inserisci il numero del giorno da correggere (1-{days}): ")) - 1
        dailylodging[day_to_correct] = float(input("Affitto: "))
        dailytransportation[day_to_correct] = float(input("Trasporti: "))
        dailymeals[day_to_correct] = float(input("Cibo: "))

        totlodging = sum(dailylodging)
        tottransportation = sum(dailytransportation)
        totmeals = sum(dailymeals)
        totalprice = totlodging + tottransportation + totmeals

        if totalprice > totalbudget:
            print("ATTENZIONE: il budget e stato superato")
            break
        else:
            print(f"Il prezzo totale dell'affito è: {totlodging} €\n Il prezzo totale dei trasporti è: {tottransportation} €\n Il prezzo totale del cibo è di: {totmeals} €\n Il prezzo totale del viaggio è quindi di: {totalprice}")
            break

    elif correct == "no":
        if totalprice > totalbudget:
            print("ATTENZIONE: il budget e stato superato")
            break
        else:
            print(f"Il prezzo totale dell'affito è: {totlodging} €\n Il prezzo totale dei trasporti è: {tottransportation} €\n Il prezzo totale del cibo è di: {totmeals} €\n Il prezzo totale del viaggio è quindi di: {totalprice}")
            break