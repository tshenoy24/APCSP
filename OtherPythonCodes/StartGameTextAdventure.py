import Main_TextAdventure
def StartGame():
    User = input("Enter your name: ")
#The input to put your name
    print("Hello", User +"!")
#When you enter your name it welcome's your name
StartGame()
User = input("Please confirm your name: ")
def ReadMe (thing_1,thing_2):
    print(thing_1 + thing_2)
#Sets up the function to add both the things for the questions
    
def Answer():
    ans = input ("Press any button to start! ")
#This asks the question
Answer()

def Load():
    print("Loading the game...")
    print("loading... ")
#Loads the game here
Load()

def Output1():
    print("Ok "+ User + " let me show you where we get our groceries and some of the best resturants around town ")
    #Output for when you say "Yes"
Output1()

def output1():
    print("Yea " + User + " you looked kinda tired today after a long trip. Please get comfy and let me know when your ready for me to show you around town")
    #output for when you say "No"
output1()

def Output2():
    print("Walking to the grocery stores...")
    ans4=input ("What do you want to buy? Press X for fruits, Y for seeds, and A for snacks. ")
    if ans4== ("X"):
                print("Loading fruits...")
                ans5=input ("You have currently 1000 coins. Apples cost 30 coins, bannanas cost 80 coins, and mangoes cost 25 coins. Press X for Apples, B for bannanas, or O for Mangoes.")
                if ans5== ("X"):
                        print("You bought some apples! Your remaining coins are 970 coins. Now what do you want to do? ")
                        ans6=input ("Press O for meeting with the local townspeople or Press A to start your farming.")
                        if ans6== ("O"):
                                print("loading...")
                                ans7=input ("You come to the center of town and see Jack, Luke, and Sam. Press A to talk to Jack, B to talk to Luke, and C to talk to Sam")
                                if ans7== ("A"):
                                            print("Hey " + User + " my name is Jack and I just welcomed you yesterday. How have you been liking it?")
                                            print("You talk to Sam for hours...")
                                elif ans7== ("B"):
                                            print("Oh hello " + User + " my name is Luke and I heard you just moved in. Would you like to come over to my house")
                                            print("You talk to Luke for hours...")
                                elif ans7== ("C"):
                                            print("Oh hello " + User + " I heard you just moved in yesterday. My name is Sam and I hope you enjoy your visit.")
                                            print("You talk to Sam for hours...")
                                            ans8==input ("You talked and socialized to the locals and are now coming home. It's 10 PM and your very tired so you go to sleep on your bed.")
                                            print("Loading...")
                                            ans9=input("You wake up at 6 am and are ready to go start your day off. You realize that you need to check on your farm. You see that your crops didn't make it. Press 'A' to fix your farm and replant the wheat seeds or Press 'B' to buy other seeds.")
                                            if ans9== ("A"):
                                                    print("You planted your wheat seeds and watered them. Out of nowhere they grow soo fast and are ready to harvest")
                                            elif ans9== ("B"):
                                                    print("You get the seeds of corn, potatoes, and tomatoes and decide to plant them and water them right away. You water them and out of nowhere your corn grows and is ready to harvest")
                                                    ans10=input("You get your crops and are ready to sell them. It's now 8 am and you have some crops and you realize there is a farmers market you can setup a stand and sell your crops. What do you want to do? Press 'A' to setup a stand and start sellng your crops or press 'B' to keep them")
                                                    if ans10== ("A"):
                                                        print("You setup your stand and sell your crops. Since your new around town you get people around your stand and they buy your crops and pay you a lot more than you charged. You are now at 4960 coins after the sale")
                                                        print("ACIEVEMENT UNLOCKED - Farmer's market")
                                                    elif ans10== ("B"):
                                                            print("You save all your crops and store them in your house and decide to plant more seeds. You have nothing much to do and feel a little tired after planitng and harvesting your crops. You sleep on your bed and wake up the next day")
                        elif ans6== ("A"):
                            print("loading...")
                            print("going back to your farm")
                            ans7=input ("Your back at your farm and you have some corn seeds, bean seeds, and wheat seeds. Press A to plant corn seeds, B to plant bean seeds, or C to plant wheat seeds.")
                            if ans7== ("A"):
                                print("You go to your shed behind your house and get the corn seeds. You got 10 corn seeds but havent tilled the soil or gotten any water to water the seeds.")
                                ans8=input("However you realize you need to till the ground or fill your watering can. Press 'A' to fill your watering can or Press 'B' to till the soil.")
                                if ans8== ("A"):
                                    print("Filling your watering can...")
                                    print("Loading...")
                                elif ans8== ("B"):
                                    print("Tilling the soil around you...")
                                    print("Loading...")
                elif ans5== ("B"):
                        print("You bought some bananas! Your remaining coins are 920 coins. Now what do you want to do? Press O for meeting with the local townspeople or Press A to start your farming.")
                elif ans5== ("O"):
                        print("You bought some Mangoes! Your remaining coins are 975 coins. Now what do you want to do? Press O for meeting with the local townspeople or Press A to start your farming.")
                        #The response for when you give an input
