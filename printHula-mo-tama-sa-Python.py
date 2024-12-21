def ask_question(question, options, correct_answer, score):
    print(question)
    for option in options:
        print(option)
    while True:
        answer = input("Please select your answer (A, B, C, or D): ")
        if answer in ["A", "B", "C", "D"]:
            if answer == correct_answer:
                score.append(answer)
            break
        else:
            print("Invalid input, only A, B, C, or D are allowed inputs.")
    return score

def display_results(name, difficulty, score, mistakes):
    print("RESULTS:\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("Name: " + name)
    print("Quiz difficulty: " + difficulty)
    print(f"Score: {len(score)}")
    print(f"Number of mistakes: {mistakes}\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

def quiz(difficulty, score):
    if difficulty == "Easy":
        score = ask_question("Question 1: What is Python primarily used for?", 
                             ["A. Web Development", "B. Machine Learning", "C. Data Analysis", "D. All of the Above"], 
                             "D", score)
        score = ask_question("Question 2: What is the output of 'print(3+4)'", 
                             ["A. 34", "B. 7", "C. 3", "D. Error"], 
                             "B", score)
        score = ask_question("Question 3: How do you create a list in Python?", 
                             ["A. <>", "B. { }", "C. []", "D. ()"], 
                             "C", score)
        score = ask_question("Question 4: What is the symbol to start a comment in Python?", 
                             ["A. #", "B. *", "C. //", "D. --"], 
                             "A", score)
        score = ask_question("Question 5: What is the correct way to create a variable in Python?", 
                             ["A. x = 5", "B. var x = 5", "C. let x = 5", "D. None of the Above"], 
                             "A", score)
    
    elif difficulty == "Normal":
        score = ask_question("Question 1: What is the output of this code: x = [1,2,3]\nprint(len(x))", 
                             ["A. 1", "B. 2", "C. 3", "D. Error"], 
                             "C", score)
        score = ask_question("Question 2: What does the break keyword do in Python?", 
                             ["A. Skips the current iteration of a loop", "B. Exits the loop entirely", "C. Terminates the program", "D. Pauses the execution temporarily"], 
                             "B", score)
        score = ask_question("Question 3: How to add an item to a list?", 
                             ["A. add()", "B. insert()", "C. append()", "D. extend()"], 
                             "C", score)
        score = ask_question("Question 4: Which of the following is NOT a valid Python data type?", 
                             ["A. List", "B. TupleSet", "C. Set", "D. Dictionary"], 
                             "B", score)
        score = ask_question("Question 5: What is the output of this code: for x in range (1,6)\nprint(x * 2, end=' ')", 
                             ["A. 2 4 6 8 10", "B. 1 2 3 4 5", "C. 2 3 4 5 6", "D. 10 4 2 6 8"], 
                             "A", score)

    elif difficulty == "Hard":
        score = ask_question("Question 1: What is the output of this code if the user inputs 10:\nx = input('Enter a number: ')\nprint(x * 2)", 
                             ["A. 20", "B. 1010", "C. 10", "D. Print Error"], 
                             "B", score)
        score = ask_question("Question 2: What is the output of this code:\nfor i in range(3):\n    for j in range(2):\n        if j == 1:\n            break\n        print(i, j)", 
                             ["A. 0 0\n1 0\n2 0", "B. 0 1\n1 1\n2 1", "C. Prints an Error message", "D. None of the Above"], 
                             "A", score)
        score = ask_question("Question 3: What does the term immutable mean in Python?", 
                             ["A. A variable whose value can be changed", "B. A variable whose value cannot be changed after creation", "C. A variable that can hold any data type", "D. A type of loop that never stops"], 
                             "B", score)
        score = ask_question("Question 4: Who created the Python programming language?", 
                             ["A. Jaes Gosling", "B. Guido van Rossum", "C. Bjarne Stroustrup", "D. Dennis Ritchie"], 
                             "B", score)
        score = ask_question("Question 5: What inspired the name Python for the programming language?", 
                             ["A. The founder's favorite pet", "B. A type of snake that represents flexibility", "C. The acronym for Pythagorean, related to mathematics", "D. The Monty Python comedy group, specifically Monty Python's Flying Circus"], 
                             "D", score)
    
    return score

def main():
    name = input("Enter your name: ")
    while True:
        score = []
        print("Hi " + name + "!, Let's test your knowledge in Python!")
        
        while True:
            print("Each difficulty will include 5 questions, please type the CAPITAL letter of your answer.")
            print("Please select quiz difficulty among the following:\n")
            print("-Easy")
            print("-Normal")
            print("-Hard\n")
            difficulty = input("Difficulty: ")
            if difficulty in ["Easy", "Normal", "Hard"]:
                break
            else:
                print("Invalid input, Type only Easy, Normal, or Hard")
        
        score = quiz(difficulty, score)
        mistakes = 5 - len(score)
        display_results(name, difficulty, score, mistakes)

        while True:
            more_quiz = input("Do you wish to take another Quiz?: ")
            if more_quiz == "Yes":
                break  
            elif more_quiz == "No":
                print("Thank you! We hope to have tested your knowledge on Python. Come again!")
                exit()
            else:
                print("Invalid input, Only type 'Yes' or 'No'.")

if __name__ == "__main__":
    main()
