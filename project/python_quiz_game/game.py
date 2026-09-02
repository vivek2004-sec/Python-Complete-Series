
questions = ("How many elements are there in periodic table?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in earth's atmosphere?",
             "How many bones are there in human body?",
             "Which planet in the solar system is the hottest?")

options = (("A. 116", "B. 112", "C. 118", "D. 119"), 
           ("A. Whale", "B. Elephant", "C. Emu", "D. Ostrich"), 
           ("A. Nitrogen", "B. Hydrogen", "C. Argon", "D. Helium"), 
           ("A. 206", "B. 208", "C. 207", "D. 211   "),
           ("A. Mercury", "B. Venus", "C.  Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0

option_number = 0

for question in questions:
    print("_______________________")
    print(question)
    for option in options[option_number]:
        print(option)
        
    guess = input("Enter the answer(A, B, C, D):  ").capitalize()
    if guess  not in ['A', "B", "C", "D"]:
        print("Invalid Input")
        break
    else:
        continue
    
    option_number += 1