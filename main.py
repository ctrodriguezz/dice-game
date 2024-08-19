from random import randint


# Sign up function#
def signUp():
    print("Welcome to 2Dice, your favourite 2 player dice game!\n")
    while True:
        # First player sign-up#
        print("Player 1 Sign up -")
        username1 = input("Please enter your desired username: ")
        password1 = input("Please enter your password: ")
        while True:  # nested while loop for second user to sign-up#
            print("Player 2 Sign up -")
            username2 = input("Please enter your desired username: ")
            password2 = input("Please enter your password: ")
            if username2 == username1:
                print("Username already in use. Try again.")
            else:
                print("\nThanks for signing up to 2Dice " + username1.upper() + " and " + username2.upper() + "!")
                signIn1(username1, username2, password1, password2)  # Pass variables to signIn1 function#
                break  # Break to end loop once both players have signed up#
        break

# Sign-in function for first player with variables passed through from sign-up function#
def signIn1(username1, username2, password1, password2):
    print("Log-in: ")
    while True:
        signin_username1 = input("Enter your username: ")
        signin_password1 = input("Enter your password: ")
        if signin_username1 == username1:
            if signin_password1 == password1:  # Nested if statements to check password is also correct#
                print("Successful login!")
                signIn2(username1, username2, password1, password2, signin_username1)  # passing variables#
                break  # end loop if login is successful#
            else:
                print("Username/Password do not match.\nTry again:")
                continue  # continue statement to re-loop to top of while loop avoid doubling error messages#
        if signin_username1 == username2:
            if signin_password1 == password2:
                print("Successful login!")
                signIn2(username1, username2, password1, password2, signin_username1)  # passing variables#
                break
            else:
                print("Username/Password do not match.\nTry again:")
                continue
        else:
            print("Username/Password do not match.\nTry again:")

# Sign-in function for second player with variables passed through from sign-up function#
def signIn2(username1, username2, password1, password2, signin_username1, ):
    print("Player 2 Log-in:")
    while True:
        signin_username2 = input("Enter your username: ")
        signin_password2 = input("Enter your password: ")
        if signin_username2 == username1 and signin_username2 != signin_username1:
            # != signin_username1 to ensure users do not repeat the login info from first login#
            if signin_password2 == password1:
                print("Successful login!")
                userArrange(username1, username2)  # passing variables#
                break
            else:
                print("Username/Password do not match.\nTry again:")
        if signin_username2 == username2 and signin_username2 != signin_username1:
            if signin_password2 == password2:
                print("Successful login!")
                userArrange(username1, username2, )  # passing variables#
                break
            else:
                print("Username/Password do not match.\nTry again:")
        else:
            print("Username/Password do not match.\nTry again:")


def userArrange(username1, username2):
    player1 = username1.upper()  # changing username variable to players one and two#
    player2 = username2.upper()  # setting it so that usernames are displayed in all caps#
    print("\n*****GAME RULES:*****\n\n"  # GAME RULES#
          "• The points rolled on each player’s dice are added to their score.\n• If the total is an even number, an "
          "additional 5 points are added to their score.\n• If the total is an odd number, 5 points are subtracted from"
          " their score.\n• If they roll a double, they get to roll one extra die and get the number of points rolled"
          " added to their score.\n• The score of a player cannot go below 0 at any point.\n• The person with the "
          "highest"
          " score at the end of the 5 rounds wins.\n• If both players have the same score at the end of the 5 rounds,"
          " they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).\n")
    input("PRESS ENTER TO CONTINUE")
    rollDice(player1, player2)

 
