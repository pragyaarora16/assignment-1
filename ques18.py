from collections import Counter


def are_anagrams(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Use Counter to count the frequency of each character in both strings
    return Counter(str1) == Counter(str2)




def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    if are_anagrams(str1, str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

if __name__ == '__main__':
     main()
