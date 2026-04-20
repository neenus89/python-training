#Make a quiz that has question with 4 option. Add 1 point if the answer is correct. Reduce 1 point if it is incorrect. Also it should have an option to skip a question and quit the quiz. Design the quiz using Dictionaries.
quiz = {
    "question1": {  
        "question": "What is the largest mammal on Earth?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    "question2": {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Diamond", "B. Graphite", "C. Quartz", "D. Topaz"],
        "answer": "A"
    },

    "question3": {
        "question": "Who was the first Prime Minister of India?",
        "options": ["A. Sardar Patel", "B. Jawaharlal Nehru", "C. Mahatma Gandhi", "D. Rajendra Prasad"],
        "answer": "B"
    },

    "question4": {
        "question":"How many bones are in the adult human body?",
        "options": ["A. 205", "B. 206", "C. 207", "D. 208"],
        "answer": "B"
    }
}

score = 0
for key, value in quiz.items():
    print(value["question"])
    for option in value["options"]:
        print(option)
    answer = input("Enter your answer (or type 'Q' to skip, 'S' to exit): ")
    
    if answer.upper() == 'S':
        print("Exiting the quiz. Your final score is:", score)
        break
    if answer.upper() == 'Q':
        print("Question skipped. Your current score is:", score)
        continue
    if answer.upper() == value["answer"]:
        score += 1
        print("Correct Answer! Your current score is:", score)
    if answer.upper() != value["answer"]:
        score -= 1
        print("Incorrect Answer! Your current score is:", score)