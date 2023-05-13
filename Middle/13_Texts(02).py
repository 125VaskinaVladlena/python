def count_words(text):
    text = text.strip()
    words = text.split()
    count = len(words)

    return count

text = input("Enter a string of text: ")

result = count_words(text)
print("Number of words in the text: ", result)