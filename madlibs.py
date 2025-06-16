# %%
while True:
    
    adj = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous person: ")

    madlib = f"Computer programming is so {adj}! It makes me so excited all the time because " \
             f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

    print("\n" + madlib + "\n")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

