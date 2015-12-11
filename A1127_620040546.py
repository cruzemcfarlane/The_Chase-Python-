#620040546
#620053190

import random
import sys

#function to generate a random integer between 1 and 6
def roll(): 
    return random.randint(1,6)


#function to create an ADT called dice
def makeDice(): 
    return ('dice',[roll()])

#function to check if the ADT is indeed a dice type
def isDice(dice): 
    return type(dice)==tuple and dice[0]=='dice' and type(face(dice))==list

#function to return the list of dice element
def face(dice): 
    return dice[1]


#function to return the element at index zero
def facevalue(dice): 
    return face(dice)[0]


#function to update the facevalue of the dice when it is rolled
def rollDice(dice): 
    if isDice(dice)==True:
        face(dice).pop()  
        face(dice).append(roll())
        

#function to display the players and the dice that they rolled
def displayAndRoll(p1,p2,d1,d2):
    print '\nPlayers ', p1, 'and ', p2,' each have a dice. Going to roll each of them'

    rollDice(d1) 
    rollDice(d2)

    #Show what new facevalue the given players rolled for each dye
    print 'Dice 1: Player ', p1, ' has rolled a ', facevalue(d1) 
    print 'Dice 2: Player ', p2, ' has rolled a ', facevalue(d2) 


#function to decide whether to pass the dye to the next player or not
def passDice(fv_dice):
    if fv_dice==1 or fv_dice==6: 
        return True 
    else:
        return False 


#function to determine the next player
def nextPlayer(player,face_v,total_p):
    lst_tot_p=[x for x in range(0,total_p)] #create a list of players

    if face_v==1: #if the facevalue is 1
        if player<=lst_tot_p[0]: #check if the next player is lower than zero
            return lst_tot_p[total_p-1] #if it is, start with the player at the other end of the list
        else:
            return lst_tot_p[player-1] #otherwise, move to the left

    elif face_v==6: #if the facevalue is 6 instead
        if player>=lst_tot_p[total_p-1]: #check if the next player exceeds the list
            return lst_tot_p[0] #if it does, start with the player at the other end of the list
        else:
            return lst_tot_p[player+1] #otherwise, move to the right
        
    else: #if neither 1 or 6 is played
        return player #the current player should continue playing


#function to play the Chase Game
def play():
    
    #variables to store dice data type
    dice1=makeDice() 
    dice2=makeDice()

    cont_quit=''


    total_p=int(raw_input('\nHow many players (even numbers only)?: ')) 

    #assume the initial first player is player zero and determine the opposite player
    f_playr=0
    opp_playr=total_p/2 

    #if the total number of players is an even number continue playing
    if total_p%2==0:

        #while one player is not in possession of both dye
        while (f_playr!=opp_playr):
            
            displayAndRoll(f_playr,opp_playr,dice1,dice2)

            #Select next players
            f_playr=nextPlayer(f_playr,facevalue(dice1),total_p)
            opp_playr=nextPlayer(opp_playr,facevalue(dice2),total_p)

            #if dice1 and dice2 roll both  (1 and 6) or (1 and 1) or (6 and 6) simulateously
            if passDice(facevalue(dice1))==True and passDice(facevalue(dice2))==True:

                #Inform the players which dice they have
                print '\nPlayer ', f_playr, 'now has dice 1'
                print 'Player ', opp_playr, 'now has dice 2'

                cont_quit=raw_input("\nPress any key to roll again or 'q' to stop: ")
                
                #if a player has both dice congratulate them and ask to quit or continue playing
                if f_playr==opp_playr:
                    print '\nCongratulations! Player', f_playr, 'you won!!!'
                    sys.exit()

                elif cont_quit=='q' or cont_quit=='Q':
                    sys.exit()
                
            #if dice1 rolled either 1 or 6    
            elif passDice(facevalue(dice1))==True:

                #inform them that they have the dice 
                print '\nPlayer ', f_playr, 'now has dice 1'

                cont_quit=raw_input("\nPress any key to roll again or 'q' to stop: ")
                
                #if a player has both dice congratulate them and ask to quit or continue playing
                if f_playr==opp_playr:
                    print '\nCongratulations! Player', f_playr, 'you won!!!'
                    sys.exit()

                elif cont_quit=='q' or cont_quit=='Q':
                    sys.exit()
                  
            #if dice2 rolled either 1 or 6       
            elif passDice(facevalue(dice2))==True:

                #inform them that they have the dice 
                print '\nPlayer ', opp_playr, 'now has dice 2'

                cont_quit=raw_input("\nPress any key to roll again or 'q' to stop: ")
                
                #if a player has both dice congratulate them and ask to quit or continue playing
                if opp_playr==f_playr: 
                    print '\nCongratulations! Player', opp_playr, 'you won!!!'
                    sys.exit()

                elif cont_quit=='q' or cont_quit=='Q':
                    sys.exit()
                    
                

    #if the total number of player entered was not an even number, make user start over   
    else:
        print '\nSorry, but thats not an even number!\n'
        return play()
