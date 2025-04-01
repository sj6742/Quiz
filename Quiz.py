import time
import threading # USED FOR HANDLING TIME LIMITS
from colorama import Fore, Style, init #USED FOR COLORIES TEXT IN TERMINAL
import pyfiglet #CONVERT THE TEXT INTO ASCII (LARGE TEXT)
import random
import winsound  # For sound effects (Windows only)

init(autoreset=True)

# Sound feedback for correct/incorrect answers
def play_sound(is_correct):
    frequency = 1000  
    duration = 500  
    if is_correct:
        winsound.Beep(frequency, duration)  
    else:
        winsound.Beep(frequency // 2, duration)  

def print_title():
    title = pyfiglet.figlet_format("Python Quiz")
    print(Fore.CYAN + title)
    print(Fore.YELLOW + "Welcome to the Python Quiz Game!\n")

def timeout():
    print(Fore.RED + "\n⏳ Time's up! Moving to the next question...\n")
    global user_answer
    user_answer = None

def ask_question(question, options, correct_option, difficulty_points):
    global score, user_answer, incorrect_answers
    print(Fore.LIGHTGREEN_EX + question)
    random.shuffle(options) 
    
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
        play_sound(True)
        score += difficulty_points
    else:
        print(Fore.RED + f"❌ Wrong! The correct answer is {correct_option}.\n")
        play_sound(False)
        incorrect_answers.append((question, correct_option)) 
    
    time.sleep(1)

def save_leaderboard():
    with open("leaderboard.txt", "a") as file:
        file.write(f"Name: {name} | Score: {score} | Date: {time.ctime()}\n")

def review_incorrect_answers():
    if incorrect_answers:
        print(Fore.YELLOW + "\nReview of Incorrect Answers:")
        for question, correct_option in incorrect_answers:
            print(Fore.LIGHTRED_EX + f"Q: {question}\nCorrect Answer: {correct_option}\n")
    else:
        print(Fore.GREEN + "Great job! No incorrect answers to review.")

# Start the game
print_title()
name = input(Fore.YELLOW + "Enter your name: ")
playing = input(Fore.YELLOW + "Do you want to play? (yes/no): ").lower()
if playing != "yes":
    quit()

print(Fore.LIGHTMAGENTA_EX + "\nOkay! Let's play :)\n")
score = 0
total_questions = 18
time_limit = 15
incorrect_answers = []

rounds = [
    ("🔵 ROUND 1: Beginner Level 🔵", [
        ("Q1) What is the output of `print(2 * 3 ** 2)`?", ["A) 36", "B) 18", "C) 12", "D) 9"], "B", 1),
        ("Q2) What is the data type of `range(5)` in Python?", ["A) list", "B) tuple", "C) range", "D) dict"], "C", 1),
        ("Q3) Which keyword is used to define a function in Python?", ["A) define", "B) function", "C) def", "D) fun"], "C", 1),
        ("Q4) What is the correct syntax to print 'Hello, World!' in Python?", ["A) print('Hello, World!')", "B) echo 'Hello, World!'", "C) printf('Hello, World!')", "D) cout << 'Hello, World!';"], "A", 1),
        ("Q5) What is the index of the first element in a Python list?", ["A) 0", "B) 1", "C) -1", "D) Depends on the list"], "A", 1),
    ]),
    ("🟡 ROUND 2: Intermediate Level 🟡", [
        ("Q6) What does `list(range(3, 8, 2))` return?", ["A) [3, 5, 7]", "B) [3, 4, 5, 6, 7]", "C) [3, 8, 2]", "D) [3, 6, 9]"], "A", 2),
        ("Q7) What is the output of `bool('False')`?", ["A) False", "B) True", "C) Error", "D) None"], "B", 2),
        ("Q8) What will be the output of `set([1, 2, 2, 3, 4, 4])`?", ["A) {1, 2, 2, 3, 4, 4}", "B) {1, 2, 3, 4}", "C) [1, 2, 3, 4]", "D) (1, 2, 3, 4)"], "B", 2),
        ("Q9) What will `print(type(lambda x: x + 1))` return?", ["A) <class 'function'>", "B) <class 'lambda'>", "C) <class 'method'>", "D) <class 'callable'>"], "A", 2),
        ("Q10) What does `my_dict = {'a': 1, 'b': 2}; my_dict.pop('a')` return?", ["A) {'a': 1, 'b': 2}", "B) 1", "C) {'b': 2}", "D) None"], "B", 2),
    ]),
    ("🔴 ROUND 3: Advanced Level 🔴", [
        ("Q11) What is the time complexity of searching in a dictionary?", ["A) O(1)", "B) O(n)", "C) O(log n)", "D) O(n^2)"], "A", 3),
        ("Q12) What does `lambda x: x + 2` return?", ["A) A function", "B) x + 2", "C) None", "D) Error"], "A", 3),
        ("Q13) What will be the output of `sorted([3, 2, 1], key=lambda x: -x)`?", ["A) [1, 2, 3]", "B) [3, 2, 1]", "C) [-3, -2, -1]", "D) [None]"], "B", 3),
        ("Q14) Which of the following statements about Python’s Global Interpreter Lock (GIL) is true?", ["A) It allows multiple threads to execute in parallel.", "B) It prevents multi-threading in Python.", "C) It allows only one thread to execute at a time in CPython.", "D) It improves multi-threading performance."], "C", 3),
        ("Q15) What will `print({True: 'yes', 1: 'no', 0: 'maybe'})` output?", ["A) {'yes', 'no', 'maybe'}", "B) {'True': 'yes', 1: 'no', 0: 'maybe'}", "C) {'yes', 0: 'maybe'}", "D) {'no', 0: 'maybe'}"], "D", 3),
    ])
]

# Game loop
for round_title, questions in rounds:
    print(Fore.MAGENTA + f"\n{round_title}\n")
    for q in questions:
        ask_question(*q)


average_score = (score / total_questions) * 100
print(Fore.CYAN + "\n🎉 Quiz Completed! 🎉")
print(Fore.YELLOW + f"Your Final Score: {score}/{total_questions}")
print(Fore.YELLOW + f"Your Average Score: {average_score:.2f}%")

save_leaderboard()

review_incorrect_answers()

if average_score == 100:
    print(Fore.GREEN + "🏆 Perfect Score! You're a Python expert! 🔥")
elif average_score >= 75:
    print(Fore.BLUE + "🎯 Great job! You're very skilled in Python! 👍")
elif average_score >= 50:
    print(Fore.LIGHTCYAN_EX + "😊 Good effort! Keep practicing! 📚")
else:
    print(Fore.RED + "😢 Keep learning! Practice makes perfect! 💡")

print(Fore.MAGENTA + "\nThanks for playing! 🚀")