def rollDice(player1, player2):
    p1_score = 0  # setting scores to 0 to begin game#
    p2_score = 0

    print("\nTime for some 2Dice!\n\n" + player1 + " you will roll first.\n" + player2 +
          " you will roll second.\n\nRemember that you have 2 goes per round.\n\nGood luck!\n")

    for rolls in range(0, 5):
        print(str(player1) + "'s current score = " + str(p1_score))
        input(str(player1) + "'s first roll: \n*Press ENT to roll*")
        p1_first_roll = randint(1, 6)  # random number bete=ween 1 and 6 to simulate a dice roll#
        p1_score += p1_first_roll  # adding roll to total score#
        print("First roll: " + str(p1_first_roll) + "\n")
        input(str(player1) + "'s second roll: \n*Press ENT to roll*")
        p1_sec_roll = randint(1, 6)  # random number bete=ween 1 and 6 to simulate a dice roll#
        p1_score += p1_sec_roll  # adding roll to total score#
        print("Second roll: " + str(p1_sec_roll) + "\n")
        if (p1_first_roll + p1_sec_roll) % 2 == 0:  # if number is even#
            p1_score += 5  # adding bonus to total score#
            print("BONUS! +5 points")
            print(str(p1_first_roll) + " + " + str(p1_sec_roll) + " + " + "5")
            print("Your new score is= " + str(p1_score) + "\n")
            if p1_first_roll == p1_sec_roll:  # if double rolls#
                print("YOU ROLLED DOUBLE! EXTRA ROLL")
                input("\n*Press ENT to roll*")
                p1_third_roll = randint(1, 6)  # random number bete=ween 1 and 6 to simulate a dice roll#
                p1_score += p1_third_roll
                print("Bonus roll: " + str(p1_third_roll) + "\n")
                print(str(p1_score) + " + " + str(p1_third_roll))
                print("Your new score is = " + str(p1_score) + "\n")
        elif (p1_first_roll + p1_sec_roll) % 2 != 0:  # if number is odd#
            if p1_score < 0:
                p1_score = 0
                print("UNLUCKY -5 points")
                print("\nYour new score is = " + str(p1_score) + "\n")
            else:
                p1_score -= 5
                print("UNLUCKY -5 points")
                print(str(p1_first_roll) + " + " + str(p1_sec_roll) + " - 5")
                print("\nYour new score is = " + str(p1_score) + "\n")

        print(str(player2) + "'s current score = " + str(p2_score))  # REPEAT OF USER 1's ROLLS#
        input(str(player2) + "'s roll: \n*Press ENT to roll*")
        p2_first_roll = randint(1, 6)
        print("First roll: " + str(p2_first_roll) + "\n")
        p2_score += p2_first_roll
        input(str(player2) + "'s second roll: \n*Press ENT to roll*")
        p2_sec_roll = randint(1, 6)
        print("Second roll: " + str(p2_sec_roll) + "\n")
        p2_score += p2_sec_roll
        if (p2_first_roll + p2_sec_roll) % 2 == 0:
            p2_score += 5
            print("BONUS! +5 points")
            print(str(p2_first_roll) + " + " + str(p2_sec_roll) + " + " + "5")
            print("Your new score is= " + str(p2_score) + "\n")
            if p2_first_roll == p2_sec_roll:
                print("YOU ROLLED DOUBLE! EXTRA ROLL")
                input("\n*Press ENT to roll*")
                p2_third_roll = randint(1, 6)
                print("Bonus roll: " + str(p2_third_roll) + "\n")
                print(str(p2_score) + " + " + str(p2_third_roll))
                p2_score += p2_third_roll
                print("Your new score is = " + str(p2_score) + "\n")
        elif (p2_first_roll + p2_sec_roll) % 2 != 0:
            if p2_score < 0:
                p2_score = 0
                print("UNLUCKY -5 points")
                print(str(p2_first_roll) + " + " + str(p2_sec_roll) + " - 5")
                print("\nYour new score is = " + str(p2_score) + "\n")
            else:
                p2_score -= 5
                print("UNLUCKY -5 points")
                print(str(p2_first_roll) + " + " + str(p2_sec_roll) + " -  5")
                print("\nYour new score is = " + str(p2_score) + "\n")
    checkWinner(player1, player2, p1_score, p2_score)


def checkWinner(player1, player2, p1_score, p2_score):  # checking winner and congratulating#
    if p1_score > p2_score:
        print("\nCongratulations " + player1 + ", you have a score of " + str(p1_score) + ", you have the bigger"
                                                                                          " score.\nYou win!\n")

    elif p2_score > p1_score:
        print("\nCongratulations " + player2 + ", you have a score of " + str(p2_score) + ", you have the bigger"
                                                                                          " score.\nYou win!\n")

    else:
        while p1_score == p2_score:  # tie-breakers if scores are the same#
            print("\n\n" + str(player1) + " and " + str(player2) + " your scores are tied at " + str(p1_score) + "!\n\n"
                                                "You will play one more round for the tie-breaker!\n\nGood luck!\n\n")
            input(str(player1) + "'s roll: \n*Press ENT to roll*")
            p1_extra_roll = randint(1, 6)
            p1_score += p1_extra_roll
            print(p1_extra_roll)

            input(str(player2) + "'s roll: \n*Press ENT to roll*")
            p2_extra_roll = randint(1, 6)
            p2_score += p2_extra_roll
            print(p2_extra_roll)
            if p1_extra_roll > p2_extra_roll:
                print(
                    "\nCongratulations " + player1 + ", you have a score of " + str(p1_score) + ", you have the bigger"
                                                                                                " score.\nYou win!\n")
                break  # end loop if there is a winner#

            elif p2_extra_roll > p1_extra_roll:
                print(
                    "\nCongratulations " + player2 + ", you have a score of " + str(p2_score) + ", you have the bigger"
                                                                                                " score.\nYou win!\n")
                break  # end loop if there is a winner#
    scoreboard(player1, player2, p1_score, p2_score)


def scoreboard(player1, player2, p1_score, p2_score):
    with open("scoreboard.txt", "a") as f:  # open external file as f to append#

        if p1_score > p2_score:  # checking for winner to write in external leaderboard#
            f.write(str(p1_score) + " : " + player1 + "\n")
        else:
            f.write(str(p2_score) + " : " + player2 + "\n")

    with open("scoreboard.txt", "r") as f:  # open external file as f to read#
        print("Highest Scores:")
        scores = [line.strip().split(" : ") for line in f]  # strips whitespaces and splits strings to two#
        scores.sort(key=lambda x: x[0], reverse=True)  # sorts in descending order by score (position 0)#
        for i in range(5):  # for loop to print top 5 scores#
            print(' - '.join(scores[i]))


signUp()  # call signup function#
