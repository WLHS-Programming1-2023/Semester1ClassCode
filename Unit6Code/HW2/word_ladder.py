# function to ask user to enter index
def get_index(word):
    word_length = len(word)
    while True:
        index = int(input("Enter an index: "))
        if (index >= 0 and index < word_length) or (index == -1):
            return index
        else:
            print("Invalid index")

# function to ask user to enter a letter
def get_letter():
    while True:
        letter = input("Enter a letter: ")
        if len(letter) != 1:
            print("Must be a single letter")
            
        elif not letter.islower():
            print("Must be a lower case letter")
            
        else:
            return letter

def main():
    word = input("Enter a word: ")
    word_list = list(word)

    while True:
        index = get_index(word)
        if index == -1:
            break
        letter = get_letter()
        word_list[index] = letter
        print("".join(word_list))
        


if __name__ == "__main__":
    main()
