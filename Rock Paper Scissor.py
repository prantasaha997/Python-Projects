while True:
    import random
    item_list = ["rock", "paper", "scissor"]

    Your_choice = input("Enter your move: ")
    comp_choice = random.choice(item_list)
    
    print(f"Your choice = {Your_choice}, Computer choice = {comp_choice}")

    if Your_choice == comp_choice:
        print("Match Tie Bro!\n")

    elif Your_choice == "rock":
        if comp_choice == "paper":
            print("Computer(paper) Win!\n")
        else:
            print('You(rock) Win!\n')

    elif Your_choice == "rock":
        if comp_choice == "scissor":
            print("Computer(scissor) Win!\n")
        else:
            print("You(rock) Win!\n")

    # p-s=s win, p-r=r win

    elif  Your_choice == "paper":
        if comp_choice == "scissor":
            print("Computer(scissor) Win!\n") 
        else:
            print("You(paper) Win!\n")

    elif Your_choice == "paper":
        if comp_choice == "rock":
            print("You(rock) Win!\n") 
        else:
            print("Computer(rock) Win!\n")
        
    #s-p=s win, s-r=r win

    elif Your_choice == "scissor":
        if comp_choice == "paper":
            print("You(scissor) Win!\n")
        else:
            print("Computer(paper) Win!\n")

    elif Your_choice == "scissor":
        if comp_choice == "rock":
            print("Computer(rock) Win!\n")
        else:
            print("You(scissor) Win!\n")

    else:
        print("Khela Bujhe na!\n")

