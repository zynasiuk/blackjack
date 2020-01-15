import random
nummers = [2,3,4,5,6,7,8,9,10, "Boer", "Koningin", "Koning", "Aas"]
kleur = ["klvr", "rt", "hrt", "schp"]
combinations=[]
teller_gebruiker = 0
teller_computer = 0
score = {'Gebruiker': 0, 'Dealer': 0 } #f7

def blackjack(): #f6
    for y in kleur: #Fase 1:
        for z in nummers:
            x = (z, y)
            combinations.append(x)
    #Fase 2:
    random.shuffle(combinations)    #print("First shuffle: ", combinations)
    random.shuffle(combinations)    #print("Second shuffle: ", combinations)
    random.shuffle(combinations)    #print("Third shuffle: ", combinations)

    game = {'Gebruiker': [], 'Dealer': [] }

    game['Dealer'].append(combinations[0])
    game['Gebruiker'].append(combinations[1])
    game['Gebruiker'].append(combinations[2])
    game['Dealer'].append(combinations[3])

    del combinations[0:4]

    print("Your cards: " + str(game['Gebruiker']))
    print("Dealer's last card: " + str(game['Dealer'][-1]))

    #Fase 3:
    def punten(wie, teller):
        for i in wie:
            if (i[0] == 'Boer' or i[0] == 'Koningin' or i[0] == 'Koning') or (i[0] == 'Aas' and teller > 11):
                teller += 10
            elif (i[0] == 'Aas' and teller < 11):
                teller += 1
            else:
                teller += i[0]
        return teller

    punten_dealer = punten(game['Dealer'], teller_computer)
    punten_user = punten(game['Gebruiker'], teller_gebruiker)

    # fase 4
    while punten_user <= 21 and punten_dealer <= 21:
        hit_of_stand = (input("Do you want another card? Print \"Y\" for more: ")).upper()
        if hit_of_stand == "Y":
            game['Gebruiker'].append(combinations[0])
            del combinations[0]
            punten_user = punten(game['Gebruiker'], teller_gebruiker)
            #f5
            if punten_dealer <= punten_user:
                game['Dealer'].append(combinations[0])
                print(combinations[0])
                del combinations[0]
                punten_dealer = punten(game['Dealer'], teller_computer)
            print("Your cards: "+str(game['Gebruiker']) + " what gives "+str(punten_user) + " points.")
            print("Dealer's last card: "+str(game['Dealer'][-1]))
#f5
        if hit_of_stand != "Y" and punten_dealer <= punten_user:
            game['Dealer'].append(combinations[0])
            print(combinations[0])
            del combinations[0]
            punten_dealer = punten(game['Dealer'], teller_computer)
        print(str(game['Gebruiker']) + " what gives "+str(punten_user) + " points to the user.")
        print(str(game['Dealer']) + " punten dealer "+str(punten_dealer)+ " points to the dealer.")

#f4
    if punten_user > 21:
        print(str(punten_user) +"! You have lost!")
        score['Dealer'] +=1 #s7
#f5
    if punten_user <= 21 and (punten_dealer > 21 or punten_user > punten_dealer):
        print("Your score is: "+str(punten_user)+". Score of dealer: "+str(punten_dealer)+" You WON!")
        score['Gebruiker'] +=1 #s7

blackjack()

def winner():
    if (score['Gebruiker'] == 3):
        return("Y O U are")
    else:
        return("Dealer is")

#f6
while score['Gebruiker'] < 3 and score['Dealer'] < 3:
    new_game = (input("Another round? Print \"Y\" for YES: ")).upper()
    if (new_game == "Y"):
        print("YOU: " + str(score['Gebruiker']) +" Dealer: "+ str(score['Dealer']))
        blackjack()
    else:
        print("Game over!")
        break

print("YOU: " + str(score['Gebruiker']) +" Dealer: "+ str(score['Dealer']) +"\n"+ winner() + " the winner!!! ")
