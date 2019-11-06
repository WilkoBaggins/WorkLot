from random import randint

choices = ["Rock", "Paper", "Scissors",]

computer = choices[randint(0,2)]

player = False

while player ==False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie, sadly!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lost!", computer, "Merked" you)
            else:
                print("You won!", you, "Merked" computer)
            elif player == "Paper":
                if computer == "Scissors":
                    print("You lost!", computer "Slashed", you)
                    else:
                        print("You won!", you "Slashed", computer)
                        elif player == "Scissors":
                            if computer == "Rock":
                                print("You lost", computer, "Smashed", you)
                                else:
                                    print ("you win!", you, "Smashed" computer)
                                    else :
                                        print("Error!, please check the spell doofus!")
