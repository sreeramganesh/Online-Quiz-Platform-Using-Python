import random
quiz_data = [
    {
        "question": "What is the capital of India?",
        "options": ["A) New Delhi", "B) Mumbai", "C) Chennai", "D) Kolkata"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Mark Twain", "D) Jane Austen"],
        "answer": "A"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A) Au", "B) Ag", "C) Gd", "D) Go"],
        "answer": "A"
    },
    {
        "question": "Which country invented Pizza?",
        "options": ["A) France", "B) Italy", "C) USA", "D) Greece"],
        "answer": "B"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["A) 1940", "B) 1945", "C) 1950", "D) 1939"],
        "answer": "B"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["A) Alan Turing", "B) Charles Babbage", "C) Bill Gates", "D) Steve Jobs"],
        "answer": "B"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    }
]
def run_quiz(name, quiz_data):
    score = 0
    random.shuffle(quiz_data)
    for q in quiz_data:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer == q["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(" Wrong! Correct answer:", q["answer"])
    print(f"\n{name}, your final score: {score}/{len(quiz_data)}")
    save_score(name, score, len(quiz_data))
def save_score(name, score, total):
    with open("results.txt", "a") as f:
        f.write(f"{name}: {score}/{total}\n")
def start_quiz():
    name = input("Enter your name: ")
    print(f"Welcome {name}! Let's start the quiz.")
    while True:
        run_quiz(name, quiz_data)
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye ")
            break
if __name__ == "__main__":
    start_quiz()
