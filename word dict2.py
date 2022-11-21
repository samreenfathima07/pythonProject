def main():

    word_dictionary = {
        'hi': 'is a way of greeting',
        'eyes': 'is an organ to see',
        'earth': 'is a planet in space',
    }

    while True:
        word = input("enter a word : ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])


main()