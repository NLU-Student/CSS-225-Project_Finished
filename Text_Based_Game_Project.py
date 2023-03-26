#importing modules being used
import random                               
import time

#Defined Variables
name = input("Enter name: ")                  
a = "ankh"
ankh_b = False
inventory = []
disable = False
info_b = False
rest_b = False
item_b = False

def addToInventory(items):
    inventory.append(items)

#Intro to game
def intro():                                                               
    answer = input("Would you like to start the game?y/n:\n> ")
    print("\n\n")                         # inputting \n to space out lines
    if answer == "y":
        print("Welcome",name,"! You will now begin 'The Pharaohs Tomb'")
        print("\n\n")
        Chapter_1()
        
    elif answer == "n":
        print("We will await for your return.")
        print("\n\n")
        exit()
    else:
        print("Invalid input, Try again.")
        intro()
        
    

#Chapter 1:
def Chapter_1():
    print("Chapter 1: \n\n")
    print("As the scorching sun engulfs the sky and makes trekking the desert unbearable. A lucky traveler finds a safe haven in sight\n\n\n" ) # Chapter 1 Intro
    time.sleep(2)                               # using time module to give a sense of suspense 
    print("As", name, "comes across Albasta, an oasis in the desert! You are greeted by various tasks\n\n\n")  #Chapter 1 Scene
    time.sleep(2)
    Chp1_Task()
    

def Chp1_Task():
    global inventory                            #input global variables, kept getting undefined error
    global info_b
    global rest_b
    global item_b
    choice = int(input("Select choice?:\n1:interact with locals\n2:Rest at inn\n3:Go to marketplace.\n4.Go towards the South.\nEnter choice:(1, 2, 3, or 4)\n>  "))
    print("\n")
    time.sleep(2)
    i = "info"
    r = "rest"
    it = "item"

    if choice == 1:
            print("You interacted with the locals and you found out about a hidden pyramid filled with boundless amount of riches. However the path is treacherous!\n\n ")
            outcome = input("Do you want additional details?: y/n \n> ")
            if outcome == "y":
                addToInventory(i)
                print("You found out about Sandy Tombs that is located in the South, but you will need to cross the River of Styx!\n\n")
                info_b = True
                print("Chapter 1: ")
                Chp1_Task()
                
            else:
                print(" No useful information found, Try asking again?\n\n")   
                print("Chapter 1: ")
                Chp1_Task()  
                

    elif choice == 2: 
            print("You went to a inn, and payed for a short-term room.\n\n")
            response = input("Do you want to rest for the day? y/n:\n> ")
            if response == "y":
                addToInventory(r)
                print("You took a nap and regained your energy!\n\n")
                rest_b = True
                print("Chapter 1: ")
                Chp1_Task()
                
            else:
               print('You should rest up before you begin your journey!\n\n')
               print("Chapter 1: ")
               Chp1_Task()
               
    elif choice == 3:
            item = True
            print("You went to the bustling market and are mesmirized by the amount of merchants selling various goods.\n\n")
            cost = input("Do you want to purchase any items for your  inventory? y/n:\n> ")
            if cost == "y":
                addToInventory(it)
                print("You aquire new armor, potions, and rations for your journey.\n\n")
                item_b = True
                print("Chapter 1: ")
                Chp1_Task()
                
            else:
               print('You should really purchase some items for your inventory.\n\n')
               print("Chapter 1: ")
               Chp1_Task()
               
    elif choice == 4:
            if  info_b == True and rest_b == True and item_b == True:
                print("You are ready to head South!\n\n")
                direction =input("Do you want to head South? y/n:\n> ")
                if direction == "y":
                    print("You're heading south towards the desert!\n\n")  
                   
                    Chapter_2() 
                elif direction == "n":
                    print("Chapter 1: ")
                    Chp1_Task()
            else:
                print("You're not ready to move on, you still need to do additional tasks.\n\n")
                print("Chapter 1: ")
                Chp1_Task()
    else:
         print ("Invalid Input Try again\n\n")
         print("Chapter 1: ")
         Chp1_Task()
         

            

#Chapter 2
 
def Chapter_2():
    print("Chapter 2: \n\n")
    print("As you set sail through the River of Styx. You are mesmerized by the pitch-black waterways that splits the desert and gives a feeling of a deptless river.\n\n\n") # Chapter 2 intro
    print("Suddenly a raging storm begins to form out of nowhere and you're left with limited options?\n\n\n ") #Chapter 2 Scene
    Chp2_Task()

def Chp2_Task():
    option = int(input("Select an options:\n1.Return North.\n2.Go through the long route.\n3.Push Throught the storm.\nEnter choice: "))
    print("\n")
    if option == 1:
        print("With your quick thinking you determine that waiting out the storm is the best idea and you decide to head back North.\n\n")
        print("Chapter 1: ")
        Chp1_Task()
    elif option == 2:
        print("With your determination you were able to spot a hidden route! Althought it took longer to arrive at the destination you made it out alive.\n\n")
        Chapter_3()
        
    elif option == 3:
        print("You have died! You're boat capsized and you sanked into the depths of the river.\n\n")
        exit()
    else:
        print ("Invalid input, Please try again.\n\n ")   
        print("Chapter 2: ")
        Chp2_Task()
    

