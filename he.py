import random

wordlist = ["apple","table","chair","mouse","plant","bread","grape","snake","house","water","light","money","beach","candy","pizza"]

theword = random.choice(wordlist)
guesses = 6
won = False

print("welcome to wordleeeeeeeeeee!")
print()
print("ok so heres how it works")
print("u gotta guess a 5 letter word and u get 6 trys")
print("BIG letter = right letter right spot")
print("letter with a star * = its in the word but wrong spot")
print("the _ thing = nope its not in there")
print("good luck u got this!!")
print()


while guesses > 0:
    myguess = input("guess a word: ")
    myguess = myguess.lower()
    myguess = myguess.strip()   # my friend kept putting spaces so i added this

    if len(myguess) != 5:
        print("thats not 5 letters!! count again lol")
        print()
        continue

    if myguess == theword:
        print()
        print("YESSSS U WON!!!!!!")
        print("the word was " + theword)
        won = True
        break

    # the color/checking part (this was the hard part)
    answer = ""
    for i in range(0,5):
        if myguess[i] == theword[i]:
            answer = answer + myguess[i].upper()
        elif myguess[i] in theword:
            answer = answer + myguess[i] + "*"
        else:
            answer = answer + "_"

    print(answer)
    guesses = guesses - 1
    if guesses == 1:
        print("uh oh only 1 try left!!")
    else:
        print("u have " + str(guesses) + " trys left")
    print()

if won == False:
    print()
    print("noooo u ran out of trys :((((")
    print("the word was " + theword + " btw")
    print("try again ur almost good at it")



  




