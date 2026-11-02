import random
import time

# Variables

points = 0
flips = 0
flip_actions = 0
heads_streak = 0
tails_streak = 0
best_streak = 0
flip_speed = 0.5
heads_chance = 0.5
point_multiplier = 1
speed_level = 0
chance_level = 0
point_level = 1
max_speed_level = 9
max_chance_level = 9
max_point_level = 5

#functions

def stat_show():
    print("\n=== STATS ===")
    print("Total flips:", flips)
    print("Button presses:", flip_actions)
    print("Points:", points)
    print("Current streak:", heads_streak)
    print("Best streak:", best_streak)
    print("Heads probability:", round(heads_chance * 100), "%")
    print("Flip delay:", round(flip_speed, 2), "seconds")
    print("Point multiplier:", point_multiplier, "x")
    print("Speed upgrade level:", speed_level, "/", max_speed_level)
    print("Point upgrade level:", point_level, "/", max_point_level)

def coin_draw(result):
    print("\n     _____")
    print("   /       \\")
    print("  |  "+ result+"  |")
    print("   \\_______/\n")


# main game loop

while True:

#intro
    print("\n=== COIN FLIP CHALLENGE ===")
    print("Get 10 heads in a row to win!")
    print("Try to win before flip 100!")
    print("\n1. Flip coin")
    print("2. Upgrades")
    print("3. View stats")
    print("4. Quit")
    choice = input("Choose an option: ")


#if Flip
    if choice == "1":
        input(f"Press Enter to flip the coin in {flip_speed} seconds...")
        flip_actions += 1

        
        time.sleep(flip_speed)

        if random.randint(1, 100) == 1:
            number_of_flips = 2
            print("\nSomething unusual happens...")
            print("The coin flips twice!")
            print("No points are rewarded...")
        else:
            number_of_flips = 1
        game_ended = False

        for i in range(number_of_flips):
            flips += 1
            if random.random() < heads_chance:
                result = "HEADS"
                heads_streak += 1
                tails_streak = 0
                if number_of_flips == 1:
                    points += 3 * point_multiplier
                    points_earned = 3 * point_multiplier
                else:
                    points_earned = 0

                    # tested using coin_flip() and even coin_flip(result) and the output didnt work 
                coin_draw(result)
                if points_earned > 0:
                    print("Heads bonus!")
                    print("Points earned:", points_earned)
                else:
                    print("Points earned: 0")
            else:
                result = "TAILS"
                tails_streak += 1
                heads_streak = 0
                if number_of_flips == 1:
                    points += 1 * point_multiplier
                    points_earned = 1 * point_multiplier
                else:
                    points_earned = 0

                    # tested using coin_flip() and even coin_flip(result) and the output didnt work 
                coin_draw(result)
                print("Points earned:", points_earned)
            best_streak = max(best_streak, heads_streak)
            print("Result:", result)
            print("Current streak:", heads_streak, "/ 10")
            print("Total flips:", flips)
            print("Points:", points)


            # Endings:

            if tails_streak == 10:

                #rarer endings
                print("\n=== Secret Ending ===")
                print("The coin lands on the other side once again.")
                print("Ten tails.")
                print("Against all odds, you found the other side.")
                print("\n*** SECRET ENDING UNLOCKED ***")
                game_ended = True
            elif heads_streak == 10 and flip_actions < 10:
                print("\n=== Unimaginable Ending ===")
                print("Wow,")
                print("You got 10 consecutive heads in fewer than 10 button presses.")
                print("That should not have happened.")
                print("\n*** ENDING UNLOCKED ***")
                game_ended = True
                #basic endings
            elif heads_streak == 10:
                if flips < 100 and flips > 10:
                    print("\n=== Early Ending ===")
                    print("You got 10 heads in a row before flip 100!")
                    print("That's either skill, or luck!")
                elif flips == 10:
                    print("\n=== Impossible Ending ===")
                    print("You got 10 heads in 10 flips!")
                    print("Buy a lottery ticket!")
                else:
                    print("\n=== Late Ending ===")
                    print("You got 10 heads in a row at or after flip 100!")
                game_ended = True
            if game_ended:
                break

        if game_ended:
            print("\nTotal flips:", flips)
            print("Button presses:", flip_actions)
            print("Final points:", points)
            replay = input("Play again for another ending? (y/n): ").lower()

            #Could make function, chose not to
            if replay == "y":
                points = 0
                flips = 0
                flip_actions = 0
                heads_streak = 0
                tails_streak = 0
                best_streak = 0
                flip_speed = 0.5
                heads_chance = 0.50
                point_multiplier = 1
                speed_level = 0
                chance_level = 0
                point_level = 1
            else:
                print("Thanks for playing!")
                break

#If upgrades
    elif choice == "2":
        while True:
            print("\n=== UPGRADES ===")
            print("Your points:", points)
            if speed_level == max_speed_level:
                print("1. Flip speed: MAXED OUT")
            else:
                speed_cost = 20 + (speed_level * 15)
                print("1. Faster flips - Cost:", speed_cost)
                print("   Current delay:", round(flip_speed, 2), "seconds")
            if chance_level == max_chance_level:
                print("2. Heads probability: MAXED OUT")
            else:
                chance_cost = 30 + (chance_level * 20)
                print("2. Better odds - Cost:", chance_cost)
                print("   Current chance:", round(heads_chance * 100), "%")
            if point_level == max_point_level:
                print("3. Point boost: MAXED OUT")
            else:
                point_cost = 35 + ((point_level - 1) * 25)
                print("3. Point boost - Cost:", point_cost)
                print("   Current multiplier:", point_multiplier, "x")
            print("4. Back to main menu")
            upgrade = input("Choose an upgrade: ")
            # Flip speed upgrade
            if upgrade == "1":
                if speed_level == max_speed_level:
                    print("This upgrade is already maxed out!")
                else:
                    speed_cost = 20 + (speed_level * 15)
                    if points >= speed_cost:
                        points -= speed_cost
                        speed_level += 1
                        flip_speed = 0.5 - (speed_level * 0.1)
                        print("Flip speed upgraded!")
                        print("New delay:", round(flip_speed, 2), "seconds")
                        print("Points remaining:", points)
                    else:
                        print("Not enough points!")
            # Probability upgrade
            elif upgrade == "2":
                if chance_level == max_chance_level:
                    print("This upgrade is already maxed out!")
                else:
                    chance_cost = 30 + (chance_level * 20)
                    if points >= chance_cost:
                        points -= chance_cost
                        chance_level += 1
                        heads_chance = 0.50 + (chance_level * 0.05)
                        print("Heads probability upgraded!")
                        print("New chance:", round(heads_chance * 100), "%")
                        print("Points remaining:", points)
                    else:
                        print("Not enough points!")
            # Point boost upgrade
            elif upgrade == "3":
                if point_level == max_point_level:
                    print("This upgrade is already maxed out!")
                else:
                    point_cost = 35 + ((point_level - 1) * 25)
                    if points >= point_cost:
                        points -= point_cost
                        point_level += 1
                        point_multiplier = point_level
                        print("Point boost upgraded!")
                        print("New multiplier:", point_multiplier, "x")
                        print("Points remaining:", points)
                    else:
                        print("Not enough points!")
            elif upgrade == "4":
                break
            else:
                print("Invalid choice!")

#If stats
    elif choice == "3":
        stat_show()
#If quit
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Try again!")