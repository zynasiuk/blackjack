import random
nummers = [2,3,4,5,6,7,8,9,10, "Boer", "Koningin", "Koning", "Aas"]
kleur = ["klvr", "rt", "hrt", "schp"]
combinations=[]
teller_gebruiker = 0
teller_computer = 0
score = {'Gebruiker': 0, 'Dealer': 0 }

def blackjack():
#Fase 1:
    for y in kleur:
        for z in nummers:
            x = (z, y)
            combinations.append(x)
    #Fase 2:
    random.shuffle(combinations)
    #print("First shuffle: ", combinations)
    random.shuffle(combinations)
    #print("Second shuffle: ", combinations)
    random.shuffle(combinations)
    #print("Third shuffle: ", combinations)

    game = {'Gebruiker': [], 'Dealer': [] }

    game['Dealer'].append(combinations[0])
    game['Gebruiker'].append(combinations[1])
    game['Gebruiker'].append(combinations[2])
    game['Dealer'].append(combinations[3])

    del combinations[0:4]

    print("You: " + str(game['Gebruiker']))
    print("Dealer: " + str(game['Dealer'][-1]))

    #Fase 3:

    def punten(wie, teller):
        for i in wie:
            if (i[0] == 'Boer' or i[0] == 'Koningin' or i[0] == 'Koning') or (i[0] == 'Aas' and teller > 11):
                teller += 10
            elif (i[0] == 'Aas' and teller < 11):
                teller +=1
            else:
                teller += i[0]
        return teller

    punten_dealer = punten(game['Dealer'], teller_computer)
    punten_user = punten(game['Gebruiker'], teller_gebruiker)
    print(" YOUR score: "+ str(punten_user))
#"Dealer: " +str(punten_dealer) +
    # fase 4

    while punten_user <= 21 and punten_dealer <= 21:
        hit_of_stand = (input("Do you want another card? Print \"Y\" for more: ")).upper()
        print(hit_of_stand)
        if (hit_of_stand == "Y"):
            game['Gebruiker'].append(combinations[0])
            print(combinations[0])
            del combinations[0]
            punten_user = punten(game['Gebruiker'], teller_gebruiker)
            print("punten user "+str(punten_user))
            if (punten_dealer <= punten_user):
                game['Dealer'].append(combinations[0])
                print(combinations[0])
                del combinations[0]
                punten_dealer = punten(game['Dealer'], teller_computer)
            print("punten dealer "+str(punten_dealer))


        else:
            print("NO")
            if (punten_dealer <= punten_user and punten_dealer < 21):
                game['Dealer'].append(combinations[0])
                print(combinations[0])
                del combinations[0]
                punten_dealer = punten(game['Dealer'], teller_computer)
            print("punten dealer "+str(punten_dealer))


    if(punten_user > 21):
        print(str(punten_user) +"! You have lost!")
        score['Dealer'] +=1
    if(punten_user <= 21 and (punten_dealer > 21 or punten_user > punten_dealer)):
        print("Your score is: "+str(punten_user)+". Score of dealer: "+str(punten_dealer)+" You WON!")
        score['Gebruiker'] +=1
blackjack()

while ((score['Gebruiker'] <= 3) or (score['Dealer'] <= 3)):
    new_game = (input("Another round? Print \"Y\" for YES: ")).upper()
    if (new_game == "Y"):
        print("Games won, YOU: " + str(score['Gebruiker']) +" Dealer: "+ str(score['Dealer']))
        blackjack()
    else:
        print("stp")