# Chapter 3:
def Chapter_3():
    print("Chapter 3: \n\n")
    print("You arrive at the Sandy Tombs; turbulent winds causes a sandstorm to form as you try to locate the unnamed tomb, when suddenly a pack of jackals begin hounding you!\n\n")
    print("You hastily run away and you encounter 2 identical tombs. Currently you're in a dire situation between 2 uknown tombs and a pack of jackals\n\n ")
    Chp3_Task()


def Chp3_Task():
    global inventory 
    option = int(input("Select an options:\n1: Enter Tomb #1\n2: Enter Tomb #2\n3: Fight off the jackals\nEnter choice:"))
    print("\n")

    if option == 1:
        print(" You enter Tomb #1, but suddenly a black hole appears and engulfs you and transports you back to Alabasta!\n\n")
        print("Chapter 1: ")
        Chp1_Task()
    elif option == 2:
        print("You successfully chosen the correct tomb!After navigating the tomb you found a secret passage-way that leads you to your desire destination.\n\n")
        Chapter_4()
        
    elif option == 3:
        print("You are at a standstill with the pack of jackals and you're at your wits end? However you notice 2 identical swords on the ground, but one is real and the other is a fake! \n\n")
        print("Testing your luck you muster all your stregth and pick one of the swords up. \n\n")
       
        outcome =random.randint(1, 11)
        pickup = int(input("Test your luck, Pick a number between 1-10:\n> "))   
        if pickup < 1 or pickup > 10:
            print("Invalid, Enter number between 1 and 10")  
            print("Chapter 3: ")
            Chp3_Task()
        elif pickup >= 1 or pickup <= 10:
            print("You picked", pickup)
            if pickup >= outcome:
                print('You succesfully defeated the pack of jackals and a golden ankh was dropped by the aplha!\n\n')  
                pickup = input("Type 'y' to pick up ankh and put it inventory:\n> ")
                if pickup == "y":   
                    addToInventory(a)
                    print("You picked up the anhk!\n\n")
                    print("Chapter 3: ")
                    Chp3_Task()
                else:
                    print("You hesitated to long and the golden anhk disapeared.")
            elif pickup <= outcome:
                print("You have no stregthen left and you succumed to your injuries.\n\n" )
                exit()
        else:
            print ("Invalid input, Please try again.\n\n ")
            print("Chapter 3: ")
            Chp3_Task()

#Chapter 4
def Chapter_4():
    print("Chapter 4: \n\n")
    print("As you navigate through the secret passage-way filled with cobwebs and spiders. You reach the end of the path and are amazed by the abundance of treasure: dazzling gems, well-crafted weapons, etc.\n\n")
    print("You're overjoyed and fathom at the situation. You dont even know where to begin. \n\n")
    Chp4_Task()

def Chp4_Task():
    global inventory 
    global disable
    
    option = int(input("Select an options:\n1:Explore the room\n2: Loot treasure room \n3:Input the key\nEnter choice: ")) 
    print("\n")
    if option == 1:
        disable = True
        print(" As you inspect the room, you disable the traps and you notice a circle with a ankh shaped-hole.\n\n ")
        print("Pick option 3!\n\n\n ")
        print("Chapter 4: ")
        Chp4_Task()

    elif option == 2:
        print("You hear a voice sayin 'Your greed has caused your demise! Hahahaha!' as you slowy turn into gold.\n\n ")
        exit()
    elif option == 3:
        if disable == True: 
            print(" You inspect the circle with the key size hole, You check your inventory\n\n\n ")
            if  a in inventory:
                ankh = True
                print(" You grab the ankh and decide to fit the ankh to the key size hole in the circle ,To your suprise the ankh fits perfectly, but suddently....\n\n")
                Chapter_5()
            else:
                print( "Retrace your steps and go fight the pack of jackals.\n\n")
                print("Chapter 3: ")
                Chp3_Task()
        else:
                print("You need deactivate the traps. Pick options 1!\n\n")
                print("Chapter 4: ")
                Chp4_Task()
    else:
        print ("Invalid input, Please try again.\n\n ")
        print("Chapter 4: ")
        Chp4_Task()

#Chapter 5

def Chapter_5():
    print("Chapter 5: \n\n")
    print("As you place the ankh in the ankh-size hole located in the middle of the circle. The room begins to shake and a podium rises from the middle of the room containing a book.\n\n") # intro
    print(" You begin to feel a unfathomable aura coming from the book, and you specualte that the books holds the origin of the world. Not being able to restrain yourself, you start slowly moving towards the book.\n\n") # Chapter 5 Scene
    Chp5_Task()
def Chp5_Task():
    option = int(input("Select an options:\n1:Open book\n2:Move away from book\n3:Explore deeper in the tomb\nEnter choice: ")) 
    print("\n")
    if option == 1:
        print("As you open the book, a sudden black mist disperse from within the book, and you fall to the ground unconsious\n\n")
        print("You wake up in Alabasta and do not remeber anything that happen.")
        
    elif option == 2:
        print("You return to your senses and quickly gather all the treasure you carry and ran back to Alabasta\n\n")
        print("You live a lavish life, but you will always remember the unforgetful incident that happen in the tomb.")

    elif option == 3:
        print(" To be continue.... Thank you for playing the game.\n\n")

    else:
        print ("Invalid input, Please try again.\n\n ")
        print("Chapter 5: ")
        Chp5_Task()



# Game Begins 
print("Game starts here: ")
intro()




