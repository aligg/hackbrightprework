

print("Welcome to the adventure! To get started, I need your name")
username = raw_input("What is your name?")
print("Alright %s I hope you're excited for this journey" % (username))
favorite_animal = raw_input("What is your favorite animal?").lower()

if favorite_animal == "dog":
    print "Wow dogs are my favorite animal too. Did you know the average lifespan for a dog is 10-13 years?"
elif favorite_animal == "cat":
    print "I see, you're a cat person! That explains a lot! Did you know a group of cats is called a clowder? Rhymes with chowder!"
elif favorite_animal == "dragon":
    print "Dragons are legendary!"
else:
    print "I'm so sorry, I've never heard of that animal. "
    second_favorite_bool = raw_input("Would you like to journey with your second favorite animal?").lower()
    if second_favorite_bool == "yes":
        second_favorite_animal = raw_input("What is your second favorite animal?")
        print("Wow %s the %s is an awesome animal indeed!" % (username,second_favorite_animal))
    elif second_favorite_bool == "no":
        print("Okay bye %s!" % (username))