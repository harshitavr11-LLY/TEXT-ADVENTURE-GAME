
print("WELCOME TO THE ADVENTURE GAME")
print("You are exploring a mysterious treasure!")

name=input("ENTER YOUR NAME: ")
print("Let's start the adventure, " + name + "!")
inventory = []
health = 100
score=0
location = "lost jungle"
while True:
    if location == "lost jungle":
        print("\nLOST JUNGLE")
        print("1.GO TO THE ANCIENT CAVE ")
        print("2.GO TO THE LAKE WATER")
        print("3.GO TO THE  OLD CASTLE")
        print("4.Go TO THE  MYSTERY TEMPLE")
        print("5.check the inventory")
        print("6.quit the game")

        choice = input("Enter your choice (1/2/3/4/5/6): ")
        if choice == "1":
            location = " ancient cave"
        elif choice == "2":
            location = " water lake"
        elif choice == "3":
            location = " old castle"
        elif choice == "4":
            location = " mystery temple"
        elif choice == "5":

            if inventory:
                print("YOUR INVENTORY: " + ", ".join(inventory))
            else:
                print("Your inventory is empty.")
        elif choice=="6":
            print("Thank you for playing, " + name + "!")
            break

        else: 
            print("start the game again...this tym to win more points and increase the scores.")

    elif location =="cave":
        print("/nCAVE")
    elif location == "cave":

        print("\nYou entered the dark cave.")

        if "key" not in inventory:
            print("You found a key!")
            inventory.append("key")
        else:
            print("Nothing left here.")

        location = "lost jungle"
        break

    elif location == "water lake":

        print("\nYou reached the water lake.")

        if "boat" not in inventory:
            print("You found a boat!")
            inventory.append("boat")
        else:
            print("Nothing left here.")

        location = "lost jungle"

    elif location == "temple":

     print ("\nYou discovered a secret temple!")

    if "magic gem" not in inventory:

        print("You found a Magic Gem!")
        inventory.append("magic gem")

        score = score + 100
        print("Score:", score)
        print("You used the key to open the castle door.")
        print("You found the hidden treasure!")
    print("You opened the treasure box!")
    print("CONGRATULATIONS,", name + "!")
    print("YOU WIN THE GAME!")
    break

else:
    print("The temple is empty.")

location = "lost jungle"

   

            

            