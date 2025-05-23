class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def is_correct(self, choice):
        return choice == self.answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("\nWelcome to the Easy Quiz!\n")
        for i, question in enumerate(self.questions, start=1):
            print(f"Q{i}: {question.prompt}")
            for idx, option in enumerate(question.options, start=1):
                print(f"  {idx}. {option}")
            
            try:
                user_choice = int(input("Your choice (1-4): "))
                if question.is_correct(user_choice):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.options[question.answer - 1]}\n")
            except (ValueError, IndexError):
                print("Invalid input. Moving to the next question.\n")

        self.show_results()

    def show_results(self):
        print(f"Quiz finished! Your score: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Amazing! You got all the answers right!")
        elif self.score > len(self.questions) // 2:
            print("Good job! Keep it up.")
        else:
            print("Don't worry, you'll do better next time.")


if __name__ == "__main__":
    # Define the quiz questions
    questions = [
        Question(
            "What color is the sky on a clear day?",
            ["Green", "Blue", "Red", "Yellow"],
            2  # Answer is "Blue"
        ),
        Question(
            "How many legs does a dog have?",
            ["2", "4", "6", "8"],
            2  # Answer is "4"
        ),
        Question(
            "What is 2 + 2?",
            ["3", "4", "5", "6"],
            2  # Answer is "4"
        ),
        Question(
            "Which fruit is known for its bright yellow peel?",
            ["Apple", "Orange", "Banana", "Grape"],
            3  # Answer is "Banana"
        )
    ]

    # Create and start the quiz
    quiz = Quiz(questions)
    quiz.start()
