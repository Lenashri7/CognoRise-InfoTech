import random
print("Welcome to Hangman-Game")
print("--------------------------------------")
words=["lenashri","manees","lalitha","kanishka","vijay","daimond","hemant"]
randomword=random.choice(words)
for x in randomword:
    print("_",end=" ")
def print_hangman(word):
    if word==0:
        print("\n+----+")
        print("     |")
        print("     |")
        print("     |")
        print("   ===")
    elif word==1:
        print("\n+----+")
        print("O    |")
        print("     |")
        print("     |")
        print("   ===")
    elif word==2:
        print("\n+----+")
        print("O    |")
        print("|    |")
        print("     |")
        print("   ===")
    elif word==3:
        print("\n+----+")
        print(" O    |")
        print("/|   |")
        print("     |")
        print("   ===")
    elif word==4:
        print("\n+----+")
        print(" O    |")
        print("/|\   |")
        print("     |")
        print("   ===")
    elif word==5:
        print("\n+----+")
        print(" O    |")
        print("/|\   |")
        print("/     |")
        print("   ===")
    elif word==6:
        print("\n+----+")
        print(" O    |")
        print("/|\   |")
        print("/ \    |")
        print("   ===")
        
def printword(guessedletter):
    count=0
    rightletters=0
    for ch in randomword:
        if(ch in guessedletter):
            print(randomword[count],end=" ")
        else:
            print(" ",end=" ")
        count+=1
    return rightletters

def printlines():
    print("\r")
    for ch in randomword:
        print("\u203E", end=" ")
length_of_word_to_guess=len(randomword)
amount_of_times_wrong=0
current_guess_index=0
current_letters_guessed=[]
current_letters_right=0

while(amount_of_times_wrong!=6 and current_letters_right!=length_of_word_to_guess):
    print("\nLetters guessed so for:")
    for letter in current_letters_guessed:
        print(letter,end=" ")
    letterguessed=input("\nGuess a letter: ")
    if(randomword[current_guess_index]==letterguessed):
        print_hangman(amount_of_times_wrong) 
        current_guess_index+=1
        current_letters_guessed.append(letterguessed)
        current_letters_right=printword(current_letters_guessed)
        printlines()
    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letterguessed)
        print_hangman(amount_of_times_wrong)
        current_letters_right=printword(current_letters_guessed)
        printlines()
print("The Game is over! Thanks for playing :)")