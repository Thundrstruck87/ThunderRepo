# This program is a text based story game that asks for user input. Story continues based from input
#
# import time
story = False
thanks: str = "Thanks for playing! I hope you enjoyed this text based story game."

print("Welcome to the game!")
print()
print("This is a text based story game based on your answers.")
print()
answer = input("Are you ready to play? (y/n): ")
if answer.casefold() == "y":
    # STORY BEGINS HERE
    print("Story begins")
    # time.sleep(2)
    print("...")
    # time.sleep(2)
    print("\n" * 10)  # This will a clear screen of any previous code
    print("""    You have been sleeping for the past 8 hours recovering from the journey to a new star system.
    The spaceport that you're on suddenly shakes you awake. You start to wake up as the lights flicker on
    and off. Realizing something doesn't feel right, you start to wake up. You look around the room - there
    are some basic necessities and a round window looking out into deep space. 
          """)
    answer = input("What do you do next? (sleep or get up?) [q to quit]: ")
    if answer.casefold() == "sleep":
        print("The spaceport was invaded by mercenaries, you died")
    elif answer.casefold() == "get up":
        print("\n" * 10)
        print("""        You get up look around to find nothing of immediate use. You open the door only to have people
        sprint past you in a panic. As you step into the hallway you look right and see the dark hallways being lit
        by emergency lighting. Sparks sputter, and lights flicker from the distant sounds of explosions.
        
        As you look left you notice a crowd of people running and gathering near the emergency exits and escape pods with
        armed guards guiding them as they scramble to get escape pods activated and sent out to safety.
        """)
        answer = input("Where do you go? (left of right?) [q to quit]: ")
        if answer.casefold() == "right":
            print("\n" * 10)
            print("""            You decided to pursue this further. You are a natural leader, and protector. You cautiously make your way through the corridor
            as the distant rumbles and sounds of explosions get louder. The lights flicker on and off as your senses are on high alert, getting you
            ready for anything. You come across a malfunctioning door that keeps closing the last few inches, reopening and closing again. You
            peak inside and see a small emergency selection of defense weapons, you force the door open and step inside. Knowing there could be
            life or death situations, you pick one.
            """)
            weapon = input("What do you choose? pistol, club, or nothing [q to quit]: ")
            print("\n" * 10)
            if weapon.casefold() == "pistol":
                print("""                You have chosen wisely. You pull the slide back to make sure there is an energy round in the chamber and get back into
                the hallway, as you make your way through, you stumble upon a group of armed station guards who are under fire. You sneak around
                the mercenaries and attack them at the flank. The small group of mercenaries are no more. You have saved the station and have
                achieved recognition and respect among the station and crew.
                
                Congratulations, you made it through the game alive!
                """)
                print()
                print(thanks)
            elif weapon.casefold() == "club":
                print("""                Barbaric - nice. You grab hold of the club and get back into the hallway, as you make your way through, you hear two
                mercenaries talk to each other and walking closer as you hide in a recessed wall. Just as they get past you, you jump out and
                managed to hit one on the head. The other starts hand to hand combat. Luckily for you, a few armed guards come to your
                rescue. One of the guards manage to walk you back to the escape pods to help you escape.
                
                Congratulations, you made it through the game alive!""")
                print()
                print(thanks)
            elif weapon.casefold() == "nothing":
                print("""Nothing ay? How daring.
                
                As you leave into the hallway and continue on, you see the mercenaries up ahead and they notice you - run! As you're running
                you manage to dive into an unknown room with quite the echo. The mercenaries lose you and continued on. The blast doors close
                and the life support senses you and kicks on the emergency lighting. The MFD's (Multifunction Displays) light up with things
                you have never seen before. One of the MFD's shows a map of the station you're on, highlighting your location, and the nearest decompression
                doors. You realize you can lock it, and open the farthest door to have the vacuum of space suck out the mercenaries.
                
                You saved the space station, the crew and all aboard due to your interesting actions and removal of the mercenaries!
                """)
                print(thanks)
        elif answer.casefold() == "left":
            print("\n * 5")
            print("""                  You immediately go back into your room and grab your personal device. You run down the well lit hallway
                  quickly joining the others as fear and panic set in. You've managed to get in the next escape pod to be launched
                  next. You've made it. You've made it to safety. The escape pod makes it's way into space where a near orbiting
                  star fleet warps in and takes in the escaped pods.
                  
                  You survived!
                  
                  Thanks for playing! I hope you enjoyed this text based story game.
                  """)
        elif answer.casefold() == "q":
            print(thanks)
    elif answer.casefold() == "q":
        print("Thanks for playing!")

    else:
        "Please try again"

elif answer == "n":
    print("Thanks for playing!")
else:
    print("Pleas enter y for yes, or n for no.")
