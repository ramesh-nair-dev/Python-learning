# All vowel is converted to 'g'

word = input("Enter a word: ")
vowels = "aeiouAEIOU"


def translateWord(word):
    translatedWord =""
    for letter in word:
        if letter in vowels:
            translatedWord += "g"
        else:
            translatedWord += letter
    return translatedWord

finaltranlatedWord = translateWord(word)
print("Translated word:", finaltranlatedWord)

# This code takes a word input from the user and translates it by replacing all vowels (both uppercase and lowercase) with the letter 'g'.
# The translated word is then printed to the console.
# The code uses a for loop to iterate through each letter in the input word.
# If the letter is a vowel, it appends 'g' to the `translatedWord`; otherwise, it appends the original letter.
# The final result is a new string where all vowels have been replaced with 'g'.
# This is a simple example of string manipulation in Python, demonstrating how to iterate through characters in a string and conditionally modify them.
# The output will show the original word with all vowels replaced by 'g'.
# For example, if the user inputs "hello", the output will be "hgllg".
