def main():
    # Prompts the user for the answer
    great_question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    # If answer is 42 or forty_two then Yes
    if is_forty_two(great_question):
        print("Yes")
    
    # If answer anything other then No
    else:
        print("No")

def is_forty_two(question):
    true_answer = ["42", "forty-two", "forty two"]
    return (question.lower().strip() in true_answer)

main()
