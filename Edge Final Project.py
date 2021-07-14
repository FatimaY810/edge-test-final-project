#A quiz designed to help sort you into your generation, based on your answers to the following questions:
import time
Total_Score = 0
print ("Ever wondered if you were born in the right generation? Well today's your lucky day... LET'S PLAY GENERATION Q(uiz)!")
command = input("Type START to start EXIT to exit: ")
while command == "START"or command == "start":
    command = input("Question 1: What Social Media App do you use most often? \n a. TikTok \n b. Instagram \n c. Facebook \n d. I prefer face-to-face commnication \n ANS HERE: ")
    while command != "a" or command != "b" or command != "c" or command != "d":
        if command == "a":
            print ("good answer! On your way to becoming Tiktok Famous :p")
            Total_Score = Total_Score + 10
            break
        elif command == "b":
            print ("Nice! Getting the likes and followers :)")
            Total_Score = Total_Score + 20
            break
        elif command == "c":
            print ("Cool! How are the embarassing family pictures going? :)")
            Total_Score = Total_Score + 30
            break
        elif command == "d":
            print ("old school is underrated!")
            Total_Score = Total_Score + 40
            break
        else:
            print ("ERROR")
            command = input('try again: ')

    time.sleep (2)
    command = input ("Question 2: What was your first telecommunication device (trying to not make the oldies feel older :) ) \n a. Some sort of smartphone (yes, android counts) \n b. A flip phone \n c. a brick phone \n d. those landlines with the dials \n ANS HERE: ")
    while command != "a" or command != "b" or command != "c" or command != "d":
        if command == "a":
            print ("ahhh the wonders of technology")
            Total_Score = Total_Score + 10
            break
        elif command == "b":
            print ("I understand if you too were addicted to the wonders of agressive flipping")
            Total_Score = Total_Score + 20
            break
        elif command == "c":
            print ("Yikes that SOUNDS heavy")
            Total_Score = Total_Score + 30
            break
        elif command == "d":
            print ("I've always wanted to use one of those...'")
            Total_Score = Total_Score + 40
            break
        else:
            print ("ERROR")
            command = input('try again: ')

    time.sleep (2)
    command = input ("Question 3: What slang did/do you use most often as a teenager? \n a. Bet \n b. Sorry not sorry \n c. Gnarly! \n d.) Don't flip your wig! \n ANS HERE:")
    while command != "a" or command != "b" or command != "c" or command != "d":
        if command == "a":
            print ("Alright, bet")
            Total_Score = Total_Score + 10
            break
        if command == "b":
            print ("Atittude much?")
            Total_Score = Total_Score + 20
            break
        if command == "c":
            print ("Sounds like surfer slang tbh")
            Total_Score = Total_Score + 30
            break
        if command == "d":
            print ("Damn...")
            Total_Score = Total_Score + 40
            break
        else:
            print ("ERROR")
            command = input('try again: ')

    time.sleep (2)
    command = input ("Question 4: What is your favorite movie out of the following? \n a. To All The Boys I've Loved Before  \n b. Mean Girls \n c. The Breakfast Club \n d.) The Graduate \n ANS HERE:")
    while command != "a" or command != "b" or command != "c" or command != "d":
        if command == "a":
            print ("")
            Total_Score = Total_Score + 10
            break
        if command == "b":
            print ("Atittude much?")
            Total_Score = Total_Score + 20
            break
        if command == "c":
            print ("Sounds like surfer slang tbh")
            Total_Score = Total_Score + 30
            break
        if command == "d":
            print ("Damn...")
            Total_Score = Total_Score + 40
            break
        else:
            print ("ERROR")
            command = input('try again: ')

    time.sleep (2)

    print ("THE FINAL QUESTION...")
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)

    command = input ("Question 5: Who would you consider your most favorite/well-known artist out of the following? \n a. Ariana Grande  \n b. Britney Spears \n c. David Bowie \n d.) Patsy Cline \n ANS HERE:")
    while command != "a" or command != "b" or command != "c" or command != "d":
        if command == "a":
            print ("Can you hit those high notes tho?")
            Total_Score = Total_Score + 10
            break
        if command == "b":
            print ("Oops, I did it again!")
            Total_Score = Total_Score + 20
            break
        if command == "c":
            print ("LEGEND")
            Total_Score = Total_Score + 30
            break
        if command == "d":
            print ("A unique but beautiful voice <3")
            Total_Score = Total_Score + 40
            break
        else:
            print ("ERROR")
            command = input('try again: ')


    time.sleep (2)
    print ("Now, the moment you've all been waiting for: Results! ")
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)

    print ("Your total score is: ", Total_Score)

    if Total_Score <= 87:
        print ("You are a true member of Gen Z!! You guys are truly making a mark with your wild ways! We love legacy makers <3... keep confusing everyone with your weird out-of-context TikTok trends my 4lifers ")
    elif Total_Score in range (88,125):
        print ("HELLOOOO my millenial folk! Tbh you guys really need to step out of your Harry Potter and Pumpkin Spice Latte phase :p... but it's all cool fellas because that's what makes you guys so unique! Have fun #adulting (insert skull emoji here idky i would even say that)")
    elif Total_Score in range (125,162):
        print ("What's up my Gen X peopleeeee. You're in the same generation as my parents... HIGH FIVE!")
    else:
        print ("Greetings, Baby Boomers! Yeah that sounds like an insult even if i didn't mean for it to. Tbh you guys has a terrible rep right now so I suggest keeping lowkey. :)")

    print ("Hope you enjoyed!)

print ("end of game")