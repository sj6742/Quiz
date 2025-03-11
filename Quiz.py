import time
import threading
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

def print_title():
    title = pyfiglet.figlet_format("Python Quiz")
    print(Fore.CYAN + title)
    print(Fore.YELLOW + "Welcome to the Python Quiz Game!\n")

def timeout():
    print(Fore.RED + "\n⏳ Time's up! Moving to the next question...\n")
    global user_answer
    user_answer = None

def ask_question(question, options, correct_option):
    global score, user_answer
    print(Fore.LIGHTGREEN_EX + question)
    for option in options:
        print(Fore.LIGHTBLUE_EX + option)
    
    user_answer = None 
    timer = threading.Timer(time_limit, timeout) 
    timer.start()
    
    user_answer = input(Fore.YELLOW + "\nEnter your answer (A, B, C, or D): ").upper()
    timer.cancel()  

    if user_answer is None:
        print(Fore.RED + "❌ Skipped due to timeout!\n")
    elif user_answer == correct_option:
        print(Fore.GREEN + "✅ Correct! 🎉\n")
        score += 1
    else:
        print(Fore.RED + f"❌ Wrong! The correct answer is {correct_option}.\n")
    
    time.sleep(1) 

# Start the game
print_title()
playing = input(Fore.YELLOW + "Do you want to play? (yes/no): ").lower()
if playing != "yes":
    quit()

print(Fore.LIGHTMAGENTA_EX + "\nOkay! Let's play :)\n")

score = 0  
total_questions = 18  
time_limit = 15  

rounds = [
    ("🔵 ROUND 1: Beginner Level 🔵", [
        ("Q1) What is the output of `print(2 * 3 ** 2)`?", ["A) 36", "B) 18", "C) 12", "D) 9"], "B"),
        ("Q2) What is the data type of `range(5)` in Python?", ["A) list", "B) tuple", "C) range", "D) dict"], "C"),
        ("Q3) Which keyword is used to define a function in Python?", ["A) define", "B) function", "C) def", "D) fun"], "C"),
    ]),
    ("🟡 ROUND 2: Intermediate Level 🟡", [
        ("Q4) What does `list(range(3, 8, 2))` return?", ["A) [3, 5, 7]", "B) [3, 4, 5, 6, 7]", "C) [3, 8, 2]", "D) [3, 6, 9]"], "A"),
        ("Q5) What is the output of `bool('False')`?", ["A) False", "B) True", "C) Error", "D) None"], "B"),
    ]),
    ("🔴 ROUND 3: Advanced Level 🔴", [
        ("Q6) What is the time complexity of searching in a dictionary?", ["A) O(1)", "B) O(n)", "C) O(log n)", "D) O(n^2)"], "A"),
        ("Q7) What does `lambda x: x + 2` return?", ["A) A function", "B) x + 2", "C) None", "D) Error"], "A"),
    ])
]

for round_title, questions in rounds:
    print(Fore.MAGENTA + f"\n{round_title}\n")
    for q in questions:
        ask_question(*q)

average_score = (score / total_questions) * 100
print(Fore.CYAN + "\n🎉 Quiz Completed! 🎉")
print(Fore.YELLOW + f"Your Final Score: {score}/{total_questions}")
print(Fore.YELLOW + f"Your Average Score: {average_score:.2f}%")

if average_score == 100:
    print(Fore.GREEN + "🏆 Perfect Score! You're a Python expert! 🔥")
elif average_score >= 75:
    print(Fore.BLUE + "🎯 Great job! You're very skilled in Python! 👍")
elif average_score >= 50:
    print(Fore.LIGHTCYAN_EX + "😊 Good effort! Keep practicing! 📚")
else:
    print(Fore.RED + "😢 Keep learning! Practice makes perfect! 💡")

print(Fore.MAGENTA + "\nThanks for playing! 🚀")