Output2()

def Output3():
        print("Going to the towncenter to meet some townspeople...")
        ans4=input ("You come to the center of town and see Jack, Luke, and Sam. Press A to talk to Jack, B to talk to Luke, and C to talk to Sam. ")
        if ans4== ("A"):
            print("Hey " + User + " my name is Jack and I just welcomed you yesterday. How have you been liking it?")
        elif ans4== ("B"):
            print("Oh hello " + User + " my name is Luke and I heard you just moved in. Let me tell you what this town is like")
        elif ans4== ("C"):
            print("Oh hello " + User + " I heard you just moved in yesterday. My name is Sam and I hope you enjoy your visit.")
            ans5==input ("After talking with the local townspeople for a long time you wake up and you see it's 12 PM and your feeling refreshed. Where do you want to go? Press 'A' to go to the towncenter, Press 'B' to harvest your crops, or Press 'C' to go to Jack's house. ")
            if ans5 == ("A"):
                print("Walking to towncenter...")
                print("loading...")
            elif ans5 == ("B"):
                print("Harvesting your crops...")
                print("loading...")
            elif ans5 == ("C"):
                print("Going to Jack's house...")
                print("loading...")
Output3()

def Output4():
     print("Going to your farm...")
     print("Loading...")
     print("Loading resources...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading tools...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading obstacles...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading...")
     print("Loading seeds...")
     print("Loading...")
     ans4=input ("Your Farm has been loaded! what do you want to start off with? Press 'A' to fill your water can, Press 'B' to till more ground, or press 'C' to plant some seeds")
     if ans4== ("A"):
         print("Filling your water can..")
         print("Loading...")
     elif ans4== ("B"):
         print("Tilling more ground...")
         print("Loading...")
     elif ans4== ("C"):
            ans5=input("You go to get the seeds and see 3 types of seeds. There are Wheat seeds, Corn seeds, and Bean seeds. Press 'A' to plant Wheat seeds, 'B' for Corn seeds, and 'C' for bean seeds.")
            if ans5== ("A"):
                print("Planting wheat seeds...")
                print("Loading...")
            elif ans5== ("B"):
                print("Planting corn seeds...")
                print("Loading...")
            elif ans5== ("C"):
                print("Planting bean seeds...")
                print("Loading...")
Output4()

def Output5():
    print("invalid response please press one of the three. Restart your game")
        
ans4=input ("")
Output5()

ans2=input ("Good morning " + User + " my name is Jack. I am your grandfather's old friend and I was told by him if you ever decide to move in to get you settled. I hope you enjoy your new countryside farmhouse that your grandfather left as a heritage. Would you like to start off with knowing where the stores are? ")

if ans2== ("Yes"):
    Load()
    Output1()
else:
    output1()


print("Loading...")
print("You get settled in the new countryside farmhouse and get to see your local stores and resturants")
print("June 6, 2018 6:00 am")

ans3=input ("Good morning " + User + " today's your first full day in your new countryside farmhouse. What do you want to do today? Press O for meeting the local townspeople, Press X for getting some groceries and food, Or press A to start your farming.")
if ans3== ("X"):
    Output2()
    
elif ans3== ("O"):
    Output3()
    
elif ans3== ("A"):
    Output4()
       
else:
    Output5()
    
