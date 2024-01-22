def owl_count_two(text):
    indices = []
    list_of_words = text.lower().split()
    for index,word in enumerate(list_of_words):
        if "owl" in word:
            indices.append(index)
    return indices

def main():
    test_text = "The owl is not a fowl and is located in the owlery sitting in a bowl."
    owl_occurances = owl_count_two(test_text)
    print(f"There were {len(owl_occurances)} of owl")
    print(f"They occured at {str(" ".join(str(owl_occurances)))}")

if __name__ == "__main__":
    main()