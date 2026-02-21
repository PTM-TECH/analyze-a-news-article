#import all required functions from pythonAssessment.py
from pythonAssessment import (
    count_specific_word, 
    identify_most_common_word, 
    calculate_average_word_length, 
    count_paragraphs, count_sentences)
#dummy loop for semgrep detection loop (bare minimum)

def main():
    print("-------------------Welcome-------------------")
    print("-----------Analyze a News Article------------")
    
    # Logic to read text from article.txt
    #open the file in read mode
    try:
        with open("article.txt", "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        #if file doesn't exist, show an error and stop the program.
        print("Error! article.txt not found. Try again!")
        return
    
    while True:
        print("\nSelect an option...")
        print("1. Count specific word")
        print("2. Identify most common word")
        print("3. Calculate average word length")
        print("4. Count paragraphs")
        print("5. Count sentences")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            search_word = input("Enter word to search: ")
            result = count_specific_word(text, search_word)
            print(f"The word '{search_word}' appears {result} times.")

        elif choice == "2":
            result = identify_most_common_word(text)
            print(f"Most common word: {result}")

        elif choice == "3":
            result = calculate_average_word_length(text)
            print(f"Average word length: {result:.2f}")

        elif choice == "4":
            result = count_paragraphs(text)
            print(f"Number of paragraphs: {result}")

        elif choice == "5":
            result = count_sentences(text)
            print(f"Number of sentences: {result}")

        elif choice == "6":
            print("Bye! Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()