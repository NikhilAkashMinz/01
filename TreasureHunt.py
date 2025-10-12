

print("Welcome to Treasure Island.")
print("YOUR MISSION IS TO FIND TREASURE")

print("Your at a cross road. Where do you want to go?")

lr = input("Type Left or Right : ")
if lr == 'Left' or lr == 'left' or lr == 'LEFT':
    wg = input('You have come to a lake .There is a island in middle you can "wait" or "swim" :')
    if wg == 'swim' or wg == 'Swim' or wg == 'SWIM':
        print("You are attacked by the Andaconda \ You are Dead")
        exit(0)
    elif wg == 'wait' or wg == 'Wait' or wg == 'WAIT':
        print("You Reached the island ")
        tre = input("There are three doors in the island 'Red','Blue' or 'Green':  ").lower()
        if tre == 'Red':
            print("You are burnt by fire and You are 'GAY'.")
            exit(0)
        elif tre == 'Blue':
            print("You are attacked by Gay rapist. And you are GAY.")
            exit(0)
        elif tre == 'Green':
            print("You Found the treasure and You are a GAY treasure hunter.")
            print("Game Over")
            exit(0)
    else :
        print("invalid Input")
        exit(0)
elif lr == 'Right' or lr == 'right' or lr == 'RIGHT':
    print("You Fell in a hole.GameOver")
    exit(0)
else :
    print("Invalid input. Please try again.")
    exit(0)

