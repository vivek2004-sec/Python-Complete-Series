import random
import time

# List of questions
questions = [
    "Who was the first Prime Minister of India?",
    "Who wrote the Mahabharat?",
    "Who was the first President of the United States?"
]

# List of options
options = [
    ["Jawaharlal Nehru", "Subhas Chandra Bose", "Mahatma Gandhi", "Lal Bahadur Shastri"],
    ["Ved Vyas", "Valmiki", "Tulsidas", "Vishwamitra"],
    ["George Washington", "John Kennedy", "Barack Obama", "Donald Trump"]
]

# List of correct answers (index-based for easier checking)
answers = [0, 0, 0]  # 0 corresponds to the first option of each

# List of prize money
prize_money = [100, 200, 500]

# Function to play the game
def play_game():
    prize = 0
    print("🎉 Welcome to Kaun Banega Crorepati 🎉\n")
    time.sleep(1)
    
    for i in range(len(questions)):
        print(f"\n🏆 Question {i+1} for ₹{prize_money[i]}:")
        print(questions[i])
        
        for j in range(4):
            print(f"{j+1}. {options[i][j]}")
        
        # Take user input and validate
        try:
            choice = int(input("Enter your option (1-4): "))
            if choice < 1 or choice > 4:
                print("❌ Invalid option! You lost the game.")
                break
        except ValueError:
            print("❌ Please enter a number! You lost the game.")
            break

        # Check answer
        if choice - 1 == answers[i]:
            prize += prize_money[i]
            print(f"✅ Correct! You have won ₹{prize}")
        else:
            print(f"❌ Wrong answer. The correct answer was: {options[i][answers[i]]}")
            print(f"You won ₹{prize}. Better luck next time!")
            break
        time.sleep(1)

    print(f"\n🎊 Game Over! Your total winnings: ₹{prize}")

# Start the game
play_game()
