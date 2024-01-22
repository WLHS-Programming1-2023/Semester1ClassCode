def owl_count(text):
    count = 0
    list_of_words = text.lower().split()
    for word in list_of_words:
        if "owl" in word:
            count += 1
    return count

def main():
    test_text = "The owl is not a fowl and is located in the owlery sitting in a bowl."
    print(owl_count(test_text))

if __name__ == "__main__":
    main()
    