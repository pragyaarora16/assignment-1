import string

def remove_punctuation(string1):
    # Create a translation table for removing punctuation
    translator = str.maketrans('', '', string1.punctuation)
    # Translate the input string using the translation table
    return string1.translate(translator)

# Example usage
string1 = input("Enter a string: ")
result = remove_punctuation(string1)
print("String without punctuation:", result)
