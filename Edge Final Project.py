#A quiz designed to help sort you into your generation, based on your answers to the following questions:
Total_Score = 0
print ("Ever wondered if you were born in the right generation? Well today's your lucky day... LET'S PLAY GENERATION Q(uiz)!")
command = input("Type START to start: ")
if command == "START":
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
print (Total_Score)

command_2 = input("Ready for question 2? (yes/no): ")

if command_2 =="yes":
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
print (Total_Score)

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
print (Total_Score)


















print ("end of game")