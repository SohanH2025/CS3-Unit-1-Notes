

def main():
    #print("this is a bot that helps solve NYT Connections by showing all posible solutions left when at 2/4 connections solved\n    when two connections are left there are only two possibilities in a guess: you either get one off or nothing. \n        one off is self expainitory, one of the words is inncorrect. \n        nothing means, when they're only two groups left, that your guess has two words from one group and two words from the other. \n.   another key idea is that each guess will have the same result (ie one away or nothing) with its opposite guess meaning that if your guess is one away the opposite guess available ")
    #print("assume the top left is numbered 1 and to its right is 2, 3, 4, then the bottom left is 5 and to its right is 6, 7, 8")

    poss = {1, 2, 3, 4, 5, 6, 7, 8}
    possibilities = []

    ax = True
    while (ax):
        inj = input("what numbers were your guess? (no spaces. ex: '2387')\n")

        if (len(inj) == 4):
            
            numb = 0
            for letter in inj :
                if ('1' in letter or '2'in letter or '3' in letter or '4' in letter or '5' in letter or '6' in letter or '7' in letter or '8' in letter):
                    numb += 1
            
            if (numb == 4):
                numbers = int(inj)
                num_4 = numbers%10 
                numbers = int(numbers/10)
                num_3 = numbers%10 
                numbers = int(numbers/10)
                num_2 = numbers%10 
                numbers = int(numbers/10)
                num_1 = numbers%10
                numbers = int(numbers/10)

                guess = {num_1, num_2, num_3, num_4}
                alt_guess = poss.difference(guess)

                print(guess)
                print(alt_guess)
                
                
                if (len(alt_guess) == 4) :
                    ax = False
                else:
                    print("invalid numbers")
            else:
                print("invalid response")
        else:
            print("invalid character amount")





    still = True
    while (still):
        inp = input("1 away? (y/n)\n")
        if (inp == "y"):
            one_away = True
            still = False
        elif (inp == "n"):
            one_away = False
            still = False
        else:
            print("invalid response")



    
    
    
    if (one_away): # if one away
        if (len(possibilities) == 0): #if hasn't been ran set possiblilities to all possibilities of the gues
            possibilities = possibilities_one_away(guess, alt_guess)
        #else:
            

    elif (not one_away) : #else if not one away
        if (len(possibilities) == 0): #if hasn't been ran
            possibilities = possibilities_not_one_away(sorted(guess), sorted(alt_guess))
        #else: 
            


    
    
    print(possibilities)


def possibilities_one_away(guess, alt_guess): 

    poss = {1, 2, 3, 4, 5, 6, 7, 8}
    possibilities = []
    for alt_word in alt_guess : # for each word in the alternate guess
            for word in guess : # repace each word, one at a time, in the guess

                word_set = {word} #turn 'word' into a set to make functional
                possibility = guess.difference(word_set) # remove the word being replaced
                possibility.add(alt_word) #add the word from alternate guess
                alt_possibility = poss.difference(possibility) #create new alternate guess

                possibilities.append([possibility, alt_possibility]) #add both possibilities to possibilities
    return possibilities

def possibilities_not_one_away(guess, alt_guess):

    poss = {1, 2, 3, 4, 5, 6, 7, 8}
    group_1 = []
    group_2 = []
    possibilities = []

    #find all possible groups of two for guess
    for fir in range(len(guess)): #for each index (num) in guess
        sec = fir + 1 #starting with the index after num
        while (sec < len(guess)): 
            group_1.append({guess[fir], guess[sec]})
            sec += 1

    #find all possible groups of two for alt_guess
    for fir in range(len(alt_guess)): #for each index (num) in alt_guess
        sec = fir + 1 #starting with the index after num
        while (sec < len(alt_guess)): 
            group_2.append({alt_guess[fir], alt_guess[sec]})
            sec += 1
    #print("GROUP 1")
    #print (len(group_1))
    #print("GROUP 2")
    #print (len(group_2))
    for x in range(len(group_1)):
        for y in range(len(group_2)):
            possibilities.append(group_1[x].union(group_2[y]))
    
    #print("POSSIBILITIES")
    #print(len(possibilities))
    return possibilities
    
            
    



if __name__ == "__main__":
    main()
